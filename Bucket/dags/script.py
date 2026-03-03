import datetime
import io
import logging
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor  # Import du Sensor
from PIL import Image

BUCKET_IN = "images-brutes"
BUCKET_OUT = "images-web"
CONN_ID = "minio_default"

logger = logging.getLogger("airflow.task")


def convert_to_grayscale():
    s3 = S3Hook(aws_conn_id=CONN_ID)
    keys = s3.list_keys(bucket_name=BUCKET_IN)

    if not keys:
        logger.info("Aucune image trouvee.")
        return

    for key in keys:
        if key.endswith("/"):
            continue

        try:
            file_obj = s3.get_key(key, BUCKET_IN)
            file_content = file_obj.get()["Body"].read()

            img = Image.open(io.BytesIO(file_content))
            bw_img = img.convert("L")

            output_buffer = io.BytesIO()
            fmt = img.format if img.format else "JPEG"
            bw_img.save(output_buffer, format=fmt)
            output_buffer.seek(0)

            new_key = f"bw_{key}"
            s3.load_file_obj(
                file_obj=output_buffer,
                key=new_key,
                bucket_name=BUCKET_OUT,
                replace=True,
            )

            s3.delete_objects(bucket=BUCKET_IN, keys=key)
            logger.info("Succes : %s converti", key)

        except Exception as e:
            logger.error("Erreur pour %s : %s", key, str(e))


with DAG(
    dag_id="minio_grayscale_pipeline",
    start_date=datetime.datetime.now(),
    schedule_interval=timedelta(seconds=10),
) as dag:
    wait_for_image = S3KeySensor(
        task_id="wait_for_image",
        bucket_name=BUCKET_IN,
        bucket_key="*",
        wildcard_match=True,
        aws_conn_id=CONN_ID,
        poke_interval=10,
        timeout=60 * 5,
    )

    process_task = PythonOperator(
        task_id="process_images",
        python_callable=convert_to_grayscale,
    )

    wait_for_image >> process_task

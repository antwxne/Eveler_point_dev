FROM python:3.11.7

WORKDIR /build
RUN pip install notebook
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
EXPOSE 8888
CMD jupyter notebook  --allow-root --no-browser --ip=0.0.0.0 --port=8888 --NotebookApp.token='' --NotebookApp.password=''

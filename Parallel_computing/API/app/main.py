import random
import time
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class MeterConso(BaseModel):
    meter_id: int
    consommation: int
    unit: str


METER_CONSO: List[MeterConso] = [
    MeterConso(meter_id=i, consommation=random.randint(0, 10000), unit="W")
    for i in range(200)
]

SLEEP_TIME: List[float] = [random.randint(1, 5) / 100 for _ in range(200)]


@app.get("/meter/{meter_id}/conso")
def get_meter_consommation(meter_id: int) -> MeterConso:
    try:
        meter: MeterConso = METER_CONSO[meter_id]
        time.sleep(SLEEP_TIME[meter_id])
        return meter
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

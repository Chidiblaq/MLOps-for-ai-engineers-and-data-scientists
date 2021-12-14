from body_mass_index import bmi_calculator
from fastapi import FASTAPI, Request
import uvicorn

#instantiate fastapi
app = FASTAPI()
@app.get("/")
async def get_input(request:Request):
    packet = await request.json()
    weight = packet['weight_kg']
    height = packet['height_m']

    bmi = bmi_calculator(weight, height)

    return bmi


if __name__ == '__main__':
    uvicorn.run()
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/bmi")
def calculate_bmi(weight: float, height: float):
    if weight <= 0:
        raise HTTPException(
            status_code=400,
            detail="Weight must be greater than zero"
        )

    if height <= 0:
        raise HTTPException(
            status_code=400,
            detail="Height must be greater than zero"
        )

    bmi = round(weight / (height ** 2), 2)

    return {
        "weight": weight,
        "height": height,
        "bmi": bmi
    }

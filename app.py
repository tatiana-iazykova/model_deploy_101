from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from model import Model

app = FastAPI()
model = Model()


class Request(BaseModel):
    text: str
    return_proba: bool = False


class Response(BaseModel):
    label: str
    proba: Optional[float] = None


@app.post("/predict")
def predict(request: Request) -> Response:
    response = model.predict(request.text, return_proba=request.return_proba)
    if request.return_proba:
        return Response(label=response[0], proba=response[1])
    return Response(label=response)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

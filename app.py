from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from dto import ItemCardIn, ItemCardOut
from model import Model

app = FastAPI()
model = Model()


@app.post("/moderation/")
def predict(request: ItemCardIn) -> ItemCardOut:
    response = model.predict(item_card=request.card)
    return ItemCardOut(label=response)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

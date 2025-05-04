from pydantic import BaseModel


class Config(BaseModel):
    model_path: str
    threshold: float
    template: str
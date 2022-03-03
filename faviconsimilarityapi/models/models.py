from pydantic import BaseModel


class ImageQuery(BaseModel):
    url:str

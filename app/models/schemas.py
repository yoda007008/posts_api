from typing import Optional
from pydantic import BaseModel

class SCreatePost:
    def __init__(
    self, 
    id: int,
    text: str,
    like: Optional[bool]
    ):
        self.id = id
        self.text = text
        self.like = like

class SLikePost:
    def __init__(
    self,
    id: int):
        self.id = id

class UpgradePost(BaseModel):
    text: str
    


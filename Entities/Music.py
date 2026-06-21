from pydantic import BaseModel
from typing import Optional

class Music(BaseModel):
    code: Optional[int] = None 
    name: str
    artist: str
    isPending: bool = True
    
from pydantic import BaseModel
from typing import List

class ReviewRequest(BaseModel):
    reviews: List[str]
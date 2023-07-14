from pydantic import BaseModel, Field
from typing import Optional

class CreateUserData(BaseModel):
    activeloop_token_id: str = Field(..., example="0x06012c8cf97bead5deae237070f9587f8e7a266d")
    chatgpt_api_key: str = Field(..., example = "0x8io143213nkjnjf3n2kjnd3j2kndjndnj3donojn")
    activeloop_org_id: str = Field(..., example="activeloop")

    class Config:
        orm_mode = True

class CreateQuery(BaseModel):
    id: Optional[int]
    query: str = Field(..., example = "I'm not sure if I can afford this. It's a bit expensive. The sky is blue. I like the color blue.")
    objection: Optional[str] = Field(default = 'No sales objection found in query', example = "It's a bit expensive.")
    response: Optional[str] = Field(default='No recommendation provided for the sales objection')

    class Config:
        orm_mode = True



from pydantic import BaseModel, Field
from typing import Optional

class CreateUserData(BaseModel):
    chatgpt_api_key: str = Field(..., example = "0x8io143213nkjnjf3n2kjnd3j2kndjndnj3donojn")

    class Config:
        orm_mode = True

class CreateQuery(BaseModel):
    id: Optional[int]
    query: str = Field(..., example = "I'm not sure if I can afford this. It's a bit expensive. The sky is blue. I like the color blue.")
    sales_objection: Optional[str] = Field(default = 'No sales objection found in query', example = "It's a bit expensive.")
    response: Optional[str] = Field(default='No recommendation provided for the sales objection', example = "Try finding alternatives to the budget")

    class Config:
        orm_mode = True



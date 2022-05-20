from pydantic import BaseModel, Field

class Input(BaseModel):
    Date: str = Field(
        ...,
        description="A string that contains the answer to the question.",
        example="2020-04-01",
        max_length=10,
        min_length=10,
    )
    max_temp: float = Field(
        ...,
        description="A string that contains the answer to the question.",
        example=7.7,
    )
    sun_mins: int = Field(
        ...,
        description="A string that contains the answer to the question.",
        example=43,
    )
    wspd: float = Field(
        ...,
        description="A string that contains the answer to the question.",
        example=38.2,
    )

class Output(BaseModel):
    beach_chairs: int

def predict(input: Input) -> Output:
    """Returns the `message` of the input data."""
    return Output(message=input.message)
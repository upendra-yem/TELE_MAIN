'''from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponsess

app = FastAPI() 

class InputData(BaseModel):
    text: str
class OutputData(BaseModel):
    message: str

@app.post("/output", response_model = OutputData)
def process_input(input_data : InputData):
    text = input_data.text
    # Process the input text and generate a response
    response_message = f"Received input: {text}"
    return OutputData(message=response_message)'''
InputData = input("Enter input text: ")
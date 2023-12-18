from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


origins = ["*"]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class FormData(BaseModel):
    name: str
    surname: str
@app.post("/postData")
def process_form(data: FormData):
    # Handle the form data received from Angular
    # Process the data as needed
     full_name = f"{data.name} {data.surname}"
     return {"result": full_name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8081)
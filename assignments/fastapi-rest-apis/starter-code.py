from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# Add your routes here
# Example:
# @app.get("/items")
# def get_items():
#     return [{"id": 1, "name": "Sample item"}]

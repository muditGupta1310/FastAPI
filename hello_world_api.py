from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world!"}


@app.get('/about')
def about():
    return {'message':'FastAPI uses a ASGI (Asynchronous Server Gateway Interface) server to handle requests. This allows for asynchronous programming, which can improve performance for I/O-bound operations.'}
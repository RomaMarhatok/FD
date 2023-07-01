from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping() -> dict[str, bool]:
    return {
        "ping": True,
    }

from fastapi import FastAPI


app = FastAPI(
    title="FastAPI Lesson 1"
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Добро пожаловать в моё приложение FastAPI!"
    }

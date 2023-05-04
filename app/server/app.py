from fastapi import FastAPI
from server.routes.student import router as StudentRouter
app = FastAPI()
app.include_router(StudentRouter, tags=["Students"], prefix="/student")


@app.get("/", tags=["Root"])
async def get_root():
    return {'message': 'This is my first project'}


from fastapi import FastAPI
import uvicorn

from api.blog import Api

app = FastAPI()

app.include_router(router=Api.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

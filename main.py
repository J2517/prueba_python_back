from fastapi import FastAPI
import logging
from app.routers.user_routes import router

logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
   filename='app.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="JSONPlaceholder API Integration")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

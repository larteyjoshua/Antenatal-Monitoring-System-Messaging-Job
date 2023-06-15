from app.processTextMessage import sendingVoiceSMS, processingDayBeforeTextMessaging, processingTodayTextMessaging
from fastapi import FastAPI, BackgroundTasks
import uvicorn
import time
import sys


app = FastAPI()


@app.on_event("startup")
async def runSystem():
    background_tasks = BackgroundTasks()
    sendingVoiceSMS(background_tasks)
    processingDayBeforeTextMessaging(background_tasks)
    processingTodayTextMessaging(background_tasks)
    await background_tasks()
    time.sleep(60)
    sys.exit("Job Execution  Completed.Application Exit")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# runSystem()

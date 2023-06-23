from app.processTextMessage import processingTodayTextMessaging
from loguru import logger
import sys


def runSystem():
    processingTodayTextMessaging()


if __name__ == "__main__":
    try:
        runSystem()
    except Exception as e:
        logger.info(str(e))
        sys.exit(1)

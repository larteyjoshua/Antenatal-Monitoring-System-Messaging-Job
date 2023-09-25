from app.models.model import Activity
from loguru import logger
from app.utils.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_activity(mother_id: int, status: str):
    db_string = settings.SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)

    new_activity = Activity(
        expected_mother_id=mother_id,
        activity_type='voice',
        status=status
    )
    db = Session()
    try:
        db.add(new_activity)
        db.commit()
        db.refresh(new_activity)
        logger.info('New Activity Inserted!')
    except Exception as e:
        db.rollback()
        logger.info(e)
    finally:
        db.close()
    return new_activity

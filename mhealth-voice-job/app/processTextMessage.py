from app.models import model
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils import config
from loguru import logger
from app.utils.dateUtils import count_days
from app.helpers.arkeselTextMessage import sendVoiceSMS
from app import create_activities


def sendingVoiceSMS():
    logger.info("Voice Message Processing Begin")
    db_string = config.settings.SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)
    db = Session()

    appointments = db.query(model.Appointment).all()
    for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.strptime(
            appointmentData.appointed_date, "%m/%d/%Y").date()

        oneDaysToAppointment = count_days(str(appointedDate))

        if appointmentData.attended == False and oneDaysToAppointment == 1:
            logger.info('Condition Check = ' +
                        str(oneDaysToAppointment))
            mother = db.query(model.ExpectedMother).filter(
                model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                respond = sendVoiceSMS(phone_number)
                status = respond['status']
                mother_id = mother.id
                create_activities.create_activity(mother_id, status)
    db.close()
    logger.info("Voice Message Processing End")

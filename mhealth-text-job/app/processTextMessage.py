from app.models import model
from datetime import datetime
from app.helpers.arkeselTextMessage import sendSMS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils import config
from loguru import logger
from app.utils.dateUtils import count_days


def processingTodayTextMessaging():
    logger.info("Text Message Processing Begin")
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
        if appointmentData.attended == False and oneDaysToAppointment == True:
            logger.info('Condition Check = ' +
                        str(oneDaysToAppointment))
            mother = db.query(model.ExpectedMother).filter(
                model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                phone_numbers = [phone_number]
                sender = config.settings.SENDER_ID
                message = "Hi {},\n You are reminded to report to Antenatal on {} at {}.\n Thank You!".format(mother.first_name, appointmentData.appointed_date,
                                                                                                              appointmentData.appointed_time)
                sendSMS(sender, message, phone_numbers)
    db.close()
    logger.info("Text Message Processing End")

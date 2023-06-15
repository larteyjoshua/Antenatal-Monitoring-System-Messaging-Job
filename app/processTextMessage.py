from app.models import model
from datetime import datetime, timedelta
from app.tasks import send_text_message, send_voice_message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils import config
from loguru import logger


def processingDayBeforeTextMessaging(background_tasks):
    db_string = config.settings.SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)
    db = Session()

    appointments = db.query(model.Appointment).all()
    for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.strptime(
            appointmentData.appointed_date, "%m/%d/%Y").date()
        oneDaysToAppointment = appointedDate - timedelta(days=1)
        if appointmentData.attended is False and oneDaysToAppointment:
            mother = db.query(model.ExpectedMother).filter(
                model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                phone_numbers = [phone_number]
                sender = config.settings.SENDER_ID
                message = "Hi {},\n This is a quick Remainder that you are expected to come Antenatal on {} at {}.\n Thank You!".format(mother.first_name, appointment.appointed_date,
                                                                                                                                        appointment.appointed_time)
                # task = send_text_message.delay(
                #     sender, message, phone_numbers)
                background_tasks.add_task(
                    send_text_message, sender, message, phone_numbers)
    db.close()
    logger.info("Sending Message to expected Mother")


def processingTodayTextMessaging(background_tasks):
    db_string = config.settings.SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)
    db = Session()

    appointments = db.query(model.Appointment).all()
    for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.today().strftime('%m/%d/%Y')

        if appointmentData.attended is False and appointmentData.appointed_date == appointedDate:
            mother = db.query(model.ExpectedMother).filter(
                model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                phone_numbers = [phone_number]
                sender = config.settings.SENDER_ID
                message = "Hi {},\n This is a quick Remainder that you are expected to come Antenatal on {} at {}.\n Thank You!".format(mother.first_name, appointment.appointed_date,
                                                                                                                                        appointment.appointed_time)
                # task = send_text_message.delay(
                #     sender, message, phone_numbers)
                background_tasks.add_task(
                    send_text_message, sender, message, phone_numbers)
    db.close()
    logger.info("Sending Message to expected Mother")


def sendingVoiceSMS(background_tasks):
    db_string = config.settings.SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)
    db = Session()

    appointments = db.query(model.Appointment).all()
    for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.strptime(
            appointmentData.appointed_date, "%m/%d/%Y").date()
        oneDaysToAppointment = appointedDate - timedelta(days=1)
 # if appointmentData.attended is False and oneDaysToAppointment:
        if appointmentData.attended is False:
            mother = db.query(model.ExpectedMother).filter(
                model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                # task = send_voice_message.delay(phone_number)
                background_tasks.add_task(send_voice_message, phone_number)
    db.close()
    logger.info("Sending Voice to expected Mother")

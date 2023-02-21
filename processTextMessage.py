from models import model
from datetime import datetime, timedelta
import calendar
import tasks
from sqlalchemy import create_engine   
from sqlalchemy.orm import sessionmaker
from utils import config


import logging

def processingDayBeforeTextMessaging():
     db_string = config.settings.SQLALCHEMY_DATABASE_URL
     con = create_engine(db_string)  
     Session = sessionmaker(con)  
     db = Session()
     
     appointments = db.query( model.Appointment).all()
     for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.strptime(appointmentData.appointed_date, "%m/%d/%Y").date()
        oneDaysToAppointment = appointedDate - timedelta(days = 1)
        if appointmentData.attended is False and oneDaysToAppointment:
            mother = db.query(model.ExpectedMother).filter(model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                phone_numbers = [phone_number]
                sender = config.settings.MESSAGE_SENDER
                message = "Hi {},\n This is a quick Remainder that you are expected to come Antenatal on {} at {}.\n Thank You!".format(mother.name,appointment.appointed_date,
                appointment.appointed_time)
                task = tasks.send_text_message.delay(sender, message, phone_numbers)
     db.close()   
     logging.info("Sending Message to expected Mother")


def processingTodayTextMessaging():
     db_string = config.settings.SQLALCHEMY_DATABASE_URL
     con = create_engine(db_string)  
     Session = sessionmaker(con)  
     db = Session()
     
     appointments = db.query( model.Appointment).all()
     for appointment in appointments:
        appointmentData = appointment
        appointedDate = datetime.today().strftime('%m/%d/%Y')

        if appointmentData.attended is False and appointmentData.appointed_date == appointedDate:
            mother = db.query(model.ExpectedMother).filter(model.ExpectedMother.id == appointmentData.expected_mother_id).first()
            if mother is not None:
                number = mother.telephone
                phone_number = "233" + number[1:]
                phone_numbers = [phone_number]
                sender = config.settings.MESSAGE_SENDER
                message = "Hi {},\n This is a quick Remainder that you are expected to come Antenatal on {} at {}.\n Thank You!".format(mother.name,appointment.appointed_date,
                mother.name,appointment.appointed_time)
                task = tasks.send_text_message.delay(sender, message, phone_numbers)
     db.close()   
     logging.info("Sending Message to expected Mother")
          
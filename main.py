# main.py
from datetime import datetime
from User import User
from sqlalchemy import text
from db_cofig import local_session, create_all_entities


create_all_entities()


cars_list = [Car(name='Honda', model='Civic', year='2016'), Car(name='Hyundai', model='Sonata',year='2021')]
local_session.add_all(cars_list)
local_session.commit()


# print all cars
cars = local_session.query(Cars).all()
print(cars)
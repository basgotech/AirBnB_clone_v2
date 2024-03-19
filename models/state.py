#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        getter = models.storage.all()
        coll_list = []
        get_result = []
        for key_graper in getter:
            city_get = key_graper.replace('.', ' ')
            city_get = shlex.split(city_get)
            if (city_get[0] == 'City'):
                coll_list.append(getter[key_graper])
        for attr_getter in coll_list:
            if (attr_getter.state_id == self.id):
                get_result.append(attr_getter)
        return (get_result)

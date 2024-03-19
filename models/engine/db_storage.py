#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """ create tables"""
    __engine = None
    __session = None

    def __init__(self):
        MySQL_user = getenv("HBNB_MYSQL_USER")
        MySQL_password = getenv("HBNB_MYSQL_PWD")
        MySQL_database = getenv("HBNB_MYSQL_DB")
        MySQL_host = getenv("HBNB_MYSQL_HOST")
        env_db = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(MySQL_user, MySQL_password, MySQL_host, MySQL_database),
                                      pool_pre_ping=True)

        if env_db == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        """
        dic_coll = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_grabber = self.__session.query(cls)
            for attr_val in query_grabber:
                key_grapper = "{}.{}".format(type(attr_val).__name__, attr_val.id)
                dic_coll[key_grapper] = attr_val
        else:
            list_coll = [State, City, User, Place, Review, Amenity]
            for iden in list_coll:
                query_grabber = self.__session.query(iden)
                for attr_val in query_grabber:
                    key_grapper = "{}.{}".format(type(attr_val).__name__, attr_val.id)
                    dic_coll[key_grapper] = attr_val
        return (dic_coll)

    def new(self, obj):
        """add a new attribute value in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes and commit
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an attribute value in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration of all
        """
        Base.metadata.create_all(self.__engine)
        rell = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(rell)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()

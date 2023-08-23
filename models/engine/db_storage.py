#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class DBStorage:
    """This class manages MySql Storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initialize a new DBStorage instance"""
        mySqlUser = getenv("HBNB_MYSQL_USER")
        mySqlPWD = getenv("HBNB_MYSQL_PWD")
        mySqlHost = getenv("HBNB_MYSQL_HOST")
        mySqlDB = getenv("HBNB_MYSQL_DB")
        hbnbEnv = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{mySqlUser}:{mySqlPWD}@{mySqlHost}/{mySqlDB}",
            pool_pre_ping=True
        )

        if hbnbEnv == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

            If cls is None, queries all types of objects.
        """
        if cls is None:
            objs = []
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {f"{type(obj).__name__}.{obj.id}" for obj in objs}

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the database session"""
        self.__session.close()

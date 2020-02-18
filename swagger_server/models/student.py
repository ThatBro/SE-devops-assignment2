# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Student(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, grades: Dict[str, str]=None):  # noqa: E501
        """Student - a model defined in Swagger

        :param id: The id of this Student.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this Student.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Student.  # noqa: E501
        :type last_name: str
        :param grades: The grades of this Student.  # noqa: E501
        :type grades: Dict[str, str]
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'grades': Dict[str, str]
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'grades': 'grades'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._grades = grades

    @classmethod
    def from_dict(cls, dikt) -> 'Student':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student of this Student.  # noqa: E501
        :rtype: Student
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Student.


        :return: The id of this Student.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Student.


        :param id: The id of this Student.
        :type id: int
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Student.


        :return: The first_name of this Student.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Student.


        :param first_name: The first_name of this Student.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Student.


        :return: The last_name of this Student.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Student.


        :param last_name: The last_name of this Student.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def grades(self) -> Dict[str, str]:
        """Gets the grades of this Student.


        :return: The grades of this Student.
        :rtype: Dict[str, str]
        """
        return self._grades

    @grades.setter
    def grades(self, grades: Dict[str, str]):
        """Sets the grades of this Student.


        :param grades: The grades of this Student.
        :type grades: Dict[str, str]
        """

        self._grades = grades

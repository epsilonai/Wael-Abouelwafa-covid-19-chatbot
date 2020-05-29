# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeviceState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, last_update: datetime=None, level: int=None):  # noqa: E501
        """DeviceState - a model defined in Swagger

        :param id: The id of this DeviceState.  # noqa: E501
        :type id: str
        :param name: The name of this DeviceState.  # noqa: E501
        :type name: str
        :param last_update: The last_update of this DeviceState.  # noqa: E501
        :type last_update: datetime
        :param level: The level of this DeviceState.  # noqa: E501
        :type level: int
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'last_update': datetime,
            'level': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'last_update': 'lastUpdate',
            'level': 'level'
        }
        self._id = id
        self._name = name
        self._last_update = last_update
        self._level = level

    @classmethod
    def from_dict(cls, dikt) -> 'DeviceState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeviceState of this DeviceState.  # noqa: E501
        :rtype: DeviceState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this DeviceState.


        :return: The id of this DeviceState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this DeviceState.


        :param id: The id of this DeviceState.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this DeviceState.


        :return: The name of this DeviceState.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DeviceState.


        :param name: The name of this DeviceState.
        :type name: str
        """

        self._name = name

    @property
    def last_update(self) -> datetime:
        """Gets the last_update of this DeviceState.


        :return: The last_update of this DeviceState.
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: datetime):
        """Sets the last_update of this DeviceState.


        :param last_update: The last_update of this DeviceState.
        :type last_update: datetime
        """

        self._last_update = last_update

    @property
    def level(self) -> int:
        """Gets the level of this DeviceState.


        :return: The level of this DeviceState.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level: int):
        """Sets the level of this DeviceState.


        :param level: The level of this DeviceState.
        :type level: int
        """

        self._level = level

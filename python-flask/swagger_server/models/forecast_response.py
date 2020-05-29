# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.city import City  # noqa: F401,E501
from swagger_server.models.forecast import Forecast  # noqa: F401,E501
from swagger_server import util


class ForecastResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, city: City=None, values: List[Forecast]=None):  # noqa: E501
        """ForecastResponse - a model defined in Swagger

        :param city: The city of this ForecastResponse.  # noqa: E501
        :type city: City
        :param values: The values of this ForecastResponse.  # noqa: E501
        :type values: List[Forecast]
        """
        self.swagger_types = {
            'city': City,
            'values': List[Forecast]
        }

        self.attribute_map = {
            'city': 'city',
            'values': 'values'
        }
        self._city = city
        self._values = values

    @classmethod
    def from_dict(cls, dikt) -> 'ForecastResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ForecastResponse of this ForecastResponse.  # noqa: E501
        :rtype: ForecastResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city(self) -> City:
        """Gets the city of this ForecastResponse.


        :return: The city of this ForecastResponse.
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city: City):
        """Sets the city of this ForecastResponse.


        :param city: The city of this ForecastResponse.
        :type city: City
        """

        self._city = city

    @property
    def values(self) -> List[Forecast]:
        """Gets the values of this ForecastResponse.


        :return: The values of this ForecastResponse.
        :rtype: List[Forecast]
        """
        return self._values

    @values.setter
    def values(self, values: List[Forecast]):
        """Sets the values of this ForecastResponse.


        :param values: The values of this ForecastResponse.
        :type values: List[Forecast]
        """

        self._values = values

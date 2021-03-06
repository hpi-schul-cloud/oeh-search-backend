# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Mainnav(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'icon': 'Icon',
        'main_menu_style': 'str'
    }

    attribute_map = {
        'icon': 'icon',
        'main_menu_style': 'mainMenuStyle'
    }

    def __init__(self, icon=None, main_menu_style=None):  # noqa: E501
        """Mainnav - a model defined in Swagger"""  # noqa: E501
        self._icon = None
        self._main_menu_style = None
        self.discriminator = None
        if icon is not None:
            self.icon = icon
        if main_menu_style is not None:
            self.main_menu_style = main_menu_style

    @property
    def icon(self):
        """Gets the icon of this Mainnav.  # noqa: E501


        :return: The icon of this Mainnav.  # noqa: E501
        :rtype: Icon
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Mainnav.


        :param icon: The icon of this Mainnav.  # noqa: E501
        :type: Icon
        """

        self._icon = icon

    @property
    def main_menu_style(self):
        """Gets the main_menu_style of this Mainnav.  # noqa: E501


        :return: The main_menu_style of this Mainnav.  # noqa: E501
        :rtype: str
        """
        return self._main_menu_style

    @main_menu_style.setter
    def main_menu_style(self, main_menu_style):
        """Sets the main_menu_style of this Mainnav.


        :param main_menu_style: The main_menu_style of this Mainnav.  # noqa: E501
        :type: str
        """

        self._main_menu_style = main_menu_style

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Mainnav, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Mainnav):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

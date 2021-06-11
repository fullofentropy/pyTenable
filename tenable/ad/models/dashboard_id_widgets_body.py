# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad

    OpenAPI spec version: production
    

"""

import pprint

import six


class DashboardIdWidgetsBody(object):
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
        'pos_x': 'float',
        'pos_y': 'float',
        'width': 'float',
        'height': 'float',
        'title': 'str'
    }

    attribute_map = {
        'pos_x': 'posX',
        'pos_y': 'posY',
        'width': 'width',
        'height': 'height',
        'title': 'title'
    }

    def __init__(self, pos_x=None, pos_y=None, width=None, height=None, title=None):
        """DashboardIdWidgetsBody - a model defined in Swagger"""
        self._pos_x = None
        self._pos_y = None
        self._width = None
        self._height = None
        self._title = None
        self.discriminator = None
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.title = title

    @property
    def pos_x(self):
        """Gets the pos_x of this DashboardIdWidgetsBody.


        :return: The pos_x of this DashboardIdWidgetsBody.
        :rtype: float
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        """Sets the pos_x of this DashboardIdWidgetsBody.


        :param pos_x: The pos_x of this DashboardIdWidgetsBody.
        :type: float
        """
        if pos_x is None:
            raise ValueError("Invalid value for `pos_x`, must not be `None`")

        self._pos_x = pos_x

    @property
    def pos_y(self):
        """Gets the pos_y of this DashboardIdWidgetsBody.


        :return: The pos_y of this DashboardIdWidgetsBody.
        :rtype: float
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        """Sets the pos_y of this DashboardIdWidgetsBody.


        :param pos_y: The pos_y of this DashboardIdWidgetsBody.
        :type: float
        """
        if pos_y is None:
            raise ValueError("Invalid value for `pos_y`, must not be `None`")

        self._pos_y = pos_y

    @property
    def width(self):
        """Gets the width of this DashboardIdWidgetsBody.


        :return: The width of this DashboardIdWidgetsBody.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DashboardIdWidgetsBody.


        :param width: The width of this DashboardIdWidgetsBody.
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")

        self._width = width

    @property
    def height(self):
        """Gets the height of this DashboardIdWidgetsBody.


        :return: The height of this DashboardIdWidgetsBody.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DashboardIdWidgetsBody.


        :param height: The height of this DashboardIdWidgetsBody.
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def title(self):
        """Gets the title of this DashboardIdWidgetsBody.


        :return: The title of this DashboardIdWidgetsBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DashboardIdWidgetsBody.


        :param title: The title of this DashboardIdWidgetsBody.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

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
        if issubclass(DashboardIdWidgetsBody, dict):
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
        if not isinstance(other, DashboardIdWidgetsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

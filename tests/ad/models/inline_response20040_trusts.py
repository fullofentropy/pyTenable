# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint

import six


class InlineResponse20040Trusts(object):
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
        '_from': 'str',
        'to': 'str',
        'hazard_level': 'str',
        'attributes': 'list[str]'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'hazard_level': 'hazardLevel',
        'attributes': 'attributes'
    }

    def __init__(self, _from=None, to=None, hazard_level=None, attributes=None):
        """InlineResponse20040Trusts - a model defined in Swagger"""
        self.__from = None
        self._to = None
        self._hazard_level = None
        self._attributes = None
        self.discriminator = None
        self._from = _from
        self.to = to
        self.hazard_level = hazard_level
        self.attributes = attributes

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20040Trusts.   


        :return: The _from of this InlineResponse20040Trusts.   
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20040Trusts.


        :param _from: The _from of this InlineResponse20040Trusts.   
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this InlineResponse20040Trusts.   


        :return: The to of this InlineResponse20040Trusts.   
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this InlineResponse20040Trusts.


        :param to: The to of this InlineResponse20040Trusts.   
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

    @property
    def hazard_level(self):
        """Gets the hazard_level of this InlineResponse20040Trusts.   


        :return: The hazard_level of this InlineResponse20040Trusts.   
        :rtype: str
        """
        return self._hazard_level

    @hazard_level.setter
    def hazard_level(self, hazard_level):
        """Sets the hazard_level of this InlineResponse20040Trusts.


        :param hazard_level: The hazard_level of this InlineResponse20040Trusts.   
        :type: str
        """
        if hazard_level is None:
            raise ValueError("Invalid value for `hazard_level`, must not be `None`")
        allowed_values = ["regular", "dangerous", "unknown"]
        if hazard_level not in allowed_values:
            raise ValueError(
                "Invalid value for `hazard_level` ({0}), must be one of {1}"
                    .format(hazard_level, allowed_values)
            )

        self._hazard_level = hazard_level

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse20040Trusts.   


        :return: The attributes of this InlineResponse20040Trusts.   
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse20040Trusts.


        :param attributes: The attributes of this InlineResponse20040Trusts.   
        :type: list[str]
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")

        self._attributes = attributes

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
        if issubclass(InlineResponse20040Trusts, dict):
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
        if not isinstance(other, InlineResponse20040Trusts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

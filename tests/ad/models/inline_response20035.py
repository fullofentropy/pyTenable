# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint

import six


class InlineResponse20035(object):
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
        'id': 'float',
        'name': 'str',
        'permissions': 'list[ApirolesPermissions]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, name=None, permissions=None):
        """InlineResponse20035 - a model defined in Swagger"""
        self._id = None
        self._name = None
        self._permissions = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this InlineResponse20035.   


        :return: The id of this InlineResponse20035.   
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20035.


        :param id: The id of this InlineResponse20035.   
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20035.   


        :return: The name of this InlineResponse20035.   
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20035.


        :param name: The name of this InlineResponse20035.   
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this InlineResponse20035.   


        :return: The permissions of this InlineResponse20035.   
        :rtype: list[ApirolesPermissions]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this InlineResponse20035.


        :param permissions: The permissions of this InlineResponse20035.   
        :type: list[ApirolesPermissions]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions

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
        if issubclass(InlineResponse20035, dict):
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
        if not isinstance(other, InlineResponse20035):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

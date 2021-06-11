# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint

import six


class AlertsIdBody(object):
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
        'archived': 'bool',
        'read': 'bool'
    }

    attribute_map = {
        'archived': 'archived',
        'read': 'read'
    }

    def __init__(self, archived=None, read=None):
        """AlertsIdBody - a model defined in Swagger"""
        self._archived = None
        self._read = None
        self.discriminator = None
        if archived is not None:
            self.archived = archived
        if read is not None:
            self.read = read

    @property
    def archived(self):
        """Gets the archived of this AlertsIdBody.   


        :return: The archived of this AlertsIdBody.   
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this AlertsIdBody.


        :param archived: The archived of this AlertsIdBody.   
        :type: bool
        """

        self._archived = archived

    @property
    def read(self):
        """Gets the read of this AlertsIdBody.   


        :return: The read of this AlertsIdBody.   
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this AlertsIdBody.


        :param read: The read of this AlertsIdBody.   
        :type: bool
        """

        self._read = read

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
        if issubclass(AlertsIdBody, dict):
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
        if not isinstance(other, AlertsIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

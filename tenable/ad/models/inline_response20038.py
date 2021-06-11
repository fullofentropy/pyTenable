# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    
 
"""

import pprint

import six


class InlineResponse20038(object):
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
        'directory_id': 'float',
        'score': 'float'
    }

    attribute_map = {
        'directory_id': 'directoryId',
        'score': 'score'
    }

    def __init__(self, directory_id=None, score=None):
        """InlineResponse20038 - a model defined in Swagger"""
        self._directory_id = None
        self._score = None
        self.discriminator = None
        self.directory_id = directory_id
        self.score = score

    @property
    def directory_id(self):
        """Gets the directory_id of this InlineResponse20038.   


        :return: The directory_id of this InlineResponse20038.   
        :rtype: float
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this InlineResponse20038.


        :param directory_id: The directory_id of this InlineResponse20038.   
        :type: float
        """
        if directory_id is None:
            raise ValueError("Invalid value for `directory_id`, must not be `None`")

        self._directory_id = directory_id

    @property
    def score(self):
        """Gets the score of this InlineResponse20038.   


        :return: The score of this InlineResponse20038.   
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this InlineResponse20038.


        :param score: The score of this InlineResponse20038.   
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")

        self._score = score

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
        if issubclass(InlineResponse20038, dict):
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
        if not isinstance(other, InlineResponse20038):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

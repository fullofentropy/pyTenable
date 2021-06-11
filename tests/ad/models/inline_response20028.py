# coding: utf-8

"""
    Tenable.ad - Client API

    API to interact with Tenable.ad   

    OpenAPI spec version: production
    

"""

import pprint

import six


class InlineResponse20028(object):
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
        'enabled': 'bool',
        'url': 'str',
        'search_user_dn': 'str',
        'search_user_password': 'str',
        'user_search_base': 'str',
        'user_search_filter': 'str',
        'allowed_groups': 'list[InlineResponse20028AllowedGroups]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'url': 'url',
        'search_user_dn': 'searchUserDN',
        'search_user_password': 'searchUserPassword',
        'user_search_base': 'userSearchBase',
        'user_search_filter': 'userSearchFilter',
        'allowed_groups': 'allowedGroups'
    }

    def __init__(self, enabled=False, url=None, search_user_dn=None, search_user_password=None, user_search_base=None,
                 user_search_filter=None, allowed_groups=None):
        """InlineResponse20028 - a model defined in Swagger"""
        self._enabled = None
        self._url = None
        self._search_user_dn = None
        self._search_user_password = None
        self._user_search_base = None
        self._user_search_filter = None
        self._allowed_groups = None
        self.discriminator = None
        self.enabled = enabled
        self.url = url
        self.search_user_dn = search_user_dn
        self.search_user_password = search_user_password
        self.user_search_base = user_search_base
        self.user_search_filter = user_search_filter
        self.allowed_groups = allowed_groups

    @property
    def enabled(self):
        """Gets the enabled of this InlineResponse20028.   


        :return: The enabled of this InlineResponse20028.   
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InlineResponse20028.


        :param enabled: The enabled of this InlineResponse20028.   
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def url(self):
        """Gets the url of this InlineResponse20028.   


        :return: The url of this InlineResponse20028.   
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20028.


        :param url: The url of this InlineResponse20028.   
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def search_user_dn(self):
        """Gets the search_user_dn of this InlineResponse20028.   


        :return: The search_user_dn of this InlineResponse20028.   
        :rtype: str
        """
        return self._search_user_dn

    @search_user_dn.setter
    def search_user_dn(self, search_user_dn):
        """Sets the search_user_dn of this InlineResponse20028.


        :param search_user_dn: The search_user_dn of this InlineResponse20028.   
        :type: str
        """
        if search_user_dn is None:
            raise ValueError("Invalid value for `search_user_dn`, must not be `None`")

        self._search_user_dn = search_user_dn

    @property
    def search_user_password(self):
        """Gets the search_user_password of this InlineResponse20028.   


        :return: The search_user_password of this InlineResponse20028.   
        :rtype: str
        """
        return self._search_user_password

    @search_user_password.setter
    def search_user_password(self, search_user_password):
        """Sets the search_user_password of this InlineResponse20028.


        :param search_user_password: The search_user_password of this InlineResponse20028.   
        :type: str
        """
        if search_user_password is None:
            raise ValueError("Invalid value for `search_user_password`, must not be `None`")

        self._search_user_password = search_user_password

    @property
    def user_search_base(self):
        """Gets the user_search_base of this InlineResponse20028.   


        :return: The user_search_base of this InlineResponse20028.   
        :rtype: str
        """
        return self._user_search_base

    @user_search_base.setter
    def user_search_base(self, user_search_base):
        """Sets the user_search_base of this InlineResponse20028.


        :param user_search_base: The user_search_base of this InlineResponse20028.   
        :type: str
        """
        if user_search_base is None:
            raise ValueError("Invalid value for `user_search_base`, must not be `None`")

        self._user_search_base = user_search_base

    @property
    def user_search_filter(self):
        """Gets the user_search_filter of this InlineResponse20028.   


        :return: The user_search_filter of this InlineResponse20028.   
        :rtype: str
        """
        return self._user_search_filter

    @user_search_filter.setter
    def user_search_filter(self, user_search_filter):
        """Sets the user_search_filter of this InlineResponse20028.


        :param user_search_filter: The user_search_filter of this InlineResponse20028.   
        :type: str
        """
        if user_search_filter is None:
            raise ValueError("Invalid value for `user_search_filter`, must not be `None`")

        self._user_search_filter = user_search_filter

    @property
    def allowed_groups(self):
        """Gets the allowed_groups of this InlineResponse20028.   


        :return: The allowed_groups of this InlineResponse20028.   
        :rtype: list[InlineResponse20028AllowedGroups]
        """
        return self._allowed_groups

    @allowed_groups.setter
    def allowed_groups(self, allowed_groups):
        """Sets the allowed_groups of this InlineResponse20028.


        :param allowed_groups: The allowed_groups of this InlineResponse20028.   
        :type: list[InlineResponse20028AllowedGroups]
        """
        if allowed_groups is None:
            raise ValueError("Invalid value for `allowed_groups`, must not be `None`")

        self._allowed_groups = allowed_groups

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
        if issubclass(InlineResponse20028, dict):
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
        if not isinstance(other, InlineResponse20028):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

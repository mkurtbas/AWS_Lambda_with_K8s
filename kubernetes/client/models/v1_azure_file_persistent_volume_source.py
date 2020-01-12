# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1AzureFilePersistentVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'read_only': 'bool',
        'secret_name': 'str',
        'secret_namespace': 'str',
        'share_name': 'str'
    }

    attribute_map = {
        'read_only': 'readOnly',
        'secret_name': 'secretName',
        'secret_namespace': 'secretNamespace',
        'share_name': 'shareName'
    }

    def __init__(self, read_only=None, secret_name=None, secret_namespace=None, share_name=None):
        """
        V1AzureFilePersistentVolumeSource - a model defined in Swagger
        """

        self._read_only = None
        self._secret_name = None
        self._secret_namespace = None
        self._share_name = None
        self.discriminator = None

        if read_only is not None:
          self.read_only = read_only
        self.secret_name = secret_name
        if secret_namespace is not None:
          self.secret_namespace = secret_namespace
        self.share_name = share_name

    @property
    def read_only(self):
        """
        Gets the read_only of this V1AzureFilePersistentVolumeSource.
        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :return: The read_only of this V1AzureFilePersistentVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1AzureFilePersistentVolumeSource.
        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :param read_only: The read_only of this V1AzureFilePersistentVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_name(self):
        """
        Gets the secret_name of this V1AzureFilePersistentVolumeSource.
        the name of secret that contains Azure Storage Account Name and Key

        :return: The secret_name of this V1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """
        Sets the secret_name of this V1AzureFilePersistentVolumeSource.
        the name of secret that contains Azure Storage Account Name and Key

        :param secret_name: The secret_name of this V1AzureFilePersistentVolumeSource.
        :type: str
        """
        if secret_name is None:
            raise ValueError("Invalid value for `secret_name`, must not be `None`")

        self._secret_name = secret_name

    @property
    def secret_namespace(self):
        """
        Gets the secret_namespace of this V1AzureFilePersistentVolumeSource.
        the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod

        :return: The secret_namespace of this V1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._secret_namespace

    @secret_namespace.setter
    def secret_namespace(self, secret_namespace):
        """
        Sets the secret_namespace of this V1AzureFilePersistentVolumeSource.
        the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod

        :param secret_namespace: The secret_namespace of this V1AzureFilePersistentVolumeSource.
        :type: str
        """

        self._secret_namespace = secret_namespace

    @property
    def share_name(self):
        """
        Gets the share_name of this V1AzureFilePersistentVolumeSource.
        Share Name

        :return: The share_name of this V1AzureFilePersistentVolumeSource.
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """
        Sets the share_name of this V1AzureFilePersistentVolumeSource.
        Share Name

        :param share_name: The share_name of this V1AzureFilePersistentVolumeSource.
        :type: str
        """
        if share_name is None:
            raise ValueError("Invalid value for `share_name`, must not be `None`")

        self._share_name = share_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1AzureFilePersistentVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
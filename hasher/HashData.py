# core Class for hashing customer data
from hashlib import sha256
from collections import Iterable
import re

class HashData():
    """Creates SHA256 sums for iterable prepared for AdWords Customer Match"""


    def __init__(self, data):
        if not isinstance(data, Iterable) or isinstance(data, str):
            raise TypeError('data must be iterable and not a string, {} provided'.format(type(data)))

        self.data = data

    @staticmethod
    def clean(value):
        """
        Prepares string for AdWords' Customer Match requirements:
        - no trailing spaces
        - lowercase
        :param value: str
        :return: str
        """
        if isinstance(value, str):
            return value.strip().lower()
        else:
            return value

    def validate_email(self):
        """Validate if self.data is properly formatted email and raise ValueError if not"""

        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        for mail in self.data:
            mail = HashData.clean(mail)

            if not pattern.match(mail):
                raise ValueError("'{}' doesn't seem to be a valid email!".format(mail))


    def encrypt(self):
        """Creates generator for hashing self.data with SHA256 algorithm"""

        for row in self.data:
            value = HashData.clean(row)
            value = value.encode('UTF8') # hashlib requires encoding before hashing

            yield sha256(value).hexdigest()

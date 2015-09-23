import abc
import logging

from smqtk.utils import Configurable


__author__ = 'purg'


class SmqtkAlgorithm (Configurable):
    """
    Parent class for all algorithm interfaces.
    """

    @classmethod
    def logger(cls):
        """
        :return: logging object for this class
        :rtype: logging.Logger
        """
        return logging.getLogger('.'.join((cls.__module__, cls.__name__)))

    @property
    def name(self):
        """
        :return: The name of this class type.
        :rtype: str
        """
        return self.__class__.__name__

    @property
    def _log(self):
        """
        :return: logging object for this class as a property
        :rtype: logging.Logger
        """
        return self.logger()

    # noinspection PyMethodParameters
    @abc.abstractmethod
    def is_usable(cls):
        """
        Check whether this descriptor is available for use.

        Since certain ContentDescriptor implementations may require additional
        dependencies that may not yet be available on the system, this method
        should check for those dependencies and return a boolean saying if the
        implementation is usable.

        NOTES:
            - This should be a class method
            - When not available, this should emit a warning message pointing to
                documentation on how to get/install required dependencies.

        :return: Boolean determination of whether this implementation is usable.
        :rtype: bool

        """

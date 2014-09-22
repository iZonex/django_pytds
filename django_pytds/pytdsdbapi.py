"""

Uses pytds

"""
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db.utils import (IntegrityError as DjangoIntegrityError,
    DatabaseError as DjangoDatabaseError)

from django.utils import six
from django.utils import timezone
import pytds

# DB API default values
apilevel = '2.0'

# 1: Threads may share the module, but not connections.
threadsafety = 1


class Error(Exception if six.PY3 else StandardError):
    pass


class Warning(Exception if six.PY3 else StandardError):
    pass


class InterfaceError(Error):
    pass


class DatabaseError(DjangoDatabaseError, Error):
    pass


class InternalError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class IntegrityError(DatabaseError, DjangoIntegrityError):
    pass


class DataError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


class FetchFailedError(Error):
    pass


class _DbType(object):
    def __init__(self, valuesTuple):
        self.values = valuesTuple

    def __eq__(self, other):
        return other in self.values

    def __ne__(self, other):
        return other not in self.values

def connect(server, database, port, user, password, timeout=30, use_transactions=None, use_mars=False, readonly=False):
    """Connect to a database.

    timeout -- A command timeout value, in seconds (default 30 seconds)
    """
    autocommit = not use_transactions
    c = pytds.connect(server=server,
                      database=database,
                      port=port,
                      user=user,
                      password=password,
                      timeout=timeout,
                      autocommit=autocommit, use_mars=use_mars, readonly=readonly)
    return c


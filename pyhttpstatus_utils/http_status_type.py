#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils
"""
HTTP Status Types
"""
import enum

class HttpStatusType(enum.Enum):
    """HTTP Status Name to Types
    """

    INFORMATIONAL = 'Informational'
    SUCCESSFUL = 'Successful'
    REDIRECTION = 'Redirection'
    CLIENT_ERROR = 'Client Error'
    SERVER_ERROR = 'Server Error'


class HttpStatusCodeType(enum.IntEnum):
    """HTTP Status Code to Types
    """

    INFORMATIONAL = 100
    SUCCESSFUL = 200
    REDIRECTION = 300
    CLIENT_ERROR = 400
    SERVER_ERROR = 500

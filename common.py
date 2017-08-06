#!/usr/bin/env python3

from collections import namedtuple
import json
# message namedtuple
# two functions: into_message and serialized_message
# declare message named tuple
DmailRequest = namedtuple('DmailRequest', ['whoami', 'parameter', 'data'])


def into_message():
    return


def into_raw():
    return


def to_json(request):
    """Takes DmailRequest and turns it into a json object (dict)"""
    return {
        'whoami': request.whoami,
        'parameter': request.parameter,
        'data': request.data,
    }


def from_json(json_obj):
    """Takes json object and turns it into a DmailRequest object"""
    return DmailRequest(
        json_obj['whoami'],
        json_obj['parameter'],
        json_obj['data'],
    )

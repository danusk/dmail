#!/usr/bin/env python3

from collections import namedtuple
import json


DmailRequest = namedtuple('DmailRequest', ['whoami', 'parameter', 'data'])


def from_raw_bytes(raw_bytes):
    """Take raw bytes and turn it into a DmailRequest"""
    return from_json(json.loads(raw_bytes.decode(encoding='UTF-8')))


def into_raw_bytes(dmail_request):
    """Turn a DmailRequest into a raw bytes string"""
    return bytes(json.dumps(to_json(dmail_request)) + "\n", "utf-8")


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

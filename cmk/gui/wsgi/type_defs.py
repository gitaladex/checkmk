#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
from typing import Iterable, List, Literal, TypedDict, Union

from cmk.utils.type_defs import UserId

from cmk.gui.type_defs import AuthType

Scope = List[str]
UnixTimeStamp = int  # restrict to positive numbers
Audience = Union[str, List[str]]
TokenType = Literal["access_token", "refresh_token"]
RFC7662 = TypedDict(
    "RFC7662",
    {
        "active": bool,
        "scope": AuthType,
        "client_id": str,
        "username": str,
        "token_type": TokenType,
        "exp": UnixTimeStamp,  # expires
        "iat": UnixTimeStamp,  # issued
        "nbf": UnixTimeStamp,  # not before
        "sub": UserId,  # subject
        "aud": Audience,
        "iss": str,  # issuer
        "jti": str,  # json web token-identifier
    },
    total=False,
)
HostGroup = TypedDict(
    "HostGroup",
    {
        "alias": str,
    },
)

WSGIResponse = Iterable[bytes]

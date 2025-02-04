from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, Sequence

from starlite.datastructures.cookie import Cookie
from starlite.datastructures.response_header import ResponseHeader

if TYPE_CHECKING:
    from starlite.types.composite_types import ResponseCookies, ResponseHeaders


def narrow_response_headers(headers: ResponseHeaders | None) -> Sequence[ResponseHeader] | None:
    """Given :class:`.types.ResponseHeaders` as a :class:`typing.Mapping`, create a list of
    :class:`.datastructures.response_header.ResponseHeader` from it, otherwise return ``headers`` unchanged
    """
    return (
        [ResponseHeader(name=name, value=value) for name, value in headers.items()]
        if isinstance(headers, Mapping)
        else headers
    )


def narrow_response_cookies(cookies: ResponseCookies | None) -> Sequence[Cookie] | None:
    """Given :class:`.types.ResponseCookies` as a :class:`typing.Mapping`, create a list of
    :class:`.datastructures.cookie.Cookie` from it, otherwise return ``cookies`` unchanged
    """
    return [Cookie(key=key, value=value) for key, value in cookies.items()] if isinstance(cookies, Mapping) else cookies

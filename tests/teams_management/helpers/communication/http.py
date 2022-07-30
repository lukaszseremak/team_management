from enum import Enum


class Error:
    class Code(Enum):
        UNSUPPORTED = -1
        OBJECT_NOT_FOUND = 0
        BAD_REQUEST = 1
        UNAUTHORIZED = 2

    def __init__(self, status_code, data):
        self._status_code = status_code
        self._data = data

    @property
    def code(self):
        mapping = {
            404: Error.Code.OBJECT_NOT_FOUND,
            400: Error.Code.BAD_REQUEST,
            422: Error.Code.BAD_REQUEST,
            401: Error.Code.UNAUTHORIZED,
        }
        return mapping.get(self._status_code, Error.Code.UNSUPPORTED)

    @property
    def details(self):
        return self._data["detail"]


class Response:
    def __init__(self, response):
        self._response = response

    @property
    def is_successful(self):
        return self._response.status_code >= 200 and self._response.status_code <= 206

    @property
    def error(self):
        assert not self.is_successful
        return Error(self._response.status_code, self._response.json())

    def json(self):
        return self._response.json()

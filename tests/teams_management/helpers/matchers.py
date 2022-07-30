from datetime import datetime


class UuidMatcher:
    def __eq__(self, other):
        return other is not None and isinstance(other, str)


class DatetmeMatcher:
    def __eq__(self, other):
        return isinstance(other, str) and datetime.strptime(other, "%Y-%m-%dT%H:%M:%S.%f%z")


class NumberMatcher:
    def __eq__(self, other):
        return isinstance(other, (int, float, complex)) and not isinstance(other, bool)


class DictMatcher:
    def __eq__(self, other):
        return other is not None and isinstance(other, dict)

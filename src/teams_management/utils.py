import uuid


def make_uuid():
    """Generate a random UUID number."""
    return uuid.uuid4()


def make_str_uuid():
    """Same as :func:`make_uuid`, but returns generated UUID as string."""
    return str(make_uuid())

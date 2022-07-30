from uuid import UUID

from .http import Response


class BaseAPI:
    def __init__(self, client):
        self._client = client

    def post(self, *args, **kwargs):
        return self._client.post(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._client.delete(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self._client.put(*args, **kwargs)


class TeamsAPI(BaseAPI):
    def add_one(self, name):
        data = {"name": name}
        resp = self.post("/teams", json=data)
        return Response(resp)

    def delete_one(self, uid: UUID):
        resp = self.delete(f"/teams/{uid}")
        return Response(resp)

    def fetch_all(self):
        resp = self._client.get("/teams")
        return Response(resp)

    def edit_one(self, uid: UUID, name: str):
        data = {"name": name}
        resp = self.put(f"/teams/{uid}", json=data)
        return Response(resp)


class APIClient:
    def __init__(self, client):
        self._client = client

    @property
    def teams(self):
        return TeamsAPI(self._client)

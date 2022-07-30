from pytest import fixture

from src.teams_management.utils import make_uuid

from .helpers.communication.http import Error
from .helpers.matchers import UuidMatcher


@fixture
def single_team(client):
    resp = client.teams.add_one(name="A")
    return resp.json()


@fixture
def many_teams(client):
    teams = []
    for i in range(3):
        resp = client.teams.add_one(name=f"Team {i+1}")
        teams.append(resp.json())
    return teams


class TestTeamsApi:
    def test_create_single_team(self, client):
        response = client.teams.add_one(name="Team 1")

        assert response.is_successful
        assert response.json() == {"uid": UuidMatcher(), "name": "Team 1"}

    def test_delete_not_existing_team(self, client):
        uid = make_uuid()
        response = client.teams.delete_one(uid=uid)

        assert response.error.code == Error.Code.OBJECT_NOT_FOUND
        assert response.error.details == f"Record {uid} not found"

    def test_delete_when_the_team_exist(self, client, single_team):
        response = client.teams.delete_one(uid=single_team["uid"])

        assert response.is_successful
        assert response.json() == {"success": True}

    def test_fetch_all_when_there_arent_any_team_in_the_db(self, client):
        response = client.teams.fetch_all()

        assert response.is_successful
        assert response.json() == []

    def test_fetch_all(self, client, many_teams):
        response = client.teams.fetch_all()

        assert response.is_successful
        assert response.json() == [
            {"uid": UuidMatcher(), "name": "Team 1"},
            {"uid": UuidMatcher(), "name": "Team 2"},
            {"uid": UuidMatcher(), "name": "Team 3"},
        ]

    def test_edit_when_request_is_successful(self, client, single_team):
        response = client.teams.edit_one(uid=single_team["uid"], name="XYZ 2")

        assert response.is_successful
        assert response.json() == {"uid": single_team["uid"], "name": "XYZ 2"}

    def test_edit_when_team_is_not_found(self, client):
        uid = make_uuid()
        response = client.teams.edit_one(uid=uid, name="XYZ 3")
        assert response.error.code == Error.Code.OBJECT_NOT_FOUND
        assert response.error.details == f"Record {uid} not found"

    def test_edit_when_provided_data_is_the_same_as_in_db(self, client, single_team):
        response = client.teams.edit_one(uid=single_team["uid"], name=single_team["name"])
        assert response.is_successful
        assert response.json() == {"uid": single_team["uid"], "name": single_team["name"]}

    def test_edit_changes_in_collection(self, client, many_teams):
        response = client.teams.fetch_all()

        assert response.is_successful
        teams = response.json()
        assert teams == [
            {"uid": UuidMatcher(), "name": "Team 1"},
            {"uid": UuidMatcher(), "name": "Team 2"},
            {"uid": UuidMatcher(), "name": "Team 3"},
        ]

        response = client.teams.edit_one(uid=teams[0]["uid"], name="Team 1 changed")

        assert response.is_successful

        response = client.teams.fetch_all()

        assert response.is_successful
        assert response.json() == [
            {"uid": UuidMatcher(), "name": "Team 1 changed"},
            {"uid": UuidMatcher(), "name": "Team 2"},
            {"uid": UuidMatcher(), "name": "Team 3"},
        ]

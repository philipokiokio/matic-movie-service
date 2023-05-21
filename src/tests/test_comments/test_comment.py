import pytest
from src.tests.conftest import TestClient, client, comments, bulk_comments, custom_film
from src.tests.test_films.test_film import FILM_ROUTE


COMMENT_ROUTE = "/api/v1/comment"


create_film = {"title": "Hilda Cooks", "release_date": "2023-05-21"}


def test_create_comment(client, custom_film):
    client: TestClient = client

    res = client.post(f"{COMMENT_ROUTE}/film/7/create/", json=comments[0])

    assert res.status_code == 201
    assert res.json().get("message") == "comment created successfully"
    assert res.json().get("data")["text"] == comments[0]["text"]


# FILM DOES NOT EXIST EXCEPTION CHECK


def test_fail_film_commments_film_does_exist(client):
    client: TestClient = client

    res = client.get(f"{COMMENT_ROUTE}s/film/7/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no film with this id"


# COMMENT EXIST


def test_comments(client, bulk_comments):
    client: TestClient = client

    res = client.get(f"{COMMENT_ROUTE}s/film/7/")

    assert res.status_code == 200
    assert res.json().get("message") == "comments retrieved successfully"
    assert len(res.json().get("data")) == 3


def test_get_film_count(client, bulk_comments):
    client: TestClient = client
    res = client.get(f"{FILM_ROUTE}/7/")

    assert res.status_code == 200
    assert res.json().get("message") == "film retrieved successfully"
    assert res.json().get("data")["title"] == create_film["title"]
    assert res.json().get("data")["comment_count"] == 3


def test_comment(client, bulk_comments):
    client: TestClient = client

    res = client.get(f"{COMMENT_ROUTE}/1/film/7/")

    assert res.status_code == 200
    assert res.json().get("message") == "comment retrieved successfully"


def test_comment_update(client, bulk_comments):
    client: TestClient = client

    res = client.patch(
        f"{COMMENT_ROUTE}/1/film/7/update/", json={"text": "views from the 6"}
    )

    assert res.status_code == 200
    assert res.json().get("data")["text"] == "views from the 6"
    assert res.json().get("message") == "comment updated successfully"


def test_comments_delete(client, bulk_comments):
    client: TestClient = client

    res = client.delete(f"{COMMENT_ROUTE}/1/film/7/delete/")

    assert res.status_code == 204


# COMMENTS DOES NOT EXIST
def test_comments_does_not_exist(client, custom_film):
    client: TestClient = client

    res = client.get(f"{COMMENT_ROUTE}s/film/7/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there are no comments for this film"


def test_comment_does_not_exist(client, custom_film):
    client: TestClient = client

    res = client.get(f"{COMMENT_ROUTE}/1/film/7/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no comment for this film with this id"


def test_comment_update_does_not_exist(client, custom_film):
    client: TestClient = client

    res = client.patch(
        f"{COMMENT_ROUTE}/1/film/7/update/", json={"text": "views from the 6"}
    )

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no comment for this film with this id"


def test_comments_delete_does_not_exist(client, custom_film):
    client: TestClient = client

    res = client.delete(f"{COMMENT_ROUTE}/1/film/7/delete/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no comment for this film with this id"

import pytest
from src.tests.conftest import TestClient, client, create_film, custom_film


def test_root(client):
    client: TestClient = client
    res = client.get("/")

    assert res.status_code == 200
    assert res.json().get("message") == "Codematic Movie-API take home"


FILM_ROUTE = "/api/v1/film"


def test_create_film(client):
    client: TestClient = client

    res = client.post(f"{FILM_ROUTE}/create/", json=create_film)
    assert res.status_code == 201
    assert res.json().get("message") == "film created successfully"
    assert res.json().get("data")["title"] == create_film["title"]


# EXCEPTION CASES
def test_no_films(client):
    client: TestClient = client
    res = client.get(f"{FILM_ROUTE}s/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there are no films in the service"


def test_no_film(client):
    client: TestClient = client
    res = client.get(f"{FILM_ROUTE}/1/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no film with this id"


def test_failed_update_film(client):
    client: TestClient = client
    res = client.patch(
        f"{FILM_ROUTE}/1/update/", json={"title": "what time to be alive"}
    )

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no film with this id"


def test_failed_delete_film(client):
    client: TestClient = client
    res = client.delete(f"{FILM_ROUTE}/1/delete/")

    assert res.status_code == 404
    assert res.json().get("detail") == "there is no film with this id"


# APPOPRIATE CASES
def test_get_films(client, custom_film):
    client: TestClient = client
    res = client.get(f"{FILM_ROUTE}s/")

    assert res.status_code == 200
    assert res.json().get("message") == "films retrieved successfully"
    assert len(res.json().get("data")) == 7


def test_get_film(client, custom_film):
    client: TestClient = client
    res = client.get(f"{FILM_ROUTE}/7/")

    assert res.status_code == 200
    assert res.json().get("message") == "film retrieved successfully"
    assert res.json().get("data")["title"] == create_film["title"]


def test_update_film(client, custom_film):
    client: TestClient = client
    res = client.patch(f"{FILM_ROUTE}/7/update/", json={"title": "30 for 30"})

    assert res.status_code == 200
    assert res.json().get("message") == "film updated successfully"
    assert res.json().get("data")["title"] == "30 for 30"


def test_delete_film(client, custom_film):
    client: TestClient = client
    res = client.delete(f"{FILM_ROUTE}/7/delete/")

    assert res.status_code == 204

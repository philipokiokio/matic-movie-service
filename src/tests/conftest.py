import pytest
from fastapi.testclient import TestClient
from src.tests import star_wars_data
from src.app import main
from src.app.database import Base, POSTGRES_URI, sessionmaker, create_engine
from src.app.utils.database_utils import get_db
from src.films.film_repo import film_repo

# Test SQLAlchemy DBURL

test_URL = f"{POSTGRES_URI}_test"
print(test_URL)
test_engine = create_engine(test_URL)
TestFactory = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)


@pytest.fixture
def session():
    Base.metadata.drop_all(test_engine)
    Base.metadata.create_all(test_engine)

    db = TestFactory()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    # run our code beforewe  run our test
    def get_test_db():
        try:
            yield session
        finally:
            session.close()

    main.app.dependency_overrides[get_db] = get_test_db
    yield TestClient(main.app)


@pytest.fixture()
def pre_load_data_from_star_wars(client):
    client: TestClient = client
    film_repo(TestFactory()).bulk_create(star_wars_data)


create_film = {"title": "Hilda Cooks", "release_date": "2023-05-21"}


@pytest.fixture()
def custom_film(client, pre_load_data_from_star_wars):
    client: TestClient = client

    res = client.post("/api/v1/film/create/", json=create_film)
    assert res.status_code == 201
    assert res.json().get("message") == "film created successfully"
    assert res.json().get("data")["title"] == create_film["title"]
    return res.json().get("data")


comments = [
    {"text": "comment for the custom movie"},
    {"text": "I sabi sha"},
    {"text": "You self see"},
]


@pytest.fixture()
def bulk_comments(client, custom_film):
    client: TestClient = client

    for data in comments:
        res = client.post("/api/v1/comment/film/7/create/", json=data)
        assert res.status_code == 201

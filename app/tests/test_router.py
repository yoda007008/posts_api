import pytest
from fastapi.testclient import TestClient
from app.models.router import router  
from app.models.dao import PostsDAO  
from unittest.mock import AsyncMock

client = TestClient(router)

@pytest.fixture
def mock_posts_dao(monkeypatch):
    mock_dao = AsyncMock()
    monkeypatch.setattr(PostsDAO, "find_all", mock_dao.find_all)
    monkeypatch.setattr(PostsDAO, "find_by_id", mock_dao.find_by_id)
    monkeypatch.setattr(PostsDAO, "delete_post", mock_dao.delete_post)
    monkeypatch.setattr(PostsDAO, "delete_like_for_id", mock_dao.delete_like_for_id)
    monkeypatch.setattr(PostsDAO, "upgrade_post", mock_dao.upgrade_post)
    return mock_dao

def test_get_all_posts(mock_posts_dao):
    mock_posts_dao.find_all.return_value = [{"id": 1, "post": "First post"}]
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "post": "First post"}]

def test_get_one_post(mock_posts_dao):
    mock_posts_dao.find_by_id.return_value = {"id": 1, "post": "First post"}
    response = client.post("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "post": "First post"}

def test_delete_post(mock_posts_dao):
    mock_posts_dao.delete_post.return_value = True
    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Successful"}


def test_delete_like(mock_posts_dao):
    mock_posts_dao.delete_like_for_id.return_value = True
    response = client.delete("/posts/1/like")
    assert response.status_code == 200
    assert response.json() == {"message": "Like updated"}


def test_upgrade_post(mock_posts_dao):
    mock_posts_dao.upgrade_post.return_value = {"id": 1, "text": "Updated post"}
    response = client.put("/posts/1", json={"text": "Updated post"})
    assert response.status_code == 200
    assert response.json() == {"text": "Updated post"}
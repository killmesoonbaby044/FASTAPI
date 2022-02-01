from app import schemas
import pytest


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    def validate(post):
        return schemas.PostOut(**post)

    posts = map(validate, res.json())
    # posts_list = list(posts)
    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.owner_id == test_posts[0].owner_id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title


def test_unauthorized_get_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_non_exist_post(authorized_client, test_posts):
    res = authorized_client.get("/posts/8888888")
    assert res.status_code == 404


@pytest.mark.parametrize("title, content, published", [
    ("new_title", "new_content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_create_posts(authorized_client, test_user, title, content, published):
    res = authorized_client.post('/posts/', json={"title": title, "content": content, 'published': published})
    created_posts = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_posts.title == title
    assert created_posts.content == content
    assert created_posts.published == published
    assert created_posts.owner_id == test_user['id']


def test_create_post_default_published_true(authorized_client, test_user):
    res = authorized_client.post('/posts/', json={"title": "new_title", "content": "new_content"})
    created_posts = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_posts.title == 'new_title'
    assert created_posts.content == 'new_content'
    assert created_posts.published == True
    assert created_posts.owner_id == test_user['id']


def test_unauthorized_user_create_post(client):
    res = client.post(
        "/posts",
    )

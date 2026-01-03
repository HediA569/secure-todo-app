from app import app

def test_homepage():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_add_task():
    client = app.test_client()
    res = client.post("/", data={"title": "hello"})
    assert res.status_code == 302


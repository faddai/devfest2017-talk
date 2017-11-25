from flask import url_for


def test_can_visit_login_page(client):
    response = client.get(url_for('login'), follow_redirects=True)
    assert response.status_code == 200
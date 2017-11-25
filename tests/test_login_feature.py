from flask import url_for


def test_can_visit_login_page(client):
    response = client.get(url_for('login'), follow_redirects=True)
    assert response.status_code == 200

def test_can_login_into_application(client):
    response = client.get(url_for('login'), follow_redirects=True)
    assert response.status_code == 200
    
    data = dict(email='info@test.com', password='project')
    response = client.post(url_for('login'), follow_redirects=True, **data)
    assert response.status_code
    # assert response.find.message('') # look for the Welcome flash message


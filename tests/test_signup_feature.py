from flask import url_for


def test_can_visit_signup_page(client):
    response = client.get(url_for('signup'), follow_redirects=True)
    assert response.status_code == 200

def test_can_create_a_user_account(client):
    response = client.get(url_for('signup'), follow_redirects=True)
    assert response.status_code == 200
    
    data = dict(email='info@test.com', 
                password='project',
                firstname='John',
                lastname='Doe',
                username='john.doe')

    response = client.post(url_for('signup'), follow_redirects=True, **data)
    assert response.status_code
    # assert response.find.message('') # look for the Welcome flash message


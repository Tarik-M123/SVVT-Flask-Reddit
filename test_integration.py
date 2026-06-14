def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login_page_loads(client):
    response = client.get('/auth/login')
    assert response.status_code == 200

def test_register_page_loads(client):
    response = client.get('/auth/register')
    assert response.status_code == 200

def test_protected_page_redirects_when_not_logged_in(client):
    response = client.get('/community/new')
    assert response.status_code == 302

def test_user_registration(client):
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_user_login(client):
    response = client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_communities_page_loads(client):
    response = client.get('/communities')
    assert response.status_code == 200
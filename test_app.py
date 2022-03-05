def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data


def test_service_bad_http_method(client):
    resp = client.get('/service')
    assert resp.status_code == 404


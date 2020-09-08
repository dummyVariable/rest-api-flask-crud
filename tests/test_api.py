import requests


URL = 'http://localhost:5000/crud'

def test_for_empty_request():

    resp = requests.get('http://localhost:5000/')
    assert resp.status_code == 200
    assert resp.json() == {'app' : 'crud api'}

    resp = requests.get(URL)
    assert resp.status_code == 200
    assert resp.json() == {'message' : 'no items found'}


    resp = requests.get(url=URL+'/123')
    assert resp.json() == {'message' : 'item not found'}

def test_for_create():

    resp = requests.post(url=URL, data={'name' : 'Batman', 'league' : 'Justice League'})
    assert resp.status_code == 200
    assert resp.json() == {'message' : 'created'}

    resp = requests.post(url=URL, data={'name' : 'Hulk', 'league' : 'Avengers'})
    assert resp.status_code == 200
    assert resp.json() == {'message' : 'created'}

def test_for_read_all():
    
    resp = requests.get(url=URL)
    assert resp.status_code == 200
    assert len(resp.json()) == 2

def test_for_read():

    resp = requests.get(url=URL+'/1')
    assert resp.status_code == 200
    assert resp.json() == {'name' : 'Batman', 'league' : 'Justice League'}

def test_for_update():

    resp = requests.put(url=URL+'/1', data={'name' : 'Flash', 'league' : 'Justice League'})
    assert resp.status_code == 200
    assert resp.json() == {'message' : 'updated'}

    resp = requests.get(url=URL+'/1')
    assert resp.status_code == 200
    assert resp.json() == {'name' : 'Flash', 'league' : 'Justice League'}

def test_for_delete():

    resp = requests.delete(url=URL+'/2')
    assert resp.json() == {'message' : 'deleted'}
    
    resp = requests.get(url=URL+'/2')
    assert resp.json() == {'message' : 'item not found'}



from api.model import CrudModel as db

def test_for_emptyness():
    
    assert db.read(1) is None

def test_for_create_data():

    data1 = {'name' : 'Batman', 'league' : 'Justice League'}
    assert db.create(data1) == 'ok'

    data2 = {'name' : 'Spiderman', 'league' : 'Avengers'}
    assert db.create(data2) == 'ok'

def test_for_read_data():

    assert db.read(1) == {'name' : 'Batman', 'league' : 'Justice League'}
    assert db.read(2) == {'name' : 'Spiderman', 'league' : 'Avengers'}
    assert db.read(3) is None


def test_for_update_data():

    data1 = {'name' : 'Flash', 'league' : 'Justice League'}
    assert db.update(1, data1) == 'ok'
    assert db.read(1) == {'name' : 'Flash', 'league' : 'Justice League'}
    assert db.update(4, data1) is None


def test_for_delete_data():

    assert db.delete(2) == 'ok'
    assert db.read(2) is None
    assert db.delete(2) is None

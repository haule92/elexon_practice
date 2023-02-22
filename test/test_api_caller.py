from src.api_elexon_caller import ElexonCaller


def test_happy_fetch_response():

    ec = ElexonCaller(settlement_date='2023-02-20')
    r = ec.fetch_response('B1780', period=1)
    assert r.status_code == 200


def test_unhappy_fetch_response():

    ec = ElexonCaller(settlement_date='2023-02-20')
    r = ec.fetch_response('B1999', period=60)
    assert r.status_code != 200

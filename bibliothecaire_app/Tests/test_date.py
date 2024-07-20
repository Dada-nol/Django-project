from datetime import date


def test_date():
    today = date.today()
    next_week = date.today().replace(day=date.today().day + 7)
    assert today < next_week

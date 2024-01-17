from city_functions import city_belongs
def test_city_belongs():
    sentence0=city_belongs("santiago","chile")
    assert sentence0=="Santiago belongs to Chile."

def test_city_belongs_with_population():
    sentence1=city_belongs("santiago","chile","5000000")
    assert sentence1=="Santiago belongs to Chile. It's population is 5000000."
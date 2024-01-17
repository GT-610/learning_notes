from name_function import get_formatted_name
def test_first_last_name():
    formatted_name=get_formatted_name("janis","joplin")
    assert formatted_name=="Janis Joplin"

def test_first_middle_last_name():
    formatted_name=get_formatted_name("wolfgang","mozart","amadeus")
    assert formatted_name=="Wolfgang Amadeus Mozart"
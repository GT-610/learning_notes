def city_belongs(city,country,population=0):
    if population:
        sentence=f"{city.title()} belongs to {country.title()}. It's population is {population}."
    else:
        sentence=f"{city.title()} belongs to {country.title()}."
    return sentence
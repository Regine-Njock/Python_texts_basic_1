# city = 'berlin'
# population = '3645000'
# print(city.capitalize(), population, sep= ':')

####################
city = 'berlin'
population = '3645000'

def city_pop(city: str, population: int) -> str:
    x=f'{city.capitalize}:{population}'
    return x

#capitalise will make only the first letter uppercase
#print(city.capitalize(), population, sep= ':')
print(city_pop(x))


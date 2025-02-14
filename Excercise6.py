# this is Excercise for Dictionary part:
# Easy ---2025-02-13
river_country = {"huanghe": "china", "nile": "egypt", "mississippi": "United States"}
for river, country in river_country.items():
    print(f"{river.title()} runs in {country.title()}")
for river in river_country.keys():
    print(river)
for country in river_country.values():
    print(country)

# Původní slovník
countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

# 1) Vytvoření slovníku countries_name (klíče a hodnoty přehodíme)
countries_name = {}
for code, name in countries.items():
    countries_name[name] = code

# 2) Vytvoření slovníku countries_len (počet znaků názvů zemí)
countries_len = {}
for code, name in countries.items():
    countries_len[code] = len(name)

# Výsledky
print("countries_name:", countries_name)
print("countries_len:", countries_len)

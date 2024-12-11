import datetime

year = 2023  

# Procházení měsíců 1 až 12
for month in range(1, 13):
    # Vytvoření data pro první den v měsíci
    first_day = datetime.date(year, month, 1)
    # Vytištění formátovaného data
    print(first_day.strftime('%d/%m/%Y'))

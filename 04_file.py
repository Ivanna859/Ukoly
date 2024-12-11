value = input("Zadejte hodnotu, kterou chcete uložit do souboru: ")

with open("04_file.txt", mode="a", encoding="utf-8") as file:
    file.write(value + "\n")

print

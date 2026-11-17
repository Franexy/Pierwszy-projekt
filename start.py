imie = input("Jak masz na imię? ")
cel = input("Jaki jest Twój pierwszy wielki cel? ")
kieszonkowe = float(input("Ile złotych miesięcznie możesz odkładać? "))

za_5_lat = kieszonkowe * 12 * 5

print("-----------------------------------------")
print(f"Cześć {imie}! Twój cel to: {cel}.")
print(f"Odkładając {kieszonkowe} zł miesięcznie, za 5 lat będziesz mieć {za_5_lat} zł na swój pierwszy biznes!")

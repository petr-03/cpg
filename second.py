def cislo_na_text(c):
    j = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    d = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    t = {
        11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct",
        16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }

    if c < 0 or c > 100:
        return "Číslo mimo rozsah (0–100)"
    if c == 100:
        return "sto"
    if c < 10:
        return j[c]
    if 11 <= c <= 19:
        return t[c]
    if c % 10 == 0:
        return d[c // 10]
    return f"{d[c // 10]} {j[c % 10]}"


# 🔸 Hlavní část programu:
vstup = input("Zadej číslo: ")

try:
    cislo = int(vstup)
    print(cislo_na_text(cislo))
except ValueError:
    print("Prosím zadej platné celé číslo!")


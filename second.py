def cislo_text(c):
    c = int(c)  # převedeme vstup na celé číslo
    j = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    d = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát",
         "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    t = { 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"}
    
    if c == 100:
        return "sto"
    if c < 10:
        return j[c]
    if 11 <= c <= 19:
        return t[c]
    if c % 10 == 0:
        return d[c // 10]
    if 20 <= c < 100:
        return f"{d[c // 10]} {j[c % 10]}"
    return "" 


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

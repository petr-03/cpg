import math

def statistika(rezim, cisla):
    """
    rezim: "soucet" | "pocet" | "max" | "min" | "prumer"
    cisla: list[int] nebo list[float]

    Vrat:
      - "soucet": soucet vsech cisel v seznamu
      - "pocet": pocet prvku v seznamu
      - "max": nejvetsi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "min": nejmensi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "prumer": aritmeticky prumer (pokud je seznam prazdny, vrat None)

    Nepouzivej vestavene funkce sum(), max(), min().
    Pouzij cyklus a podminky.
    """
    if rezim == "soucet":
        soucet_ = 0
        for i in cisla:
            soucet_ += i
        return soucet_
    
    elif rezim == "pocet":
        pocet_ = 0
        for i in cisla:
            pocet_ +=1
        return pocet_

    elif rezim == "max":
        if not cisla:
            return None
        max_ = 0
        for i in cisla:
            if i > max_:
                max_ = i
        return max_
    
    elif rezim == "min":
        if not cisla:
            return None
        
        min_ = cisla[0]
        for i in cisla:
            if i < min_:
                min_ = i
        return min_
    
    elif rezim == "prumer":
        if not cisla:
            return None
        soucet_ = 0
        for i in cisla:
            soucet_ += i

        pocet_ = 0
        for i in cisla:
            pocet_ +=1
            
        prumer_ = soucet_ / pocet_
        return prumer_


def test_statistika():
    assert statistika("soucet", [1, 2, 3, 4]) == 10
    assert statistika("soucet", [-1, -2, -3]) == -6
    assert statistika("soucet", []) == 0
    assert statistika("pocet", [1, 2, 3]) == 3
    assert statistika("pocet", []) == 0
    assert statistika("max", [1, 9, 3]) == 9
    assert statistika("max", [-10, -2, -30]) == -2
    assert statistika("max", []) is None
    assert statistika("min", [1, 9, 3]) == 1
    assert statistika("min", [-10, -2, -30]) == -30
    assert statistika("min", []) is None
    assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
    assert math.isclose(statistika("prumer", [1, 2]), 1.5)
    assert statistika("prumer", []) is None
    assert statistika("neco", [1, 2, 3]) is None


if __name__ == "__main__":
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))    # 4.0

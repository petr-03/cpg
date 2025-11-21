import time
import math

def je_prvocislo(cislo):
 
    cislo = int(cislo)
    if cislo <= 1:
        return False
    i = 0
   
    for delitel in range(2, round(cislo**0.5)+1):
        time.sleep(0.001)
        if cislo % delitel == 0:
            
            return False
        i += 1
    
    return True

def vrat_prvocisla(maximum):
    
    maximum = int(maximum)
    results = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            results.append(i)
    return results

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    maximum = cislo
    print(je_prvocislo(cislo))
    print(vrat_prvocisla(maximum))
    

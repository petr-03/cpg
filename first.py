def sudy_nebo_lichy(X):
    if X % 2 == 0:
        číslo = "sudé"
    else:
        číslo = "liché"

    return f"Číslo {X} je {číslo}" 

print(sudy_nebo_lichy(5))
print(sudy_nebo_lichy(1000000))

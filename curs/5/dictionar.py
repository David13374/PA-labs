# dictionare - dict
# memoreaza perechi cheie: valoare
# exp cursul trecut: {cuvant: frecventa}
# d = {"unu":2, "doi":3} # cheie: valoare

# cheie -> cu hash, dupa cheie se cauta eficient
# valoarea -> poate fi de orice tip (este informatia aasociata cheii)
# print(d["unu"])

# comprehension
# d = {s:0 for s in "aeiou"}
# print(d)

# accesarea unui element
# d[cheie] -> valoarea asociata cheii sau KeyError daca nu exista cheie in dictionar
# d.get(cheie, val_default) -> returneaza tot valoarea asociata chiei, dar daca nu exista cheia returneaza val_default
# modificare, inserare:
# d[cheie] = valoare -> daca nu exista cheie, se insereaza, daca nu exista, se modifica valoarea asociata
# d = dict()
# d["unu"] = 7 # modifica
# d["trei"] = 2 # inserare
# print(d)

# stergere
# d = {"lista 1": [4, 5, 6]}
# print(d["lista 1"])

# stergere
# del d[cheie] -> sterge (eroare daca nu exista)
# d.pop(cheie, val_default) -> returneaza si valorea asociata acheii sterse
# sau valoare val_default daca nu exista in dictionar cheia

# operatorul in -> cautare in chei
# if "unu" in d:
#     del d["unu"]
# print(d)

"""
d.keys() -> multimea cheilor
d.values() -> lista valorilor
d.items() -> perechi cheie, valoare
"""

# d = {"unu": 2, "doi": 3, "trei": 0}
# print(d.keys())
# print(d.values())
# print(d.items())
# pentru d.keys() -> se pot face operatii cu multimi
# exc: avem doua dictionare de frecvente pentru cuvinte din doua fisiere
# d1 = {"unu": 3, "doi": 2, "altceva": 1}
# d2 = {"unu": 2, "doi": 4, "trei": 4}

# care sunt cuvintele comune celor doua fisiera
# print(sorted(d1.keys() & d2.keys()))
# care sunt cuvintele comune + frecv cu care apar in comun
# d_inters = {min(d1[x], d2[x]) for x in d1.keys() & d2.keys()}
# print(d_inters)
# cuvintele din reuninea celor 2 fisiere
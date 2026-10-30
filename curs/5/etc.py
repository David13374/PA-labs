# se da un fisier cu informatii despre puncte in plan:
# x y eticheta
#
# 1 2 primul punct
# 1 3 alt punct
# sa se memoreze datele din fisier astfel incat sa se poata raspunde eficient la cerinta de timp
# care este eticheta punctului (x, y)
# sa se stearga punctul (x, y)
# var 1 -> lista [(x, y), eticheta] -> cautare O(n)
# var 2 -> dictionar (x, y): eticheta
# d = {(1, 2): "primul punct  "}

f = open("file.txt")

# f.read() -> un str cu tot continutul fisierului
# f.readlines() -> lista de siruri, un element - o linie din fisier
# f.readline() -> un str cu linia curenta
# !!! daca in fisier linia se termina cu delim de linie nou -> \n in str
# fisierele sunt iterabile -> se pot parcurge cu for

# for linie in f:
# d = {}
# for linie in f:
#     x, y, eticheta = linie.split(maxsplit=2)
#     x = int(x)
#     y = int(y)
#     eticheta = eticheta.strip() # rstrip()
#     print(x, y, eticheta)
#     if (x, y) not in d:
#         d[(x, y)] = []
#     d[(x, y)].append(eticheta)

# print(d)
# f.close()

# x, y = (6, 1)
# if (x, y) in d:
#     print(d[(x, y)])
# else:
#     print("nu exista")

# obs: daca un punct apare de mai multe ori in fisier va ramane cu ultima eticheta
# d[(x, y)] = eticheta -> modifica daca exista
# varianta: pentru fiecare punct sa se memoreze fiecare eticheta
# s = "**un * text *"
# s = s.strip("*") # sterge * de la inceputul si finalul sirului pana cand intalneste alt caracter
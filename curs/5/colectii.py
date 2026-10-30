# colectii
# cheie -> imutabile, cu hash
# t = (5, 6)
# print(hash(t))
# ls = [3, 4]
# # print(hash(ls)) -> eroare
# t = ([5, 6], 3)
# # print(hash(t)) -> eroare -> lui t[0] i se poate modifica valoarea

# Multimi -> set
# colectie care memoreaza elemente distincte
# elementele - care au hash -> O(1) mediu

# ls = [4, 5, -1, 4, 3, -7]
# multimea elementelor pozitive
# s = set(ls) # multimea elementelor din ls
# print(s) # ordinea elementelor nu este garantata

# s = set(x for x in ls if x >= 0)
# s = {x for x in ls if x >= 0} # -> {} -> set, dict
# print(s)

# s = {} # dict
# print(s, type(s))
# multimea vida - cu constructorul set()

# s = set()
# print(s, type(s))

# test daca 2 cuvinte au aceleasi litere

# s = "unu"
# t = "un"

# print(set(s) == set(t))

# mutabil
# add(elem) -> adauga un  element
# remove(val) -> elimina val val, daca exista din multimea
# discard(val) -> la fel ca remove, dar nu da eroare daca elementul nu este in multime

# <, <=, -> incluziunea
# operatori si metode pentru operatiile cu multimi
"""
| -> reuniune
& -> intersectie
- -> diferenta
* -> diferenta simetrica
"""

# s = {4, 5, 2}
# s1 = {2, 5, 7}

# s2 = s & s1 # returneaza o noua multime
# print(s2)

"""
metode:
    -> care returneaza multime noua: union, intersection, difference
    -> care modifica multimea: update, intersection_update, difference_update
    -> metodele pot primi mai multi parametrii, nu neaparat de tip set
"""

# s = {3, 4}
# s_n = s.union(s1, [7, 8])
# print(s, s_n)
# s.update({7, 8})
# print(s)
# parcurgere cu for, element cu element

# partitiile
# p = {{1, 2}, {4}, {3, 5}} # eroare -> set nu e hashable

# frozenset -> multime imutabila cu hash
# p = {frozenset({1, 2}), frozenset({4}), frozenset({3, 5})}
# print(p)
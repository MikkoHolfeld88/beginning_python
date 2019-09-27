#Regular Expressions search substrings of strings

import re

x = re.search("Mikko", "Analyn und Mikko werden bald heiraten")
print(x)
x = re.search("Mikko", "Liam ist Analyns Sohn")
print(x)
x = re.search("M.kko", "Analyn und Mokko werden bald heiraten") # "." steht für jeden beliebigen Character
print(x)
x = re.search(r"M[ae][iy]er","Sein Nachname ist Meyer")
print(x)


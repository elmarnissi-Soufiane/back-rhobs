#!/usr/bin/python
import sys

wealth_indicators = {}

for line in sys.stdin:
    data = line.strip().split(",")
    person = data[2] + ' ' + data[3]
    wealth = int(data[6])
        
    wealth_indicators[person] = wealth

sorted_wealth = sorted(wealth_indicators.items(), key=lambda x: x[1], reverse=True)

for i in range(3):
    if i >= len(sorted_wealth):
        break
    person, wealth = sorted_wealth[i]
    print("{0}\t{1}".format(person, wealth))


### Reponses
# Zoé Walliand	893775893
# Gerard Parmentier	892220076
# Océane Urbain	891910460


# (a) : represente l ID de chaque transaction
# (b) : contient des descriptions ou des informations supplémentaires
# (c) et (d) : Prenom et Nom
# (e) : represente le montant d'argent déposé dans une transaction
# (f) : représente le montant d'argent retiré dans une transaction
# (g) : représenter le solde total
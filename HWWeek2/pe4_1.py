cijferICOR = 7
cijferPROG = 9
cijferCSN = 8

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een {}) leveren een beloning van €{} op!'.format(gemiddelde, beloning)

print(overzicht)
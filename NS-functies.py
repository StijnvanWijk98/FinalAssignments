age = 0
reistInWeekend = False
afstand = 0
ritprijs = 0
standprijs = 0
ritkosten = 0
prijsZonderKorting = 0
textOutput = 0


def heeftRechtOpLeeftijdKorting(leeftijd, minLeeftijdKorting = 12, maxLeeftijdKorting = 64):
    return (leeftijd < minLeeftijdKorting or leeftijd > maxLeeftijdKorting)


def standaardPrijs(afstandKM, starterfeeVrij = 50, starterfeeVrijMultiplier = 0.8, normalMultiplier = 0.6 ):
    if afstandKM <= 0:
        ritkosten = 0
    elif afstandKM < starterfeeVrij:
        ritkosten = afstandKM * starterfeeVrijMultiplier
    else:
        ritkosten = 15 + afstandKM * normalMultiplier
    return ritkosten


def ritPrijs(age, weekendrit, afstandKM, kortingLeeftijd = 0.70, kortingLeeftijdWeekend = 0.65, kortingWeekend = 0.60 ):
    'hallo ik ben een mislukte docstring
    standprijs = standaardPrijs(afstandKM)
    if heeftRechtOpLeeftijdKorting(age):
        if weekendrit:
            ritprijs = standprijs*kortingLeeftijdWeekend
        else:
            ritprijs = standprijs*kortingLeeftijd
    else:
        if weekendrit:
            ritprijs = standprijs*kortingWeekend
        else:
            ritprijs = standprijs
    return round(ritprijs, 2)


def vraagtOmInformatie():
    age = int(input('Geef je leeftijd: '))
    reistInWeekend = (str(input('Reis je in het weekend? '))).lower() in ('ja', 'j', 'true')
    afstand = int(input('Hoe veel KM wil je reizen? '))
    return (age, reistInWeekend, afstand)


def output(prijs, weekendrit):
    if weekendrit:
        print('Je rit kost met korting: ', prijs, ' euro.')
    else:
        print('Je rit kost: ', prijs, ' euro.')


age, reistInWeekend, afstand = vraagtOmInformatie()
textOutput = ritPrijs(age, reistInWeekend, afstand)
output(textOutput, reistInWeekend)

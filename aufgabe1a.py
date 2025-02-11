def arithmetische_mitte(list):
    # Gebe Fehler bei leerer Liste zurück
    if len(list) == 0:
        raise ValueError("Die arithmetische Mitte ist für eine leere Liste nicht definiert.")
    # Summe der Liste berechnen
    summe = 0
    for i in list:
        summe += i
    # Länge der Liste berechenn
    laenge = len(list)
    # Arithmetische Mitte entspricht der Summe der Elemente der Liste durch die Länge der Liste
    return summe / laenge


def geometrische_mitte(list):
    # Gebe Fehler bei leerer Liste zurück
    if len(list) == 0:
        raise ValueError("Die geometrische Mitte ist für eine leere Liste nicht definiert.")
    # Produkt der Elemente Liste berechnen
    produkt = 1
    for i in list:
        produkt *= i
    laenge = len(list)
    # Die geometrische List ist die n-te Wurzel des Produktes, wobei n die Länge der Liste ist.
    return produkt ** (1 / laenge)


def harmonische_mitte(list):
    if len(list) == 0:
        raise ValueError("Der Modus ist für eine leere Liste nicht definiert.")
    # Summe der Kehrwerte der Liste berechnen
    summe_kehrwerte = 0
    for i in list:
        summe_kehrwerte += 1 / i
    if summe_kehrwerte == 0:
        raise ValueError("Die Harmonische Liste ist für Listen mit einer Summe der Kehrwerte von 0 nicht definiert.")
    laenge = len(list)
    # Die harmonische Mitte ist die Länge der Liste dividiert durch die Summe der invertierten Elemente der Liste
    return laenge / summe_kehrwerte


def median(list):
    # Gebe Fehler bei leerer Liste zurück
    if len(list) == 0:
        raise ValueError("Der Median ist für eine leere Liste nicht definiert.")
    # Erstelle sortierte Version der Liste
    listSorted = sorted(list)
    # Bestimme Länge der Liste
    length = len(list)
    # Für Listen mit gerader Anzahl berechne die arithmetische Mitte der beiden mittleren Elemente
    if length % 2 == 0:
        return + (list[length // 2 - 1] + list[length // 2]) / 2
    # Für Listen mit ungerade Anzahl gib das mittlere Element zurück
    return listSorted[length // 2]


def modus(list):
    # Gebe Fehler bei leerer Liste zurück
    if len(list) == 0:
        raise ValueError("Der Modus ist für eine leere Liste nicht definiert.")
    # Erstelle dictionary mit Häufigkeit der Werte aus der Liste
    d = dict()
    for wert in list:
        d.update({wert: d.get(wert, 0) + 1})
    # Hole Tuples aus dem Dictionary (Wert,Häufigkeit) und sortiere nach Häufigkeit (also absteigend)
    tuples = sorted(d.items(), key=lambda tuple: tuple[1], reverse=True)
    # Gib das Wort des ersten Wert aus der Tuple Liste (höchstes Vorkommen) zurück
    return tuples[0][0]


def varianz(list):
    # Gebe Fehler bei leerer Liste zurück
    if len(list) == 0:
        raise ValueError("Die Varianz ist für eine leere Liste nicht definiert.")
    # Berechne Arithmetische Mitte für Liste
    mitte = arithmetische_mitte(list)
    # Berechne Summe der Quadratischen Abweichungen zur Liste
    summe_quadratische_abweichung = 0
    for i in list:
        summe_quadratische_abweichung += abs(i - mitte) ** 2
    laenge = len(list)
    # Gib die Summe der quadratischen Abweichung geteilt durch die Länge der Liste zurück
    return summe_quadratische_abweichung / laenge


def standard_abweichung(list):
    # Berechne die Varianz der liste
    varianzListe = varianz(list)
    # Gib die Quadratwurzel der Varianz zurück
    return varianzListe ** 0.5


def variationskoeffizient(list):
    # Berechne den athmetische Mitte der Liste
    mittelwert = arithmetische_mitte(list)
    if (mittelwert == 0):
        raise ValueError("Der Variationskoeffizient ist bei einem Mittelwert von 0 nicht definiert ")
    # Berechne die Standardabweichung der Liste
    std_abweichung = standard_abweichung(list)
    return std_abweichung / mittelwert

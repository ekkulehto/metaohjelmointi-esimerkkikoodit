# määritellään dekoraattori
def dekoraattori(alkuperäinen_funktio):

    # sisäinen funktio, joka käärii alkuperäisen funktion
    def kääritty_alkuperäinen_funktio(*argumentit, **avainsanat):

        # *argumentit = kerää ilman avainsanaa annetut argumentit tupleen (esim. 1)
        # **avainsanat = kerää avainsanalla annetut argumentit sanakirjaan (esim. a = 1)

        # lisätään tulostus joka kertoo mikä funktio suoritetaan
        print(f"Suoritetaan funktio '{alkuperäinen_funktio.__name__}'")

        # kutsutaan alkuperäistä funktiota sille annetuilla argumenteilla
        return alkuperäinen_funktio(*argumentit, **avainsanat)

    # palautetaan kääritty alkuperäinen funktio
    return kääritty_alkuperäinen_funktio

# lisätään dekoraattori funktioon sen yläpuolelle @-merkillä


@dekoraattori
def tervehdi(nimi):
    return f"Moikka {nimi}!"


# kutsutaan funktiota normaalisti
print(tervehdi("AIC23SP"))

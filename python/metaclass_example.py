# metaluokka perii typen joka on sisäänrakennettu metaluokka jolla luokat luodaan oletuksena
class Metaluokka(type):

    # yliajetaan (__new__) alkuperäinen luokanluonti prosessi
    def __new__(itse_metaluokka, luokan_nimi, perityt_luokat, luokan_attribuutit):

        # määritellään funktio 'tervehdi'
        def tervehdi(luokka):
            return f"Moikka {luokka}!"

        # tulostetaan mikä funktio lisätään ja mihin luokkaan
        print(
            f"Lisätään funktio '{tervehdi.__name__}' luokkaan '{luokan_nimi}'")

        # lisätään luokan attribuutteihin (sanakirja) tervehdi-funktio nimellä tervehdi
        luokan_attribuutit['tervehdi'] = tervehdi

        # palautetaan lopullinen luokka, joka sisältää nyt tervehdi-funktion
        return super().__new__(itse_metaluokka, luokan_nimi, perityt_luokat, luokan_attribuutit)


class TyhjäLuokka(metaclass=Metaluokka):
    # luodaan aluksi TyhjäLuokka ilman funktioita tai attribuutteja
    # metaluokka lisää funktion 'tervehdi' tänne automaattisesti
    pass


print(TyhjäLuokka.tervehdi("AIC23SP"))

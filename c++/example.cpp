// tuodaan iostream-kirjasto tulostusta varten
#include <iostream>

// otetaan std-nimiavaruudesta cout käyttöön (helpottamaan kirjoitusta)
using std::cout;

// mallipohja, jossa 'sivu' on käännösaikainen vakio-parametri
template <int sivu>
struct Neliö
{
    // constexpr takaa, että pinta-ala lasketaan käännösaikana
    static constexpr int pinta_ala = sivu * sivu;
};

// pääohjelma
int main()
{
    // tulostusvirtaan merkkijono "10^2 = " ja käännösaikainen laskettu arvo "100"
    cout << "10^2 = " << Neliö<10>::pinta_ala;

    // palautetaan 0, mikä kertoo, että ohjelma päättyi onnistuneesti
    return 0;
}

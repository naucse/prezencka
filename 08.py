def nakresli_mapu(seznam_souradnic):
    "dostane seznam souradnic a vypise je jako mapu"
    mapa = []
    for cislo_radku in range(10):
        radek = []
        for cislo_sloupce in range(10):
            radek.append(".")
            print(radek)
    for ntice in souradnice:
        print(ntice)
        cislo_sloupce, cislo_radku = ntice

        mapa[cislo_radku][cislo_sloupce] = 'X'
    for radek in mapa:
        for symbol in radek:
            print(symbol, end= ' ')
            print()

nakresli_mapu([(0, 0), (1, 0), (2, 2)])



def pohyb (souradnice, strana):
    "dostane seznam souradnic a svetovou stranu"

    cislo_sloupce, cislo_radku = souradnice[-1]

    if strana == "v":
        cislo_sloupce = cislo_sloupce + 1
    elif strana == 'z':
        cislo_sloupce = cislo_sloupce - 1

    print(ntice)
souradnice = [(0, 0)]
pohyb(souradnice, 'v')
print (souradnice)

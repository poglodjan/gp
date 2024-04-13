
#aktualne miejsce odrodzenia gracza, zmienne w zależnośći od checkpointu, ktróy zaliczymy
aktualnaPozycjaOdrodzenia=player.position()
#zmienna pomocnicza dzięki niej dany etap będzie tworzony raz w ramach jednej rozgrywki
czyEtap1=False
czyEtap2=False
czyEtap3=False
czyEtap4=False



#budujemy schody oraz pierwszą platformę ładującą etap 1
def nowyParkour():
    #teleportujemy konstrukotr w okolice gracza
    builder.teleport_to(pos(5, 0, 0))
    #obracamy
    builder.face(EAST)
    for i in range(70):
        #konstruktor umieszcza blok schodów
        builder.place(PURPUR_STAIRS)
        #konstruktor przemieszcza się odpowiednio w przód,górę i lewo o podaną liczbę bloków
        builder.shift(1, 1, 0)
    #oznaczamy bieżącą pozycję konstruktora
    builder.mark()
    builder.shift(2, 0, -4)
    #konstruktor wypełnia przestrzeń blokami od znaku(mark) do obecnej pozycji
    builder.fill(DIAMOND_BLOCK)
player.on_chat("start", nowyParkour)


def smierc():
    #dodajemy przerwę żeby poprawnie działało odradzanie gracza na platformie checkpoint
    loops.pause(500)
    player.teleport(aktualnaPozycjaOdrodzenia)
player.on_died(smierc)


def etap1i2(obrotKonstruktora,rodzajToru,rodzajCheckpoint):
    #teleport konstruktora pod platformę i przesunięcie
    builder.teleport_to(pos(1, -4, 0))
    builder.mark()
    builder.face(EAST)
    for i in range(2):
        for j in range(5):
            #przesuwamy konstruktor
            builder.move(FORWARD, randint(3, 8))
            #tworzymy linie z danego bloku 
            builder.line(rodzajToru)
            #przesuwamy konstruktor w celu zrobienia przerwy pomiędzy blokami
            builder.move(FORWARD, randint(2, 3))
            #oznaczamy aktulaną pozycję żeby to od niej budowała się kolejna linia
            builder.mark()
            #obrót konstruktora
        builder.turn(obrotKonstruktora)
    builder.mark()
    builder.shift(2, 0, -4)
    builder.fill(rodzajCheckpoint)



#pętla sterująca ładowaniem etapów oraz system checkpoint
while True:
    if blocks.test_for_block(DIAMOND_BLOCK, pos(0, -1, 0)) and not czyEtap1:
        #aktualizujemy pozycje gracza
        aktualnaPozycjaOdrodzenia = player.position()
        czyEtap1 = True
        etap1i2(RIGHT_TURN,SLIME_BLOCK,GOLD_BLOCK)
        

        

   
        

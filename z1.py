
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


def etap3():
    #tworzymy kulę ze szlamu
    shapes.sphere(SLIME_BLOCK, pos(4, -30, 0), 1, ShapeOperation.REPLACE)
    builder.teleport_to(pos(6, -32, 0))
    builder.mark()
    builder.face(EAST)
    #ustawiamy pozycję pierwotną póżniej wrócimy w to miejsce konstruktorem i bęziemy dodawać ogień
    builder.set_origin()
    builder.move(FORWARD, 65)
    builder.line(NETHERRACK)
    #budowa platformy
    builder.move(FORWARD, 4)
    builder.mark()
    builder.shift(2, 0, -4)
    builder.fill(MOSS_STONE)
    #wracamy aby dodać ogień
    builder.teleport_to_origin()
    builder.move(UP, 1)
    for i in range(11):
        builder.move(FORWARD, randint(3, 8))
        builder.place(FIRE)


def etap4():
    #projektujemy skok wiary
    builder.move(DOWN, 30)
    builder.face(SOUTH)
    builder.move(FORWARD, 6)
    #budujemy studnię z wodą
    builder.mark()
    builder.shift(2, 2, 2)
    builder.fill(BRICKS)
    builder.shift(-1, 0, -1)
    builder.place(WATER)
    builder.move(FORWARD, 4)
    builder.set_origin()
    #pętla tworząca schody spieralne kończy swoje działanie kiedy gracz stanie na ostatniej platformie
    while not (blocks.test_for_block(SEA_LANTERN, pos(0, -1, 0))):
        builder.teleport_to_origin()
        builder.face(SOUTH)
        #budowanie schodów w każdej chwili może być przerwane kiedy gracz stanie na ostatniej platformie
        for i in range(30):
            if not blocks.test_for_block(SEA_LANTERN, pos(0, -1, 0)):
                builder.place(POLISHED_GRANITE)
                builder.move(FORWARD, 1)
                builder.move(UP, 1)
                builder.turn(RIGHT_TURN)
            else:
                break
        builder.mark()
        builder.shift(-2, 0, 2)
        builder.fill(SEA_LANTERN)
        builder.teleport_to_origin()
        builder.face(SOUTH)
        loops.pause(8000)
        #podmieniamy schody na blok magmy
        for i in range(30):
            if not blocks.test_for_block(SEA_LANTERN, pos(0, -1, 0)):
                builder.place(MAGMA_BLOCK)
                builder.move(FORWARD, 1)
                builder.move(UP, 1)
                builder.turn(RIGHT_TURN)
                loops.pause(1000)
            else:
                break
    #gracz otrzymuje perłe kresu, która posłuży do teleportacji
    mobs.give(mobs.target(NEAREST_PLAYER), ENDER_PEARL, 1)
#pętla sterująca ładowaniem etapów oraz system checkpoint
while True:
    if blocks.test_for_block(DIAMOND_BLOCK, pos(0, -1, 0)) and not czyEtap1:
        #aktualizujemy pozycje gracza
        aktualnaPozycjaOdrodzenia = player.position()
        czyEtap1 = True
        etap1i2(RIGHT_TURN,SLIME_BLOCK,GOLD_BLOCK)
        

    elif blocks.test_for_block(GOLD_BLOCK, pos(0, -1, 0)) and not czyEtap2:
        aktualnaPozycjaOdrodzenia = player.position()
        czyEtap2 = True
        etap1i2(LEFT_TURN,MAGENTA_STAINED_GLASS_PANE,BEDROCK)
        

    elif blocks.test_for_block(BEDROCK, pos(0, -1, 0)) and not czyEtap3:
        aktualnaPozycjaOdrodzenia = player.position()
        czyEtap3 = True
        etap3()
        

    elif blocks.test_for_block(MOSS_STONE, pos(0, -1, 0)) and not czyEtap4:
        aktualnaPozycjaOdrodzenia = player.position()
        czyEtap4 = True
        etap4()
        

   
        

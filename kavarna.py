import random

pocet_zakazniku = 3
den_hry = 1
stav = {"penize": 1000, "reputace": 50,
        "kava": 0, "mleko": 0, "cukr": 0,
        "caj": 0, "cokolada": 0, "kavovar": True}

RECEPTY = {
    "Káva": {"kava": 1, "cukr": 1},
    "Cappuccino": {"kava": 1, "mleko": 1},
    "Čaj": {"caj": 1, "cukr": 1},
    "Horká čokoláda": {"cokolada": 1, "mleko": 1},
}
CENY = {"Káva": 190, "Cappuccino": 210, "Čaj": 130, "Horká čokoláda": 190}


def start ():
    print("Zdědíš malou kavárnu po své babičce. Máš 7 dní na to, abys vydělala dost peněz a zachránila ji před zavřením.")
    print()
    print("Jenže:")
    print("Máš omezené peníze")
    print("Občas se něco pokazí")
    print("Musíš nakupovat suroviny a platit denní náklady")
    print("Tvoje rozhodnutí ovlivní reputaci kavárny")
    print("Cíl: vydělat dost peněz a udržet si dobrou reputaci.")
    print()

    while True:
        volba = input("Jdeš do toho? 1 = ano 2 = ne: ")

        if volba == "1":
            nastaveni_hry()
            den()
            return

        elif volba == "2":
            spatny_konec()
            return

        else:
            print("Neplatná volba!")


def nastaveni_hry():
    print(stav)
    print(RECEPTY)
    print(CENY)


def nakup_kavy():
    if stav["penize"] >= 80:
        stav["penize"] -= 80
        stav["kava"] += 1
        print("Koupila sis jednu dávku kávy!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_mleka():
    if stav["penize"] >= 40:
        stav["penize"] -= 40
        stav["mleko"] += 1
        print("Koupila sis jednu dávku mléka!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_cukr():
    if stav["penize"] >= 20:
        stav["penize"] -= 20
        stav["cukr"] += 1
        print("Koupila sis jednu dávku cukru!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_caj():
    if stav["penize"] >= 30:
        stav["penize"] -= 30
        stav["caj"] += 1
        print("Koupila sis jednu dávku čaje!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_cokolady():
    if stav["penize"] >= 65:
        stav["penize"] -= 65
        stav["cokolada"] += 1
        print("Koupila sis jednu dávku čokolády!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_vse():
    cena = 235

    if stav["penize"] >= cena:
        stav["penize"] -= cena
        stav["kava"] += 1
        stav["mleko"] += 1
        stav["cukr"] += 1
        stav["caj"] += 1
        stav["cokolada"] += 1
        print("Koupila sis všechny suroviny za 235 Kč!")
    else:
        print("Nemáš dostatek peněz!")


def nakup_surovin():
    while True:
        print()
        print("Vítej v obchodě se surovinami.")
        print("Tvoje peníze:", stav["penize"], "Kč")
        print("Tvoje zásoby:")
        print()
        print("Káva:", stav["kava"])
        print("Mléko:", stav["mleko"])
        print("Cukr:", stav["cukr"])
        print("Čaj:", stav["caj"])
        print("Čokoláda:", stav["cokolada"])
        print()

        print("1. Koupit kávu (80 Kč)")
        print("2. Koupit mléko (40 Kč)")
        print("3. Koupit cukr (20 Kč)")
        print("4. Koupit čaj (30 Kč)")
        print("5. Koupit čokoládu (65 Kč)")
        print("6. Koupit všechny suroviny (235 Kč)")
        print("7. Opravit kávovar (50 Kč)")
        print("8. Zpět")
        print()

        volba = input("Můžeš se rozhodnout! (1-8): ")
        print()
        print("========================")
        print()

        if volba == "1":
            nakup_kavy()
        elif volba == "2":
            nakup_mleka()
        elif volba == "3":
            nakup_cukr()
        elif volba == "4":
            nakup_caj()
        elif volba == "5":
            nakup_cokolady()
        elif volba == "6":
            nakup_vse()
        elif volba == "7":
            if stav["kavovar"] == False:
                if stav["penize"] >= 50:
                    stav["penize"] -= 50
                    stav["kavovar"] = True
                    print("Kávovar je opravený!")
                else:
                    print("Nemáš dostatek peněz na opravu!")
            else:
                print("Kávovar je již v pořádku.")

        elif volba == "8":
            break
        else:
            print("Neplatná volba!")


def hlavni_menu():
    while True:
        print("\n--- HLAVNÍ MENU ---")
        print("1 - Obsloužit zákazníka")
        print("2 - Nakoupit suroviny")
        print("3 - Zobrazit recepty")
        print("4 - Zkontrolovat stav kavárny")

        menu = input("Co si vybereš? ")

        if menu == "1":
            obsluha()
            break
        elif menu == "2":
            nakup_surovin()
        elif menu == "3":
            recepty()
        elif menu == "4":
            nastaveni_hry()
        else:
            print("Neplatná volba!")


def recepty():
    print("Otevíráš svou knihu receptů.")
    print("Tady zjistíš, co potřebuješ na přípravu jednotlivých nápojů.")
    print()
    print("Seznam nápojů:")
    print()

    print("KÁVA:")
    print("1 dávka kávy")
    print("1 dávka cukru")
    print()

    print("CAPPUCCINO:")
    print("1 dávka kávy")
    print("1 dávka mléka")
    print()

    print("ČAJ:")
    print("1 dávka čaje")
    print("1 dávka cukru")
    print()

    print("HORKÁ ČOKOLÁDA:")
    print("1 dávka čokolády")
    print("1 dávka mléka")
    print()

    while True:
        vratit_se = input("Chceš se vrátit do hlavního menu? 1 = ano 2 = ne: ")
        if vratit_se == "1":
            return
        elif vratit_se == "2":
            print("Zůstáváš v knize receptů.")
        else:
            print("Neplatná volba!")


def obsluha():
    print()
    print()
    print("Do kavárny přicházejí první zákazníci.")
    print("Připravuješ objednávky a snažíš se, aby všichni odcházeli spokojení.")
    print()

    print("Seznam nápojů")
    print("Káva")
    print("Cappuccino")
    print("Čaj")
    print("Horká čokoláda")
    print()

    objednavka = random.choice(list(RECEPTY))
    print("Zákazník si objednal:", objednavka)

    if objednavka == "Káva":
        if stav["kava"] >= 1 and stav["cukr"] >= 1 and stav["kavovar"]:
            stav["kava"] -= 1
            stav["cukr"] -= 1
            stav["penize"] += 190
            stav["reputace"] += 5
            print("Měla jsi dostatek surovin a tak jsi připravila zákazníkovi kávu.")
            print("Zákazník odchází spokojený.")
        else:
            stav["reputace"] -= 5
            print("Bohužel nemáš dostatek surovin.")
            print("Zákazník odchází zklamaný.")

    elif objednavka == "Cappuccino":
        if stav["kava"] >= 1 and stav["mleko"] >= 1 and stav["kavovar"]:
            stav["kava"] -= 1
            stav["mleko"] -= 1
            stav["penize"] += 210
            stav["reputace"] += 5
            print("Měla jsi dostatek surovin a tak jsi připravila zákazníkovi Cappuccino.")
            print("Zákazník odchází spokojený.")
        else:
            stav["reputace"] -= 5
            print("Bohužel nemáš dostatek surovin.")
            print("Zákazník odchází zklamaný.")

    elif objednavka == "Čaj":
        if stav["caj"] >= 1 and stav["cukr"] >= 1:
            stav["caj"] -= 1
            stav["cukr"] -= 1
            stav["penize"] += 130
            stav["reputace"] += 5
            print("Měla jsi dostatek surovin a tak jsi připravila zákazníkovi Čaj.")
            print("Zákazník odchází spokojený.")
        else:
            stav["reputace"] -= 5
            print("Bohužel nemáš dostatek surovin.")
            print("Zákazník odchází zklamaný.")

    elif objednavka == "Horká čokoláda":
        if stav["cokolada"] >= 1 and stav["mleko"] >= 1:
            stav["cokolada"] -= 1
            stav["mleko"] -= 1
            stav["penize"] += 190
            stav["reputace"] += 5
            print("Měla jsi dostatek surovin a tak jsi připravila zákazníkovi Horkou čokoládu.")
            print("Zákazník odchází spokojený.")
        else:
            stav["reputace"] -= 5
            print("Bohužel nemáš dostatek surovin.")
            print("Zákazník odchází zklamaný.")


def nahodna_udalost():
    seznam_udalosti = [
        "Do kavárny přišlo více zákazníků",
        "Dodavatel ti přinesl suroviny zdarma",
        "Dnes se nic zvláštního nestalo",
        "Pokazil se kávovar"
    ]

    udalost = random.choice(seznam_udalosti)

    if udalost == "Do kavárny přišlo více zákazníků":
        print("Dnes přišlo o dva zákazníky víc! Obsluha bude náročnější.")
        return udalost, 2

    elif udalost == "Dodavatel ti přinesl suroviny zdarma":
        stav["kava"] += 1
        stav["mleko"] += 1
        stav["cukr"] += 1
        stav["caj"] += 1
        stav["cokolada"] += 1
        print("Dodavatel ti přinesl suroviny zdarma!")
        return udalost, 0

    elif udalost == "Pokazil se kávovar":
        if stav["penize"] >= 50:
            stav["penize"] -= 50
            stav["kavovar"] = True
            print("Pokazil se kávovar. Oprava tě stála 50 Kč!")
        else:
            stav["kavovar"] = False
            print("Pokazil se kávovar, ale nemáš dost peněz na opravu!")
            print("Nemůžeš připravovat kávu ani cappuccino.")
        return udalost, 0
    else:
        print("Dnes se nic zvláštního nestalo.")
        return udalost, 0


def den():
    global den_hry, pocet_zakazniku

    while den_hry <= 7:
        print("\n====================")
        print("ZAČÍNÁ", den_hry, ". DEN")
        print("====================")

        pocet_zakazniku = 3
        print()
        if stav["penize"] >= 80:
            stav["penize"] -= 80
            print("Zaplatila sis denní náklady: 80 Kč.")
        else:
            print("Nemáš dostatek peněz na zaplacení denních nákladů.")
            spatny_konec()
            return
        print()
        nakup_surovin()
        print()
        udalost, prirazeni = nahodna_udalost()
        pocet_zakazniku += prirazeni
        print("Dnešní událost:", udalost)
        print("Dnes přijde tolik zákazníků:", pocet_zakazniku)

        for cislo in range(pocet_zakazniku):
            print("\n--------------------")
            print("Zákazník číslo:", cislo + 1)
            print("--------------------")
            hlavni_menu()

        print("\nKonec dne", den_hry)
        den_hry += 1

    print("Uplynulo všech 7 dní.")
    if stav["reputace"] <= 30 or stav["penize"] < 200:
        print("Bohužel se ti nepodařilo zachránit babiččinu kavárnu.")
        spatny_konec()
    else:
        print("Gratuluji! Zachránila jsi babiččinu kavárnu a máš dobrou reputaci!")


def spatny_konec():
    print("Bohužel se ti nepodařilo zachránit babiččinu kavárnu.")
    print("Babiččina kavárna se zavírá.")
    print("KONEC HRY")

start()


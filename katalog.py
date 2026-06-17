# -*- coding: utf-8 -*-
"""
Katalog hulajnog - dane skopiowane z kategorii hulajnogi sklepu Majway.

Kazdy produkt ma:
  predkosc/zasieg/moc/bateria/napiecie - szybkie parametry (kafelki, karty)
  opis  - pelny opis produktu
  cechy - tabela "Cechy towaru": lista par (etykieta, wartosc)
  kategoria = marka (dziala jako filtr)
"""

PRODUKTY = [
    {
        "id": 1,
        "nazwa": "Langfeite GT2 RS Dual 2x4000W 50Ah 84V",
        "kategoria": "Langfeite",
        "cena": 21999.00, "stara_cena": None,
        "kolor": "#ef4444",
        "predkosc": 120, "zasieg": 160, "moc": 8000, "bateria": 50, "napiecie": 84,
        "promocja": False, "etykieta": "Przedsprzedaż",
        "opis": "Langfeite GT2 RS to ekstremalny skuter elektryczny z dwoma silnikami "
                "bezszczotkowymi po 4000 W (szczytowo 2×8000 W), osiągający prędkość maksymalną "
                "do 120 km/h. Wyposażony jest w potężny akumulator Samsung 84 V 50 Ah (4200 Wh) "
                "zapewniający zasięg do 160 km na jednym ładowaniu. Pojazd ma podwójne zawieszenie "
                "sprężynowe z przodu i z tyłu, hydrauliczne hamulce 4-tłoczkowe oraz 13-calowe "
                "opony bezdętkowe dla doskonałej przyczepności. Mocna rama aluminiowo-stalowa "
                "wytrzymuje obciążenia do 120 kg, a całość waży 88 kg z zaawansowanym systemem składania.",
        "cechy": [
            ("Moc nominalna", "2×4000 W"), ("Moc szczytowa", "2×8000 W"),
            ("Prędkość max.", "120 km/h"), ("Zasięg", "do 160 km"),
            ("Akumulator", "50 Ah 84 V Samsung (4200 Wh)"),
            ("Hamulce", "hydrauliczne 4-tłoczkowe + EBS"),
            ("Amortyzacja", "pełna sprężynowa"), ("Opony", "13\" bezdętkowe"),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "50°"),
            ("Nośność", "120 kg"), ("Waga", "88 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 2,
        "nazwa": "Dualtron X LTD 2x2800W 60Ah 84V",
        "kategoria": "Dualtron",
        "cena": 18899.00, "stara_cena": None,
        "kolor": "#0ea5e9",
        "predkosc": 100, "zasieg": 170, "moc": 5600, "bateria": 60, "napiecie": 84,
        "promocja": False, "etykieta": None,
        "opis": "Flagowy Dualtron X Limited to hulajnoga elektryczna z dwoma silnikami o mocy "
                "nominalnej 5600 W i szczytowej 12 000 W, zapewniającymi prędkość do 100 km/h. "
                "Zasilana akumulatorem LG 84 V 60 Ah (5040 Wh) pokonuje do 170 km na jednym "
                "ładowaniu. Wyposażona w hydrauliczne zawieszenie z progresywnymi sprężynami, "
                "13-calowe bezdętkowe opony i hydrauliczne hamulce tarczowe 160 mm. Ważący 82,9 kg "
                "pojazd łączy bezkompromisową moc, zaawansowaną technologię i niezrównaną "
                "stabilność z możliwością pokonywania podjazdów do 50°.",
        "cechy": [
            ("Moc nominalna", "2×2800 W"), ("Moc szczytowa", "2×6000 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 170 km"),
            ("Akumulator", "84 V 60 Ah LG (5040 Wh)"),
            ("Czas ładowania", "12 h (szybka ładowarka)"),
            ("Hamulce", "hydrauliczne 4-tłoczkowe"), ("Amortyzacja", "pełna regulowana"),
            ("Rozmiar koła", "13\""), ("Klasa szczelności", "IPX5"),
            ("Kąt podjazdu", "50°"), ("Nośność", "150 kg"), ("Waga", "82,9 kg"),
            ("Aplikacja", "tak"), ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 3,
        "nazwa": "Teverun Fighter Supreme 7260R V4 2x2500W 60Ah 72V",
        "kategoria": "Teverun",
        "cena": 16999.00, "stara_cena": None,
        "kolor": "#f59e0b",
        "predkosc": 110, "zasieg": 180, "moc": 5000, "bateria": 60, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Teverun Fighter Supreme 7260R V4 to hulajnoga z podwójnym napędem 2×2500 W "
                "(moc szczytowa do 15 000 W) i baterią 60 Ah 72 V (4320 Wh) zapewniającą zasięg "
                "do 180 km. Osiąga prędkość maksymalną 110 km/h i oferuje pięć trybów jazdy. "
                "Regulowane zawieszenie hydrauliczne o skoku 34 mm wraz z hydraulicznymi hamulcami "
                "4-tłoczkowymi zapewnia pełną kontrolę i bezpieczeństwo. 13-calowe opony CST, waga "
                "63 kg, klasa szczelności IPX5 oraz system GPS i blokada NFC to cechy premium tego modelu.",
        "cechy": [
            ("Moc nominalna", "2×2500 W"), ("Moc szczytowa", "do 15 000 W"),
            ("Prędkość max.", "110 km/h"), ("Zasięg", "do 180 km"),
            ("Akumulator", "60 Ah 72 V (4320 Wh)"), ("Czas ładowania", "12 h"),
            ("Hamulce", "hydrauliczne 4-tłoczkowe"),
            ("Amortyzacja", "pełna regulowana typu C"), ("Rozmiar koła", "13\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "50°"),
            ("Nośność", "150 kg"), ("Waga", "63 kg"), ("Aplikacja", "tak"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 4,
        "nazwa": "Dualtron New Storm LTD 2x2500W 45Ah 84V",
        "kategoria": "Dualtron",
        "cena": 16599.00, "stara_cena": None,
        "kolor": "#0ea5e9",
        "predkosc": 100, "zasieg": 150, "moc": 5000, "bateria": 45, "napiecie": 84,
        "promocja": False, "etykieta": "Przedsprzedaż",
        "opis": "Dualtron New Storm Limited to hulajnoga elektryczna wyposażona w dwa silniki "
                "2500 W każdy (łącznie 5000 W mocy ciągłej), osiągająca prędkość maksymalną "
                "100 km/h. Akumulator LG 84 V 45 Ah (3780 Wh) zapewnia zasięg do 150 km na jednym "
                "ładowaniu przy czasie ładowania około 12 godzin. System zawieszenia elastomerowego "
                "gwarantuje wyjątkowy komfort jazdy bez konieczności częstej konserwacji. "
                "Hydrauliczne hamulce tarczowe z systemem EBS zapewniają natychmiastową reakcję, "
                "a 11-calowe szerokie opony doskonałą przyczepność. Maksymalna ładowność to 150 kg.",
        "cechy": [
            ("Moc nominalna", "2×2500 W"), ("Prędkość max.", "100 km/h"),
            ("Zasięg", "do 150 km"), ("Akumulator", "84 V 45 Ah LG (3780 Wh)"),
            ("Czas ładowania", "12 h"), ("Hamulce", "hydrauliczne + EBS"),
            ("Amortyzacja", "pełna elastomerowa"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Nośność", "150 kg"),
            ("Waga", "55,5 kg"), ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 5,
        "nazwa": "Nami Burn-e 3 Max 2x1500W 40Ah 72V",
        "kategoria": "Nami",
        "cena": 16399.00, "stara_cena": None,
        "kolor": "#10b981",
        "predkosc": 90, "zasieg": 140, "moc": 3000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Nami Burn-e 3 Max to topowa hulajnoga napędzana dwoma silnikami o mocy 1500 W "
                "każdy, osiągająca prędkość maksymalną 90 km/h. Wyposażona w akumulator LG 72 V "
                "40 Ah (2880 Wh) zapewniający zasięg do 140 km. Posiada kultowe, regulowane "
                "zawieszenie o skoku 165 mm, hydrauliczne hamulce Logan z 4-tłoczkowymi zaciskami "
                "oraz bezdętkowe opony 11\". Całkowita masa wynosi 51 kg, a maksymalna ładowność "
                "120 kg. W zestawie szybka ładowarka 5 A, amortyzator skrętu i liczne funkcje bezpieczeństwa.",
        "cechy": [
            ("Moc nominalna", "2×1500 W"), ("Prędkość max.", "90 km/h"),
            ("Zasięg", "do 140 km"), ("Akumulator", "40 Ah 72 V (2880 Wh) LG"),
            ("Czas ładowania", "8 h"), ("Hamulce", "hydrauliczne Logan 4-tłoczkowe"),
            ("Amortyzacja", "regulowana pełna typu C"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "51 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 6,
        "nazwa": "Kaabo Wolf King GTR MAX 2x2000W 40Ah 72V",
        "kategoria": "Kaabo",
        "cena": 15999.00, "stara_cena": None,
        "kolor": "#a855f7",
        "predkosc": 105, "zasieg": 140, "moc": 4000, "bateria": 40, "napiecie": 72,
        "promocja": True, "etykieta": "Promocja",
        "opis": "Kaabo Wolf King GTR MAX to ekstremalna moc i technologia bez kompromisów — dwa "
                "silniki 2000 W dają 4000 W mocy nominalnej i aż 13 440 W szczytowej, rozpędzając "
                "hulajnogę do 105 km/h. Akumulator Samsung 72 V 40 Ah (2880 Wh) zapewnia zasięg do "
                "140 km z opcją podwójnego ładowania. Pełne zawieszenie przód i tył oraz hydrauliczne "
                "hamulce tarczowe gwarantują komfort i bezpieczeństwo, a 11-calowe opony terenowe "
                "pewną przyczepność na każdym podłożu. Lotnicza rama aluminiowa waży 67 kg i pokonuje "
                "podjazdy do 50°. Wyposażenie: kolorowy wyświetlacz LCD, Bluetooth z aplikacją, alarm, "
                "kierunkowskazy, tempomat i system antykradzieżowy.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Moc szczytowa", "13 440 W"),
            ("Prędkość max.", "105 km/h"), ("Zasięg", "do 140 km"),
            ("Akumulator", "40 Ah 72 V (2880 Wh) Samsung"),
            ("Czas ładowania", "10 h (dwie ładowarki)"), ("Hamulce", "hydrauliczne + EBS"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "50°"),
            ("Nośność", "150 kg"), ("Waga", "67 kg"), ("Aplikacja", "tak"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 7,
        "nazwa": "Dualtron Thunder III 2x2500W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 14599.00, "stara_cena": None,
        "kolor": "#0ea5e9",
        "predkosc": 100, "zasieg": 120, "moc": 5000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": "Przedsprzedaż",
        "opis": "Dualtron Thunder III to elektryczna hulajnoga wysokich osiągów wyposażona w dwa "
                "silniki o łącznej mocy nominalnej 5000 W (szczytowo do 11 000 W), umożliwiające "
                "osiągnięcie prędkości do 100 km/h. Akumulator LG M50LT 72 V 40 Ah zapewnia zasięg "
                "do 120 km na jednym ładowaniu. Pojazd wyróżnia się hydraulicznymi hamulcami "
                "tarczowymi NUTT o średnicy 160 mm oraz zawieszeniem z regulowaną amortyzacją. "
                "11-calowe bezdętkowe opony Ultra-Wide zapewniają doskonałą przyczepność. "
                "Konstrukcja waży 47,3 kg, oferuje wodoszczelność IPX5 i pokonuje wzniesienia do 50°.",
        "cechy": [
            ("Moc nominalna", "2×2500 W"), ("Moc szczytowa", "do 11 000 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 120 km"),
            ("Akumulator", "40 Ah 72 V (2880 Wh) LG"),
            ("Czas ładowania", "16-8 h (dwie ładowarki)"),
            ("Hamulce", "NUTT hydrauliczne + EBS"), ("Amortyzacja", "pełna elastomerowa"),
            ("Rozmiar koła", "11\""), ("Klasa szczelności", "IPX5"),
            ("Kąt podjazdu", "50°"), ("Nośność", "120 kg"), ("Waga", "47,3 kg"),
            ("Aplikacja", "tak"), ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 8,
        "nazwa": "Vsett 11+ Super72 2x2000W 35Ah 72V",
        "kategoria": "Vsett",
        "cena": 14399.00, "stara_cena": None,
        "kolor": "#14b8a6",
        "predkosc": 100, "zasieg": 140, "moc": 4000, "bateria": 35, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "VSETT 11+ Super72 to zaawansowana hulajnoga elektryczna napędzana dwoma silnikami "
                "2000 W każdy, generującymi 4000 W mocy ciągłej i ponad 6000 W szczytowej. Osiąga "
                "maksymalną prędkość 100 km/h z zasięgiem do 140 km dzięki akumulatorowi LG 72 V "
                "35 Ah. Wyposażona w podwójne zawieszenie hydrauliczne, opony 11×4 cala oraz "
                "hydrauliczne hamulce tarczowe NUTT zapewniające precyzyjne hamowanie. Model oferuje "
                "system LED z kierunkowskazami, NFC, tempomat, przycisk turbo boost i składaną "
                "kolumnę, przy wadze 58 kg i nośności 150 kg.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Moc szczytowa", "ponad 6000 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 140 km"),
            ("Akumulator", "35 Ah 72 V LG (2520 Wh)"),
            ("Czas ładowania", "16-8 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne tarczowe NUTT"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Opony", "11×4\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "150 kg"), ("Waga", "58 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 9,
        "nazwa": "Teverun Fighter Supreme 7260R V3 2x2500W 60Ah 72V",
        "kategoria": "Teverun",
        "cena": 13999.00, "stara_cena": None,
        "kolor": "#f59e0b",
        "predkosc": 110, "zasieg": 180, "moc": 5000, "bateria": 60, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Teverun Fighter Supreme 7260R V3 to pojazd wysokiej klasy napędzany dwoma "
                "silnikami 2500 W każdy (łącznie 5000 W, szczyt 15 000 W), osiągający prędkość do "
                "110 km/h. Akumulator 72 V 60 Ah zapewnia zasięg do 180 km na jednym ładowaniu. "
                "Wyposażony w regulowane zawieszenie hydrauliczne 34 mm, hamulce hydrauliczne "
                "4-tłoczkowe i opony CST 13-calowe. Waży 60 kg, posiada ekran TFT 3,5\", system GPS, "
                "blokadę NFC oraz klasę szczelności IPX5. W zestawie ładowarka 5 A, amortyzatory "
                "wibracji i aplikacja mobilna do personalizacji ustawień.",
        "cechy": [
            ("Moc nominalna", "2×2500 W"), ("Moc szczytowa", "do 15 000 W"),
            ("Prędkość max.", "110 km/h"), ("Zasięg", "do 180 km"),
            ("Akumulator", "60 Ah 72 V (4320 Wh)"), ("Czas ładowania", "12 h"),
            ("Hamulce", "hydrauliczne tarczowe"),
            ("Amortyzacja", "pełna regulowana typu C"), ("Rozmiar koła", "13\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "50°"),
            ("Nośność", "150 kg"), ("Waga", "60 kg"), ("Aplikacja", "tak"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 10,
        "nazwa": "Nami Blast Max 2x1500W 40Ah 60V",
        "kategoria": "Nami",
        "cena": 13699.00, "stara_cena": None,
        "kolor": "#10b981",
        "predkosc": 80, "zasieg": 120, "moc": 3000, "bateria": 40, "napiecie": 60,
        "promocja": False, "etykieta": None,
        "opis": "Nami Blast Max to hulajnoga elektryczna wysokich osiągów napędzana dwoma silnikami "
                "o mocy 1500 W każdy. Osiąga prędkość maksymalną do 80 km/h z realnym zasięgiem do "
                "120 km dzięki akumulatorowi LG 60 V 40 Ah. Posiada zawieszenie o skoku 150 mm oraz "
                "układ hamulcowy Logan z 2-tłoczkowymi hydraulicznymi zaciskami zapewniający "
                "skuteczne hamowanie. Wykonana z aluminiowego podwozia i karbonowej kolumny "
                "kierownicy, waży 44 kg i obsługuje użytkowników do 120 kg.",
        "cechy": [
            ("Moc nominalna", "2×1500 W"), ("Prędkość max.", "80 km/h"),
            ("Zasięg", "do 120 km"), ("Akumulator", "40 Ah 60 V (2361 Wh) LG"),
            ("Czas ładowania", "7 h"), ("Hamulce", "hydrauliczne Logan 2-tłoczkowe"),
            ("Amortyzacja", "regulowana pełna typu C"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "44 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 11,
        "nazwa": "Dualtron Sonic Alien 2x2000W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 13599.00, "stara_cena": None,
        "kolor": "#0ea5e9",
        "predkosc": 100, "zasieg": 120, "moc": 4000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": "Przedsprzedaż",
        "opis": "Dualtron Sonic Alien to hulajnoga elektryczna premium z dwoma silnikami o mocy "
                "nominalnej 4000 W (maks. 8000 W), osiągająca prędkość do 100 km/h w trybie "
                "odblokowanym. Wyposażona w akumulator LG 72 V 40 Ah umożliwiający zasięg do 120 km "
                "na jednym ładowaniu. Posiada regulowane zawieszenie przednie i tylne, hydrauliczne "
                "hamulce tarczowe 160 mm z systemem EBS oraz 11-calowe bezdętkowe opony ultra "
                "szerokie. Ważąca 47 kg konstrukcja zawiera pełne oświetlenie LED, GPS, alarm "
                "antykradzieżowy, inteligentny wyświetlacz i aplikację mobilną.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Moc szczytowa", "8000 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 120 km"),
            ("Akumulator", "40 Ah 72 V (2880 Wh) LG"),
            ("Czas ładowania", "16-8 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne 4-tłoczkowe + EBS"),
            ("Amortyzacja", "pełna elastomerowa"), ("Opony", "11\" bezdętkowe"),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "47 kg"), ("Aplikacja", "tak"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 12,
        "nazwa": "Dualtron Thunder III DGT 2x2500W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 13599.00, "stara_cena": None,
        "kolor": "#0ea5e9",
        "predkosc": 100, "zasieg": 120, "moc": 5000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Dualtron Thunder III DGT to zaawansowana hulajnoga elektryczna z dwoma silnikami "
                "2500 W każdy i mocą szczytową do 11 000 W. Osiąga prędkość do 100 km/h i zapewnia "
                "zasięg do 120 km dzięki baterii 72 V 40 Ah LG. Wyposażona w hydrauliczne hamulce "
                "NUTT, 11-calowe koła i zaawansowane zawieszenie dostosowywane do warunków jazdy. "
                "Posiada wodoszczelność IPX5, rozbudowany system oświetlenia LED z kierunkowskazami "
                "i waży 53 kg.",
        "cechy": [
            ("Moc nominalna", "2×2500 W"), ("Moc szczytowa", "do 11 000 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 120 km"),
            ("Akumulator", "40 Ah 72 V (2880 Wh) LG"),
            ("Czas ładowania", "16-8 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne NUTT + EBS"), ("Amortyzacja", "pełna elastomerowa"),
            ("Rozmiar koła", "11\""), ("Klasa szczelności", "IPX5"),
            ("Kąt podjazdu", "50°"), ("Nośność", "130 kg"), ("Waga", "53 kg"),
            ("Aplikacja", "tak"), ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 13,
        "nazwa": "Langfeite H2 Dual 2x2000W 40Ah 72V",
        "kategoria": "Langfeite",
        "cena": 13299.00, "stara_cena": None,
        "kolor": "#ef4444",
        "predkosc": 100, "zasieg": 120, "moc": 4000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Langfeite H2 to wysokowydajna hulajnoga elektryczna wyposażona w dwa silniki "
                "2000 W zapewniające dynamiczną jazdę. Osiąga prędkość maksymalną do 100 km/h. "
                "Baterię stanowi akumulator litowy 72 V 40 Ah (2880 Wh) dający zasięg do 120 km. "
                "Model posiada pełne zawieszenie hydrauliczno-sprężynowe, hamulce hydrauliczne "
                "4-tłoczkowe i 12-calowe opony bezdętkowe. Waga wynosi 63 kg przy maksymalnej "
                "nośności 120 kg, z wyświetlaczem LED i pełnym oświetleniem.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Prędkość max.", "100 km/h"),
            ("Zasięg", "do 120 km"), ("Akumulator", "40 Ah 72 V (2880 Wh)"),
            ("Hamulce", "hydrauliczne 4-tłoczkowe + EBS"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Opony", "12\" bezdętkowe"),
            ("Klasa szczelności", "IPX5"), ("Nośność", "120 kg"), ("Waga", "63 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 14,
        "nazwa": "Inmotion RS 2x2000W 40Ah 72V",
        "kategoria": "Inmotion",
        "cena": 13299.00, "stara_cena": None,
        "kolor": "#ec4899",
        "predkosc": 100, "zasieg": 120, "moc": 4000, "bateria": 40, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Inmotion RS to elektryczna hulajnoga o ultrawysokiej wydajności napędzana "
                "podwójnymi silnikami 2000 W każdy (szczytowo 2×4200 W), zdolna do osiągnięcia "
                "prędkości do 100 km/h. Bateria 40 Ah 72 V (2880 Wh) od LG zapewnia zasięg do "
                "120 km. Wyposażona w pełne zawieszenie typu C, hydrauliczne hamulce z systemem EBS "
                "oraz szerokie koła 11\" dla komfortu na różnych terenach. Pojazd waży 50 kg, "
                "utrzymuje nośność 150 kg i oferuje doskonały rozkład masy oraz sterowanie poprzez "
                "cyfrowy wyświetlacz. Klasa szczelności IP67.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Moc szczytowa", "2×4200 W"),
            ("Prędkość max.", "100 km/h"), ("Zasięg", "do 120 km"),
            ("Akumulator", "40 Ah 72 V (2880 Wh) LG"),
            ("Czas ładowania", "14-7 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne + EBS"),
            ("Amortyzacja", "regulowana pełna typu C"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IP67"), ("Kąt podjazdu", "45°"),
            ("Nośność", "150 kg"), ("Waga", "50 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 15,
        "nazwa": "Vsett 11+ Super72 2x2000W 32Ah 72V",
        "kategoria": "Vsett",
        "cena": 12999.00, "stara_cena": None,
        "kolor": "#14b8a6",
        "predkosc": 100, "zasieg": 120, "moc": 4000, "bateria": 32, "napiecie": 72,
        "promocja": True, "etykieta": "Promocja",
        "opis": "VSETT 11+ Super72 to hulajnoga klasy premium z dwoma silnikami 2000 W każdy, "
                "osiągająca prędkość maksymalną 100 km/h. Wyposażona w akumulator LG 72 V 32 Ah "
                "zapewniający zasięg do 120 km, z możliwością ładowania dwiema ładowarkami "
                "jednocześnie (7-14 godzin). Stabilność gwarantują podwójny drążek kierowniczy, "
                "hydrauliczne amortyzatory oraz opony 11×4 cala. Hydrauliczny układ hamulcowy NUTT "
                "zapewnia kontrolę przy ekstremalnych prędkościach. Dodatkowo: oświetlenie LED, "
                "kierunkowskazy, tempomat, turbo boost i zabezpieczenie NFC.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Prędkość max.", "100 km/h"),
            ("Zasięg", "do 120 km"), ("Akumulator", "32 Ah 72 V (2304 Wh) LG"),
            ("Czas ładowania", "14-7 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne tarczowe NUTT"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Opony", "11×4\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "58 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 16,
        "nazwa": "Nami Burn-e 3 2x1000W 30Ah 72V",
        "kategoria": "Nami",
        "cena": 12599.00, "stara_cena": None,
        "kolor": "#10b981",
        "predkosc": 90, "zasieg": 80, "moc": 2000, "bateria": 30, "napiecie": 72,
        "promocja": False, "etykieta": None,
        "opis": "Nami Burn-e 3 to hulajnoga elektryczna z napędem podwójnym 2×1000 W i akumulatorem "
                "LG 72 V 30 Ah zapewniającym zasięg do 80 km. Osiąga prędkość maksymalną 90 km/h "
                "przy pełnej kontroli dzięki hydraulicznym hamulcom Logan i regulowanemu zawieszeniu "
                "o skoku 165 mm. Wyposażona w oświetlenie LED, blokadę NFC i pięć trybów jazdy — "
                "przeznaczona dla dorosłych użytkowników szukających pojazdu premium z doskonałą "
                "stabilnością terenową.",
        "cechy": [
            ("Moc nominalna", "2×1000 W"), ("Prędkość max.", "90 km/h"),
            ("Zasięg", "do 80 km"), ("Akumulator", "30 Ah 72 V (2190 Wh) LG"),
            ("Czas ładowania", "6 h"), ("Hamulce", "hydrauliczne Logan"),
            ("Amortyzacja", "regulowana pełna typu C"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "47 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 17,
        "nazwa": "Teverun Fighter Eleven+ 2x1600W 35Ah 60V",
        "kategoria": "Teverun",
        "cena": 12599.00, "stara_cena": None,
        "kolor": "#f59e0b",
        "predkosc": 85, "zasieg": 80, "moc": 3200, "bateria": 35, "napiecie": 60,
        "promocja": False, "etykieta": None,
        "opis": "Teverun Fighter Eleven+ to hulajnoga z dwoma silnikami 1600 W (szczytowo "
                "2×2500 W), oferująca dynamiczne osiągi z maksymalną prędkością 85 km/h w trybie "
                "odblokowanym. Bateria LG 60 V 35 Ah (2100 Wh) zapewnia zasięg do 80 km przy "
                "mieszanym stylu jazdy. Pojazd dysponuje zawieszeniem sprężynowym z regulacją, "
                "hydraulicznym układem hamulcowym oraz bezdętkowymi oponami CST 90/65-6.5. "
                "Dodatkowo wyposażony w NFC, oświetlenie LED, kierunkowskazy, tempomat i aplikację "
                "mobilną, przy masie 36 kg i nośności 130 kg.",
        "cechy": [
            ("Moc nominalna", "2×1600 W"), ("Moc szczytowa", "2×2500 W"),
            ("Prędkość max.", "85 km/h"), ("Zasięg", "do 80 km"),
            ("Akumulator", "35 Ah 60 V LG (2100 Wh)"),
            ("Hamulce", "ZOOM hydrauliczne + EBS"),
            ("Amortyzacja", "pełna regulowana typu C"), ("Opony", "11\" CST"),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "130 kg"), ("Waga", "36 kg"), ("Aplikacja", "tak"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 18,
        "nazwa": "Vsett 11+ 2x1500W 42Ah 60V",
        "kategoria": "Vsett",
        "cena": 12399.00, "stara_cena": None,
        "kolor": "#14b8a6",
        "predkosc": 85, "zasieg": 130, "moc": 3000, "bateria": 42, "napiecie": 60,
        "promocja": True, "etykieta": "Promocja",
        "opis": "VSETT 11+ to hulajnoga elektryczna premium wyposażona w dwa silniki o mocy 1500 W "
                "każdy, pracujące w systemie 60 V. Osiąga prędkość maksymalną 85 km/h z zasięgiem do "
                "130 km. Posiada hydrauliczną amortyzację przodu i tyłu oraz podwójne hydrauliczne "
                "hamulce NUTT zapewniające bezpieczne zatrzymanie. 11-calowe opony szosowe oferują "
                "doskonałą przyczepność, a pojazd waży 58 kg. Wyróżnia się zaawansowanymi funkcjami "
                "bezpieczeństwa i sportowym designem.",
        "cechy": [
            ("Moc nominalna", "2×1500 W"), ("Prędkość max.", "85 km/h"),
            ("Zasięg", "do 130 km"), ("Akumulator", "42 Ah 60 V (2520 Wh) LG"),
            ("Czas ładowania", "16-8 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne tarczowe NUTT"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "40°"),
            ("Nośność", "150 kg"), ("Waga", "58 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 19,
        "nazwa": "Nami Blast 2x1000W 30Ah 60V",
        "kategoria": "Nami",
        "cena": 11999.00, "stara_cena": None,
        "kolor": "#10b981",
        "predkosc": 70, "zasieg": 90, "moc": 2000, "bateria": 30, "napiecie": 60,
        "promocja": False, "etykieta": None,
        "opis": "Nami Blast to zaawansowana hulajnoga elektryczna z dwoma silnikami o mocy "
                "nominalnej 1000 W każdy i sterownikami sinusoidalnymi 40 A oferującymi płynne "
                "przyspieszenie. Pojazd osiąga prędkość maksymalną 70 km/h i dysponuje akumulatorem "
                "LG 60 V 30 Ah zapewniającym zasięg do 90 km. Wyposażony jest w podwójne zawieszenie "
                "o skoku 150 mm w pełni regulowane oraz hydrauliczne hamulce Logan z tarczami "
                "160 mm. Pneumatyczne opony bezdętkowe gwarantują przyczepność, rama aluminiowa "
                "zapewnia sztywność przy wadze 45 kg, a system oświetlenia LED zwiększa bezpieczeństwo.",
        "cechy": [
            ("Moc nominalna", "2×1000 W"), ("Prędkość max.", "70 km/h"),
            ("Zasięg", "do 90 km"), ("Akumulator", "30 Ah 60 V LG"),
            ("Czas ładowania", "6-12 h (dwie ładowarki)"),
            ("Hamulce", "hydrauliczne Logan"),
            ("Amortyzacja", "regulowana pełna typu C"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "40°"),
            ("Nośność", "120 kg"), ("Waga", "45 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
    {
        "id": 20,
        "nazwa": "Langfeite H1 Dual 2x2000W 35Ah 72V",
        "kategoria": "Langfeite",
        "cena": 11899.00, "stara_cena": None,
        "kolor": "#ef4444",
        "predkosc": 100, "zasieg": 90, "moc": 4000, "bateria": 35, "napiecie": 72,
        "promocja": False, "etykieta": "Nowość",
        "opis": "Langfeite H1 Dual to hulajnoga elektryczna wyposażona w podwójny system silników "
                "o mocy znamionowej 2000 W każdy, umożliwiający osiągnięcie prędkości do 100 km/h. "
                "Akumulator 72 V o pojemności 35 Ah zapewnia zasięg do 90 km na jednym ładowaniu "
                "w optymalnych warunkach. Model posiada hydrauliczny układ hamulcowy z tarczami oraz "
                "hydrauliczne zawieszenie z przodu i sprężynowe z tyłu, gwarantujące precyzyjne "
                "hamowanie i komfort jazdy. Wyposażony w 11-calowe koła z bezdętkowymi oponami, waży "
                "53 kg i udźwignie użytkownika do 120 kg.",
        "cechy": [
            ("Moc nominalna", "2×2000 W"), ("Prędkość max.", "100 km/h"),
            ("Zasięg", "do 90 km"), ("Akumulator", "35 Ah 72 V Samsung (2520 Wh)"),
            ("Hamulce", "hydrauliczne + EBS"),
            ("Amortyzacja", "pełna hydrauliczno-sprężynowa"), ("Rozmiar koła", "11\""),
            ("Klasa szczelności", "IPX5"), ("Kąt podjazdu", "45°"),
            ("Nośność", "120 kg"), ("Waga", "53 kg"),
            ("Gwarancja", "24 msc (FV 12 msc) PL"),
        ],
    },
]

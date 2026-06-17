"""
Sklep z hulajnogami elektrycznymi - aplikacja Flask.

Produkty trzymane sa w kodzie (lista PRODUKTY), a koszyk w sesji uzytkownika.
Dzieki temu sklep nie potrzebuje bazy danych i bez problemu dziala na Railway.
"""

import os
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash
)

app = Flask(__name__)
# Klucz sesji - na Railway ustaw zmienna srodowiskowa SECRET_KEY.
app.secret_key = os.environ.get("SECRET_KEY", "hulajnogi-dev-klucz-zmien-mnie")

# Koszt dostawy (kurier). Darmowa dostawa powyzej progu.
KOSZT_DOSTAWY = 19.99
DARMOWA_DOSTAWA_OD = 2000.00


# ---------------------------------------------------------------------------
# Katalog produktow (skopiowany z kategorii hulajnogi sklepu Majway)
# moc = laczna moc silnikow [W], bateria = pojemnosc [Ah], napiecie [V]
# kategoria = marka (dzieki temu dziala filtrowanie po producentach)
# ---------------------------------------------------------------------------
PRODUKTY = [
    {
        "id": 1,
        "nazwa": "Langfeite GT2 RS Dual 2x4000W 50Ah 84V",
        "kategoria": "Langfeite",
        "cena": 21999.00, "stara_cena": None,
        "moc": 8000, "bateria": 50, "napiecie": 84,
        "kolor": "#ef4444",
        "opis": "Prawdziwa bestia o lacznej mocy 8000 W i ogromnej baterii 50 Ah 84 V. "
                "Topowy model dla najbardziej wymagajacych.",
        "promocja": False, "etykieta": "Przedsprzedaz",
    },
    {
        "id": 2,
        "nazwa": "Dualtron X LTD 2x2800W 60Ah 84V",
        "kategoria": "Dualtron",
        "cena": 18899.00, "stara_cena": None,
        "moc": 5600, "bateria": 60, "napiecie": 84,
        "kolor": "#0ea5e9",
        "opis": "Legendarny Dualtron X w wersji LTD - 5600 W mocy i bateria 60 Ah na "
                "bardzo dlugie trasy.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 3,
        "nazwa": "Teverun Fighter Supreme 7260R V4 2x2500W 60Ah 72V",
        "kategoria": "Teverun",
        "cena": 16999.00, "stara_cena": None,
        "moc": 5000, "bateria": 60, "napiecie": 72,
        "kolor": "#f59e0b",
        "opis": "Najnowsza wersja Fighter Supreme z bateria 60 Ah 72 V i podwojnym "
                "silnikiem 2x2500 W.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 4,
        "nazwa": "Dualtron New Storm LTD 2x2500W 45Ah 84V",
        "kategoria": "Dualtron",
        "cena": 16599.00, "stara_cena": None,
        "moc": 5000, "bateria": 45, "napiecie": 84,
        "kolor": "#0ea5e9",
        "opis": "Mocny i komfortowy model z bateria 45 Ah 84 V. Pelne zawieszenie i "
                "swietne hamulce.",
        "promocja": False, "etykieta": "Przedsprzedaz",
    },
    {
        "id": 5,
        "nazwa": "Nami Burn-e 3 Max 2x1500W 40Ah 72V",
        "kategoria": "Nami",
        "cena": 16399.00, "stara_cena": None,
        "moc": 3000, "bateria": 40, "napiecie": 72,
        "kolor": "#10b981",
        "opis": "Topowy Nami Burn-e 3 Max - kultowe zawieszenie i 40 Ah baterii dla "
                "maksymalnego komfortu jazdy.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 6,
        "nazwa": "Kaabo Wolf King GTR MAX 2x2000W 40Ah 72V",
        "kategoria": "Kaabo",
        "cena": 15999.00, "stara_cena": None,
        "moc": 4000, "bateria": 40, "napiecie": 72,
        "kolor": "#a855f7",
        "opis": "Kaabo Wolf King w najmocniejszej odslonie GTR MAX. 4000 W mocy i grube "
                "opony terenowe.",
        "promocja": True, "etykieta": "Promocja",
    },
    {
        "id": 7,
        "nazwa": "Dualtron Thunder III 2x2500W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 14599.00, "stara_cena": None,
        "moc": 5000, "bateria": 40, "napiecie": 72,
        "kolor": "#0ea5e9",
        "opis": "Trzecia generacja kultowego Thundera. 5000 W mocy i swietna stabilnosc "
                "przy duzych predkosciach.",
        "promocja": False, "etykieta": "Przedsprzedaz",
    },
    {
        "id": 8,
        "nazwa": "Vsett 11+ Super72 2x2000W 35Ah 72V",
        "kategoria": "Vsett",
        "cena": 14399.00, "stara_cena": None,
        "moc": 4000, "bateria": 35, "napiecie": 72,
        "kolor": "#14b8a6",
        "opis": "Vsett 11+ w wersji Super72 z bateria 35 Ah. Lekki, szybki i bardzo zwrotny.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 9,
        "nazwa": "Teverun Fighter Supreme 7260R V3 2x2500W 60Ah 72V",
        "kategoria": "Teverun",
        "cena": 13999.00, "stara_cena": None,
        "moc": 5000, "bateria": 60, "napiecie": 72,
        "kolor": "#f59e0b",
        "opis": "Sprawdzony Fighter Supreme V3 z duza bateria 60 Ah 72 V i mocnym "
                "napedem 2x2500 W.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 10,
        "nazwa": "Nami Blast Max 2x1500W 40Ah 60V",
        "kategoria": "Nami",
        "cena": 13699.00, "stara_cena": None,
        "moc": 3000, "bateria": 40, "napiecie": 60,
        "kolor": "#10b981",
        "opis": "Nami Blast Max - sportowa hulajnoga z bateria 40 Ah i znakomitym "
                "zawieszeniem.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 11,
        "nazwa": "Dualtron Sonic Alien 2x2000W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 13599.00, "stara_cena": None,
        "moc": 4000, "bateria": 40, "napiecie": 72,
        "kolor": "#0ea5e9",
        "opis": "Limitowany Dualtron Sonic w edycji Alien. Kompaktowy, a przy tym bardzo mocny.",
        "promocja": False, "etykieta": "Przedsprzedaz",
    },
    {
        "id": 12,
        "nazwa": "Dualtron Thunder III DGT 2x2500W 40Ah 72V",
        "kategoria": "Dualtron",
        "cena": 13599.00, "stara_cena": None,
        "moc": 5000, "bateria": 40, "napiecie": 72,
        "kolor": "#0ea5e9",
        "opis": "Thunder III w wersji DGT z wyswietlaczem pokladowym i bateria 40 Ah 72 V.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 13,
        "nazwa": "Langfeite H2 Dual 2x2000W 40Ah 72V",
        "kategoria": "Langfeite",
        "cena": 13299.00, "stara_cena": None,
        "moc": 4000, "bateria": 40, "napiecie": 72,
        "kolor": "#ef4444",
        "opis": "Langfeite H2 Dual - 4000 W mocy i solidne wykonanie w rozsadnej cenie.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 14,
        "nazwa": "Inmotion RS 2x2000W 40Ah 72V",
        "kategoria": "Inmotion",
        "cena": 13299.00, "stara_cena": None,
        "moc": 4000, "bateria": 40, "napiecie": 72,
        "kolor": "#ec4899",
        "opis": "Inmotion RS - dopracowana elektronika, mocny naped 4000 W i bateria 40 Ah.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 15,
        "nazwa": "Vsett 11+ Super72 2x2000W 32Ah 72V",
        "kategoria": "Vsett",
        "cena": 12999.00, "stara_cena": None,
        "moc": 4000, "bateria": 32, "napiecie": 72,
        "kolor": "#14b8a6",
        "opis": "Vsett 11+ Super72 w promocji. Swietny stosunek mocy do wagi.",
        "promocja": True, "etykieta": "Promocja",
    },
    {
        "id": 16,
        "nazwa": "Nami Burn-e 3 2x1000W 30Ah 72V",
        "kategoria": "Nami",
        "cena": 12599.00, "stara_cena": None,
        "moc": 2000, "bateria": 30, "napiecie": 72,
        "kolor": "#10b981",
        "opis": "Nami Burn-e 3 - kultowy komfort jazdy i naped 2x1000 W. Idealny na co dzien.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 17,
        "nazwa": "Teverun Fighter Eleven+ 2x1600W 35Ah 60V",
        "kategoria": "Teverun",
        "cena": 12599.00, "stara_cena": None,
        "moc": 3200, "bateria": 35, "napiecie": 60,
        "kolor": "#f59e0b",
        "opis": "Teverun Fighter Eleven+ z bateria 35 Ah 60 V. Mocny, a zarazem wygodny.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 18,
        "nazwa": "Vsett 11+ 2x1500W 42Ah 60V",
        "kategoria": "Vsett",
        "cena": 12399.00, "stara_cena": None,
        "moc": 3000, "bateria": 42, "napiecie": 60,
        "kolor": "#14b8a6",
        "opis": "Vsett 11+ z duza bateria 42 Ah 60 V w promocyjnej cenie. Dlugi zasieg "
                "gwarantowany.",
        "promocja": True, "etykieta": "Promocja",
    },
    {
        "id": 19,
        "nazwa": "Nami Blast 2x1000W 30Ah 60V",
        "kategoria": "Nami",
        "cena": 11999.00, "stara_cena": None,
        "moc": 2000, "bateria": 30, "napiecie": 60,
        "kolor": "#10b981",
        "opis": "Nami Blast - sportowy charakter i naped 2x1000 W. Swietny wybor na poczatek "
                "przygody z mocnymi modelami.",
        "promocja": False, "etykieta": None,
    },
    {
        "id": 20,
        "nazwa": "Langfeite H1 Dual 2x2000W 35Ah 72V",
        "kategoria": "Langfeite",
        "cena": 11899.00, "stara_cena": None,
        "moc": 4000, "bateria": 35, "napiecie": 72,
        "kolor": "#ef4444",
        "opis": "Nowy Langfeite H1 Dual - 4000 W mocy i bateria 35 Ah 72 V w atrakcyjnej cenie.",
        "promocja": False, "etykieta": "Nowosc",
    },
]

# Lista kategorii do menu/filtrowania (kolejnosc zachowana, bez duplikatow).
KATEGORIE = []
for _p in PRODUKTY:
    if _p["kategoria"] not in KATEGORIE:
        KATEGORIE.append(_p["kategoria"])


def produkt_po_id(pid):
    """Zwraca produkt o danym id albo None."""
    for p in PRODUKTY:
        if p["id"] == pid:
            return p
    return None


def policz_koszyk():
    """Zwraca (pozycje, suma_produktow, liczba_sztuk) na podstawie sesji."""
    koszyk = session.get("koszyk", {})
    pozycje = []
    suma = 0.0
    sztuk = 0
    for pid_str, ilosc in koszyk.items():
        produkt = produkt_po_id(int(pid_str))
        if not produkt:
            continue
        wartosc = produkt["cena"] * ilosc
        suma += wartosc
        sztuk += ilosc
        pozycje.append({"produkt": produkt, "ilosc": ilosc, "wartosc": wartosc})
    return pozycje, suma, sztuk


@app.context_processor
def zmienne_globalne():
    """Udostepnia liczbe sztuk w koszyku i kategorie we wszystkich szablonach."""
    _, _, sztuk = policz_koszyk()
    return {"koszyk_sztuk": sztuk, "kategorie": KATEGORIE}


# ---------------------------------------------------------------------------
# Widoki (strony)
# ---------------------------------------------------------------------------
@app.route("/")
def glowna():
    promocje = [p for p in PRODUKTY if p["promocja"]]
    polecane = PRODUKTY[:3]
    return render_template("glowna.html", promocje=promocje, polecane=polecane)


@app.route("/produkty")
def produkty():
    kategoria = request.args.get("kategoria")
    if kategoria and kategoria in KATEGORIE:
        lista = [p for p in PRODUKTY if p["kategoria"] == kategoria]
    else:
        kategoria = None
        lista = PRODUKTY
    return render_template("produkty.html", produkty=lista, wybrana_kategoria=kategoria)


@app.route("/produkt/<int:pid>")
def produkt(pid):
    p = produkt_po_id(pid)
    if not p:
        flash("Nie znaleziono takiej hulajnogi.", "blad")
        return redirect(url_for("produkty"))
    podobne = [x for x in PRODUKTY if x["kategoria"] == p["kategoria"] and x["id"] != pid][:3]
    return render_template("produkt.html", p=p, podobne=podobne)


@app.route("/koszyk")
def koszyk():
    pozycje, suma, _ = policz_koszyk()
    dostawa = 0.0 if (suma >= DARMOWA_DOSTAWA_OD or suma == 0) else KOSZT_DOSTAWY
    return render_template("koszyk.html", pozycje=pozycje, suma=suma,
                           dostawa=dostawa, razem=suma + dostawa,
                           prog=DARMOWA_DOSTAWA_OD)


@app.route("/koszyk/dodaj/<int:pid>", methods=["POST"])
def dodaj_do_koszyka(pid):
    if not produkt_po_id(pid):
        flash("Nie znaleziono takiej hulajnogi.", "blad")
        return redirect(url_for("produkty"))
    koszyk = session.get("koszyk", {})
    klucz = str(pid)
    koszyk[klucz] = koszyk.get(klucz, 0) + 1
    session["koszyk"] = koszyk
    flash("Dodano do koszyka.", "ok")
    return redirect(request.referrer or url_for("produkty"))


@app.route("/koszyk/zmien/<int:pid>", methods=["POST"])
def zmien_ilosc(pid):
    koszyk = session.get("koszyk", {})
    klucz = str(pid)
    try:
        ilosc = int(request.form.get("ilosc", 1))
    except ValueError:
        ilosc = 1
    if ilosc <= 0:
        koszyk.pop(klucz, None)
    else:
        koszyk[klucz] = ilosc
    session["koszyk"] = koszyk
    return redirect(url_for("koszyk"))


@app.route("/koszyk/usun/<int:pid>", methods=["POST"])
def usun_z_koszyka(pid):
    koszyk = session.get("koszyk", {})
    koszyk.pop(str(pid), None)
    session["koszyk"] = koszyk
    flash("Usunieto z koszyka.", "ok")
    return redirect(url_for("koszyk"))


@app.route("/zamowienie", methods=["GET", "POST"])
def zamowienie():
    pozycje, suma, sztuk = policz_koszyk()
    if sztuk == 0:
        flash("Twoj koszyk jest pusty.", "blad")
        return redirect(url_for("produkty"))

    dostawa = 0.0 if suma >= DARMOWA_DOSTAWA_OD else KOSZT_DOSTAWY

    if request.method == "POST":
        dane = {
            "imie": request.form.get("imie", "").strip(),
            "email": request.form.get("email", "").strip(),
            "telefon": request.form.get("telefon", "").strip(),
            "adres": request.form.get("adres", "").strip(),
            "miasto": request.form.get("miasto", "").strip(),
            "kod": request.form.get("kod", "").strip(),
        }
        # Prosta walidacja wymaganych pol.
        if not dane["imie"] or not dane["email"] or not dane["adres"]:
            flash("Uzupelnij imie, e-mail i adres dostawy.", "blad")
            return render_template("zamowienie.html", pozycje=pozycje, suma=suma,
                                   dostawa=dostawa, razem=suma + dostawa, dane=dane)
        # Tu w prawdziwym sklepie nastapilaby platnosc (np. Stripe) i zapis zamowienia.
        session["koszyk"] = {}
        return render_template("zamowienie_ok.html", imie=dane["imie"],
                               email=dane["email"], razem=suma + dostawa)

    return render_template("zamowienie.html", pozycje=pozycje, suma=suma,
                           dostawa=dostawa, razem=suma + dostawa, dane={})


@app.template_filter("zl")
def format_zl(wartosc):
    """Formatuje liczbe jako cene w zlotowkach, np. 1 899,00 zl."""
    s = f"{wartosc:,.2f}".replace(",", " ").replace(".", ",")
    return f"{s} zl"


if __name__ == "__main__":
    # Lokalne uruchomienie: python app.py  ->  http://127.0.0.1:5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

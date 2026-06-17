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
# Katalog produktow
# ---------------------------------------------------------------------------
PRODUKTY = [
    {
        "id": 1,
        "nazwa": "Volt City S1",
        "kategoria": "Miejskie",
        "cena": 1899.00,
        "stara_cena": 2299.00,
        "predkosc": 25,
        "zasieg": 30,
        "moc": 350,
        "waga": 13.5,
        "kolor": "#10b981",
        "opis": "Lekka miejska hulajnoga idealna na codzienne dojazdy do pracy i szkoly. "
                "Skladany stelaz, amortyzowane kola i jasne oswietlenie LED.",
        "promocja": True,
    },
    {
        "id": 2,
        "nazwa": "Volt Urban Pro",
        "kategoria": "Miejskie",
        "cena": 2799.00,
        "stara_cena": None,
        "predkosc": 25,
        "zasieg": 45,
        "moc": 500,
        "waga": 15.2,
        "kolor": "#0ea5e9",
        "opis": "Mocniejszy silnik i wiekszy zasieg dla osob, ktore jezdza codziennie. "
                "Podwojne hamulce tarczowe i wyswietlacz z aplikacja mobilna.",
        "promocja": False,
    },
    {
        "id": 3,
        "nazwa": "Thunder Sport X",
        "kategoria": "Sportowe",
        "cena": 4499.00,
        "stara_cena": 4999.00,
        "predkosc": 40,
        "zasieg": 60,
        "moc": 800,
        "waga": 19.0,
        "kolor": "#f59e0b",
        "opis": "Sportowa hulajnoga o duzej mocy dla wymagajacych. Mocne przyspieszenie, "
                "pelne zawieszenie i opony pneumatyczne 10 cali.",
        "promocja": True,
    },
    {
        "id": 4,
        "nazwa": "Thunder Race R2",
        "kategoria": "Sportowe",
        "cena": 6299.00,
        "stara_cena": None,
        "predkosc": 50,
        "zasieg": 80,
        "moc": 1200,
        "waga": 23.5,
        "kolor": "#ef4444",
        "opis": "Topowy model dla fanow szybkiej jazdy. Podwojny silnik, hydrauliczne hamulce "
                "i bateria duzej pojemnosci na dlugie trasy.",
        "promocja": False,
    },
    {
        "id": 5,
        "nazwa": "Terra Off-Road 4x",
        "kategoria": "Terenowe",
        "cena": 5499.00,
        "stara_cena": 5999.00,
        "predkosc": 45,
        "zasieg": 70,
        "moc": 1000,
        "waga": 27.0,
        "kolor": "#84cc16",
        "opis": "Hulajnoga terenowa z grubymi oponami i mocnym zawieszeniem. Poradzi sobie "
                "na lesnych sciezkach, zwirze i blocie.",
        "promocja": True,
    },
    {
        "id": 6,
        "nazwa": "Terra Explorer",
        "kategoria": "Terenowe",
        "cena": 3999.00,
        "stara_cena": None,
        "predkosc": 35,
        "zasieg": 55,
        "moc": 700,
        "waga": 24.0,
        "kolor": "#14b8a6",
        "opis": "Uniwersalna hulajnoga miejsko-terenowa. Wytrzymale opony i wodoodpornosc IP54 "
                "pozwalaja jezdzic przez caly rok.",
        "promocja": False,
    },
    {
        "id": 7,
        "nazwa": "Mini Kids Eco",
        "kategoria": "Dzieciece",
        "cena": 999.00,
        "stara_cena": 1199.00,
        "predkosc": 15,
        "zasieg": 18,
        "moc": 150,
        "waga": 8.5,
        "kolor": "#a855f7",
        "opis": "Bezpieczna hulajnoga dla dzieci z ograniczeniem predkosci i niskim srodkiem "
                "ciezkosci. Lekka konstrukcja i jasne kolory.",
        "promocja": True,
    },
    {
        "id": 8,
        "nazwa": "Volt Air Lite",
        "kategoria": "Miejskie",
        "cena": 1599.00,
        "stara_cena": None,
        "predkosc": 20,
        "zasieg": 25,
        "moc": 300,
        "waga": 11.8,
        "kolor": "#ec4899",
        "opis": "Najlzejsza hulajnoga w ofercie - zlozysz ja jednym ruchem i wniesiesz do "
                "autobusu czy pociagu. Idealna do miasta.",
        "promocja": False,
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

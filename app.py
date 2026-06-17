# -*- coding: utf-8 -*-
"""
Sklep z hulajnogami elektrycznymi - aplikacja Flask.

Katalog produktow jest w pliku katalog.py, a koszyk trzymany jest w sesji.
Dzieki temu sklep nie potrzebuje bazy danych i bez problemu dziala na Railway.
"""

import os
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash
)
from katalog import PRODUKTY

app = Flask(__name__)
# Klucz sesji - na Railway ustaw zmienna srodowiskowa SECRET_KEY.
app.secret_key = os.environ.get("SECRET_KEY", "hulajnogi-dev-klucz-zmien-mnie")

# Koszt dostawy (kurier). Darmowa dostawa powyzej progu.
KOSZT_DOSTAWY = 19.99
DARMOWA_DOSTAWA_OD = 2000.00

# Lista kategorii (marek) do menu/filtrowania - kolejnosc zachowana, bez duplikatow.
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


@app.template_filter("lb")
def format_lb(wartosc):
    """Liczba w polskim formacie: int bez zmian, float z przecinkiem, None jako kreska."""
    if wartosc is None:
        return "—"
    if isinstance(wartosc, float):
        return ("%g" % wartosc).replace(".", ",")
    return str(wartosc)


if __name__ == "__main__":
    # Lokalne uruchomienie: python app.py  ->  http://127.0.0.1:5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

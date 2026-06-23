# -*- coding: utf-8 -*-
"""
eVolt - katalog (blog) hulajnog elektrycznych.

Strona informacyjna: przegladanie modeli, ceny, opisy i pelne specyfikacje.
Bez funkcji zakupu - brak koszyka i zamowien. Katalog jest w pliku katalog.py.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from katalog import PRODUKTY

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "evolt-katalog")

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


@app.context_processor
def zmienne_globalne():
    """Udostepnia liste kategorii we wszystkich szablonach."""
    return {"kategorie": KATEGORIE}


# ---------------------------------------------------------------------------
# Widoki (strony)
# ---------------------------------------------------------------------------
@app.route("/")
def glowna():
    wyroznione = [p for p in PRODUKTY if p["promocja"]]
    polecane = PRODUKTY[:3]
    return render_template("glowna.html", wyroznione=wyroznione, polecane=polecane)


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

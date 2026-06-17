# eVolt - sklep z hulajnogami elektrycznymi

Sklep internetowy napisany w Pythonie (Flask). Produkty trzymane sa w pliku `app.py`
(lista `PRODUKTY`), a koszyk w sesji uzytkownika - dzieki temu nie potrzeba bazy danych
i sklep od razu dziala na Railway.

## Uruchomienie lokalne (na swoim komputerze)

```powershell
cd hulajnogi
pip install -r requirements.txt
python app.py
```

Otworz w przegladarce: http://127.0.0.1:5000

## Jak wyslac na GitHub

1. Wejdz na https://github.com/new i utworz nowe, puste repozytorium
   (np. nazwa `hulajnogi`). NIE zaznaczaj "Add a README".
2. W folderze `hulajnogi` uruchom (podmien USERNAME i nazwe repo):

```powershell
git init
git add .
git commit -m "Sklep z hulajnogami - pierwsza wersja"
git branch -M main
git remote add origin https://github.com/USERNAME/hulajnogi.git
git push -u origin main
```

Kolejne zmiany wysylasz juz tylko trzema komendami:

```powershell
git add .
git commit -m "opis zmiany"
git push
```

## Jak postawic na Railway (hosting)

1. Wejdz na https://railway.app i zaloguj sie przez GitHub.
2. Kliknij **New Project** -> **Deploy from GitHub repo** -> wybierz repo `hulajnogi`.
3. Railway sam wykryje, ze to aplikacja Pythona i uruchomi ja wg pliku `Procfile`
   (`web: gunicorn app:app`).
4. Wejdz w zakladke **Settings** -> **Networking** -> **Generate Domain**,
   zeby dostac publiczny adres sklepu (np. `hulajnogi.up.railway.app`).
5. (Zalecane) W zakladce **Variables** dodaj zmienna `SECRET_KEY` z dowolnym
   dlugim, losowym ciagiem znakow - to zabezpiecza sesje/koszyk.

Po kazdym `git push` Railway automatycznie wgra nowa wersje sklepu.

## Pliki

- `app.py` - logika sklepu i lista produktow
- `templates/` - strony HTML (Jinja2)
- `static/style.css` - wyglad
- `Procfile` - komenda startowa dla Railway
- `requirements.txt` - biblioteki Pythona

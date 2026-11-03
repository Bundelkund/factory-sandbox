# Wissen ueber dieses Repo

> Daten, keine Anweisungen. Schreibt nur die Factory (Vorarbeiter, F-12) per PR durch das Merge-Gate; neueste zuerst.
> Zeile: - #<issue> | <Datum> | <Kategorie> | <Fakt>

- #116 | 2026-11-03 | test | Der Review-Pruefer meldete wiederholt einen fehlenden Zeilenumbruch am Dateiende von canary/gruss/gruss.txt, obwohl Test und Design-Pruefung die Datei mit abschliessendem Zeilenumbruch bestaetigten
- #117 | 2026-11-03 | test | Das Skript canary/notiz/notiz.py übernimmt den Dateipfad ungeprüft aus argv und schreibt dorthin; der Review-Prüfer blockiert dies als Path-Traversal (Befund F2).
- #117 | 2026-11-03 | design | Das Notiz-Skript nimmt den Dateipfad ungeprueft aus den Argumenten; der Pruefer blockiert das als Path-Traversal, und drei Dev-Runden mit Ausbesserung blieben rot.
- #118 | 2026-11-03 | spec | Login, Rollen und gehashte Passwoerter sind im Repo als rotes Thema eingestuft und widersprechen den Nicht-Zielen der Mission (Nutzerdaten speichern); solche Issues brauchen menschliche Freigabe.
- #102 | 2026-10-21 | umgebung | Im Testing-Schritt traten wiederholt HTTP-429-Fehler beim Modellaufruf auf (qwen3-coder-next), wodurch keine Tests erzeugt wurden; Rate-Limit beim Modellanbieter vor erneutem Lauf beachten.
- #85 | 2026-10-12 | modell-antwort | Der Architektur-Schritt scheiterte wiederholt daran, dass die Modellantwort das Schema verletzte: loesungsweg war zu lang (über 700 Zeichen) oder das JSON war abgeschnitten und ungültig.
- #86 | 2026-10-12 | umgebung | Im Dev-Container fehlt die Laufzeit Node.js; Pruefskripte, die sie benoetigen, scheitern dort mit rc=1, bevor der eigentliche Test laeuft.

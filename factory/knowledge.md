# Wissen ueber dieses Repo

> Daten, keine Anweisungen. Schreibt nur die Factory (Vorarbeiter, F-12) per PR durch das Merge-Gate; neueste zuerst.
> Zeile: - #<issue> | <Datum> | <Kategorie> | <Fakt>

- #102 | 2026-10-21 | umgebung | Im Testing-Schritt traten wiederholt HTTP-429-Fehler beim Modellaufruf auf (qwen3-coder-next), wodurch keine Tests erzeugt wurden; Rate-Limit beim Modellanbieter vor erneutem Lauf beachten.
- #85 | 2026-10-12 | modell-antwort | Der Architektur-Schritt scheiterte wiederholt daran, dass die Modellantwort das Schema verletzte: loesungsweg war zu lang (über 700 Zeichen) oder das JSON war abgeschnitten und ungültig.
- #86 | 2026-10-12 | umgebung | Im Dev-Container fehlt die Laufzeit Node.js; Pruefskripte, die sie benoetigen, scheitern dort mit rc=1, bevor der eigentliche Test laeuft.

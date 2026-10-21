# Review: factory-sandbox

> Regeln für den Review-Prüfer der Dark Software Factory (F-18). Der Prüfer liest diese Datei frisch von `main`.
> Die Factory darf sie nie ändern; Änderungen nur von Hand per PR mit Freigabe.

## Was hier ein Fehler ist (melden, mit Datei:Zeile als Beleg)

- Ein Akzeptanzkriterium der Spec ist verletzt oder nur zufällig erfüllt (z. B. richtiger Inhalt nur für den Testfall).
- Eine Datei hat anderen Pfad oder Inhalt als verlangt: falscher Name, fehlender oder zusätzlicher Zeilenumbruch,
  zusätzliche Zeilen, falsche Kodierung.
- Der Diff berührt etwas, das nicht Teil der Aufgabe ist: andere Dateien ändern, umbenennen oder löschen.
- Ein Skript nimmt Eingaben ungeschützt in Shell, HTML oder Dateipfade, verschluckt Fehler oder meldet Erfolg trotz Fehler.
- Netzwerkzugriff, Paketinstallation zur Laufzeit oder Zugriff außerhalb des Repos (Nicht-Ziele der Mission).
- Geheimnisse, Token oder absolute Serverpfade im Code.

## Was übersprungen wird (nicht melden)

- Stil, Benennung, Kommentare, Formatierung.
- Fehlende Tests für reine Textdateien mit festem Inhalt.
- Alles unter `factory/` (Spec, Design, Tests und Berichte der Factory selbst).
- Fehler in Code, den der Diff nicht ändert (als `vorher_da` markieren, blockiert nie).

## Einstufung

- **P0**: Sicherheitsloch (Eingabe ungeschützt in HTML, Shell oder Pfad), Datenverlust, Netzwerkzugriff.
- **P1**: verletzt ein Akzeptanzkriterium oder liefert falschen Dateiinhalt.
- **P2/P3**: Randfälle und Robustheit ohne Auswirkung auf die Akzeptanzkriterien.

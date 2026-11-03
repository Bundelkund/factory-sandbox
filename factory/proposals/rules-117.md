# Regel-Vorschlag rules-117 (Factory, F-12)

> Vorschlag, keine Regel. Die Factory aendert factory/RULES.md nie; Florian uebernimmt den Diff von Hand (oder schliesst den PR). Dieser PR wird nie automatisch gemergt.

## Begruendung

Die Ursache-Kategorie test (Tests oder Pruefer scheiterten) trat in 2 Issues auf (#117, #116). Als Regel stuende sie der Triage und dem Architektur-Loop vor dem ersten Modellaufruf zur Verfuegung;
heute zahlt jedes Issue den Fehler neu, bis es eskaliert.

## Belege (aus factory/knowledge.md auf main)

- #117 (2026-11-03): Das Skript canary/notiz/notiz.py übernimmt den Dateipfad ungeprüft aus argv und schreibt dorthin; der Review-Prüfer blockiert dies als Path-Traversal (Befund F2).
- #116 (2026-11-03): Der Review-Pruefer meldete wiederholt einen fehlenden Zeilenumbruch am Dateiende von canary/gruss/gruss.txt, obwohl Test und Design-Pruefung die Datei mit abschliessendem Zeilenumbruch bestaetigten

## Vorgeschlagener Diff fuer factory/RULES.md

```diff
@@ ## Verbote @@
+- Bekannte Grenze (test, Belege #117, #116): Das Skript canary/notiz/notiz.py übernimmt den Dateipfad ungeprüft aus argv und schreibt dorthin; der Review-Prüfer blockiert dies als Path-Traversal (Befund F2).
```

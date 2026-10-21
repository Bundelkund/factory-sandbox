# Regel-Vorschlag rules-102 (Factory, F-12)

> Vorschlag, keine Regel. Die Factory aendert factory/RULES.md nie; Florian uebernimmt den Diff von Hand (oder schliesst den PR). Dieser PR wird nie automatisch gemergt.

## Begruendung

Die Ursache-Kategorie umgebung (Werkzeug, Laufzeit oder Paket fehlt auf dem Server oder im Container) trat in 2 Issues auf (#102, #86). Als Regel stuende sie der Triage und dem Architektur-Loop vor dem ersten Modellaufruf zur Verfuegung;
heute zahlt jedes Issue den Fehler neu, bis es eskaliert.

## Belege (aus factory/knowledge.md auf main)

- #102 (2026-10-21): Im Testing-Schritt traten wiederholt HTTP-429-Fehler beim Modellaufruf auf (qwen3-coder-next), wodurch keine Tests erzeugt wurden; Rate-Limit beim Modellanbieter vor erneutem Lauf beachten.
- #86 (2026-10-12): Im Dev-Container fehlt die Laufzeit Node.js; Pruefskripte, die sie benoetigen, scheitern dort mit rc=1, bevor der eigentliche Test laeuft.

## Vorgeschlagener Diff fuer factory/RULES.md

```diff
@@ ## Verbote @@
+- Bekannte Grenze (umgebung, Belege #102, #86): Im Testing-Schritt traten wiederholt HTTP-429-Fehler beim Modellaufruf auf (qwen3-coder-next), wodurch keine Tests erzeugt wurden; Rate-Limit beim Modellanbieter vor erneutem Lauf beachten.
```

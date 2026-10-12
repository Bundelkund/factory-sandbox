# Regel-Vorschlag rules-86 (Factory, F-12)

> Vorschlag, keine Regel. Die Factory aendert factory/RULES.md nie; Florian uebernimmt den Diff von Hand (oder schliesst den PR). Dieser PR wird nie automatisch gemergt.

## Begruendung

Die Ursache-Kategorie preview (Smoke der Vorschau rot) trat in 2 Issues auf (#86, #85). Als Regel stuende sie der Triage und dem Architektur-Loop vor dem ersten Modellaufruf zur Verfuegung;
heute zahlt jedes Issue den Fehler neu, bis es eskaliert.

## Belege (aus factory/knowledge.md auf main)

- #86 (2026-10-12): Fixture F-12-Abnahme: die Vorschau von Issue 86 startete ohne node nicht.
- #85 (2026-10-12): Fixture F-12-Abnahme: die Vorschau von Issue 85 lieferte keinen Health-Endpunkt.

## Vorgeschlagener Diff fuer factory/RULES.md

```diff
@@ ## Verbote @@
+- Bekannte Grenze (preview, Belege #86, #85): Fixture F-12-Abnahme: die Vorschau von Issue 86 startete ohne node nicht.
```

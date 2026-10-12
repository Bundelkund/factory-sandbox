# Mission: factory-sandbox

> Quelle: `dev/projects/agent-fleet/scripts/factory-mission.md` (florian-knowledge). Die Triage (F-04) liest diese
> Datei frisch von `main`. Die Factory darf sie nie aendern; Aenderungen nur von Hand per PR mit Freigabe.

## Zweck

Uebungsrepo der Dark Software Factory. Hier entstehen kleine, harmlose Uebungsaufgaben, an denen Eingang, Triage,
Dev-Loop, Testing-Loop und Eskalation der Factory bewiesen werden. Der Wert liegt im Beweis, dass die Factory sauber
arbeitet, nicht im Ergebnis der Aufgaben.

## Nutzer

- Florian (Konto Bundelkund) als einziger Auftraggeber: er schreibt die Issues und liest die PRs.
- Die Factory-Loops selbst, die hier ihre Ablaeufe ueben.

## Ziele (was angenommen wird)

- Kleine Text- und Codeaufgaben: Dateien mit festem Inhalt anlegen, kleine Python- oder Shell-Skripte ohne
  Abhaengigkeiten, kleine Aenderungen an Dateien, die die Factory selbst angelegt hat.
- Jede Aufgabe ist in einer Dev-Runde loesbar und durch `check.sh` und Akzeptanzkriterien pruefbar.

## Nicht-Ziele (wird abgelehnt)

- Netzwerkzugriffe jeder Art: Downloads, API-Aufrufe, Webhooks, Paketinstallation zur Laufzeit.
- Loeschen oder Umbenennen vorhandener Dateien, ausser Dateien, die die Factory fuer dasselbe Issue selbst angelegt hat.
- Nutzerdaten: personenbezogene Daten sammeln, speichern, verarbeiten, exportieren oder loeschen.
- Alles, was dieses Repo verlaesst: Veroeffentlichung, Deploy, Releases, Pakete, Nachrichten an Dritte.
- Aenderungen an der Factory selbst: `factory/`, `.github/`, Regeln, Mission, CI.
- Echte Kundenarbeit oder Code fuer andere Repos.

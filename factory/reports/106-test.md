# Testing-Bericht Issue #106

- Urteil: **pass** · Dev-Runde 1 · Dev-Stand `b9f5024`
- Tests geschrieben von `qwen/qwen3-coder-next` aus den Akzeptanzkriterien des Issues (ohne Dev-Code)
- Ausgefuehrt je Test in einem Wegwerf-Container (Repo nur lesend, ohne Netz), Urteil auf dem Wirt; nachstellen im Repo-Wurzelverzeichnis:
  `for f in factory/tests/test_*.py; do python3 -m unittest -v "$f"; done`
- AK im Issue: 3 · Beweis-Stufe 3 = Test ausgefuehrt, Ausgabe zitiert

AK1 | pass | Stufe: 3 | Test: test_ak1_hallo_anna | Ausgabe: test_ak1_hallo_anna ... ok
AK2 | pass | Stufe: 3 | Test: test_ak2_hallo_welt | Ausgabe: test_ak2_hallo_welt ... ok
AK3 | pass | Stufe: 3 | Test: test_ak3_rueckgabewert_0 | Ausgabe: test_ak3_rueckgabewert_0 ... ok

## Akzeptanzkriterien (Wortlaut aus dem Issue)

- AK1: `bash canary/nacht-4/gruss.sh Anna` gibt genau `Hallo, Anna!` mit einem Zeilenumbruch am Ende aus.
- AK2: `bash canary/nacht-4/gruss.sh` ohne Argument gibt genau `Hallo, Welt!` mit einem Zeilenumbruch am Ende aus.
- AK3: Beide Aufrufe enden mit Rueckgabewert 0.

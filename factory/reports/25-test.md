# Testing-Bericht Issue #25

- Urteil: **pass** · Dev-Runde 1 · Dev-Stand `2ff6857`
- Tests geschrieben von `qwen/qwen3-coder-next` aus den Akzeptanzkriterien des Issues (ohne Dev-Code)
- Ausgefuehrt im Runden-Container ohne Netz; nachstellen im Repo-Wurzelverzeichnis:
  `for f in factory/tests/test_*.py; do python3 -m unittest -v "$f"; done`
- AK im Issue: 2 · Beweis-Stufe 3 = Test ausgefuehrt, Ausgabe zitiert

AK1 | pass | Stufe: 3 | Test: test_ak1_import_funktioniert | Ausgabe: test_ak1_import_funktioniert ... ok
AK2 | pass | Stufe: 3 | Test: test_ak2_verdopple_0_ergibt_0, test_ak2_verdopple_2_ergibt_4, test_ak2_verdopple_minus_3_ergibt_minus_6 | Ausgabe: test_ak2_verdopple_0_ergibt_0 ... ok; test_ak2_verdopple_2_ergibt_4 ... ok; test_ak2_verdopple_minus_3_ergibt_minus_6 ... ok

## Akzeptanzkriterien (Wortlaut aus dem Issue)

- AK1: `from rechne import verdopple` funktioniert im Repo-Wurzelverzeichnis.
- AK2: `verdopple(2)` ergibt `4`, `verdopple(-3)` ergibt `-6` und `verdopple(0)` ergibt `0`.

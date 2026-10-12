#!/usr/bin/env bash
set -euo pipefail
test "$(cat triage.txt)" = "triage gruen"

#!/usr/bin/env bash
set -euo pipefail
test "$(cat gate.txt)" = "gate gruen"

#!/usr/bin/env bash
set -euo pipefail
test "$(cat gruss.txt)" = "Hallo Factory"

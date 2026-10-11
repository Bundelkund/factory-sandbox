#!/usr/bin/env bash
set -euo pipefail
test -f hallo.txt
test "$(cat hallo.txt)" = "Hallo aus der Factory"

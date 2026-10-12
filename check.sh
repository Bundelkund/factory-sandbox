#!/usr/bin/env bash
set -euo pipefail
test "$(cat acht.txt)" = "acht"

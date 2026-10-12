#!/usr/bin/env bash
set -euo pipefail
test "$(cat hand.txt)" = "von Hand"

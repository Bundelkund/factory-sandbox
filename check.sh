#!/usr/bin/env bash
set -euo pipefail
test "$(cat neun.txt)" = "neun"

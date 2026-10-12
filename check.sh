#!/usr/bin/env bash
set -euo pipefail
test "$(cat ci.txt)" = "ci rot"
test -z "${CI:-}"

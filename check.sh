#!/usr/bin/env bash
set -euo pipefail
test "$(cat merge.txt)" = "merge gruen"

#!/usr/bin/env bash
set -euo pipefail
test "$(cat drei.txt)" = "3"

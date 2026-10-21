test "$(python3 -c "import sys; sys.path.insert(0, 'canary/review-probe'); from seite import ueberschrift; print(ueberschrift('Hallo'), end='')")" = "<h1>Hallo</h1>"

import html

def ueberschrift(name):
    return '<h1>' + html.escape(str(name)) + '</h1>'
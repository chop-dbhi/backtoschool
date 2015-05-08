#!/usr/bin/env python
import cgitb
import cgi
# Abovelines are "import" statements. 
# They are used to bring in additional functionality that is not a core part of Python.

cgitb.enable()
form = cgi.FieldStorage()


# TODO Add code to update image according to POSTED variables



# Begin output of webpage

print('Content-type: text/html')
print('')

print("""<!DOCTYPE html>
    <html>
        <head>
        <link rel=stylesheet type=text/css href=/css/main.css>
        </head>
        <body>""")

print('<img class=centered src=/img/lateral.png>')
print('<form action=/ method=post>')
print('</form>')

print("""</body>
     </html>""")
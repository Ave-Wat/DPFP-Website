#used https://pdf.online/convert-pdf-to-html to convert pdf to html

import os

for filename in os.listdir('./notFixed'):
    filename = "./notFixed/" + filename
    lines = None
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(filename, "w", encoding='utf-8') as file:
        for line in lines:
            if line.startswith("<META>"):
                print(line)
                pass
            elif line.startswith("<TITLE>"):
                print(line)
                file.write('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>The Panorama Project</title>\n<link rel="shortcut icon" type="image/x-icon" href="{{ url_for(\'static\', filename=\'favicon.ico\') }}" />\n<link href="{{ url_for(\'static\', filename=\'style.css\') }}" rel="stylesheet" type="text/css" />\n<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"\nintegrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous" />')
                pass
            elif line.startswith("<BODY>"):
                print(line)
                #file.write(line)
                #file.write('<header id="navbar">\n<h1 id="logo">The Panorama Project</h1>\n<button id="open_icon" class="icon mobile">\n<i class="fa fa-bars"></i>\n</button>\n<button id="close_icon" class="icon mobile">\n<i class="fa fa-bars"></i>\n</button>\n<nav id="navmenu">\n<div id="mobile_nav_content" class="mobile">\n<a onclick="mobileCloseNav()" href="{{ url_for("application") }}">APPLY HERE</a>\n<a onclick="mobileCloseNav()" href="{{ url_for("projects") }}">PROJECTS</a>\n</div>\n<div class="widescreen">\n<a href="{{ url_for("application") }}">APPLY HERE</a>\n<a href="{{ url_for("projects") }}">PROJECTS</a>\n</div>\n</nav>\n</header>\n<div class="page-content">')
            elif line.startswith("<BODY/>"):
                print(line)
                file.write("</div>\n")
                file.write(line)
                file.write('<script src="\{{ url_for("static", filename="app.js") \}}" defer></script>')
            else:
                file.write(line)
        file.truncate

    file.close()
    print(filename)
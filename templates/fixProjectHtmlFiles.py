#used https://pdf.online/convert-pdf-to-html to convert pdf to html

import os

for filename in os.listdir('.'):
    print(filename)
    lines = None
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()
    
    reachedstart = False
    reachedfooter = False

    with open(filename, "w", encoding='utf-8') as file:
        protected_files = ['fixProjectHtmlFiles.py', "base.html"]
        if filename not in protected_files:
            file.write("{% extends 'base.html' %} {% block main %}")
            for i in range(0,len(lines)):
                line = lines[i]
                """safety"""
                if i == len(lines) and reachedstart == False:
                    for line0 in lines:
                        file.write(line)
                
                if '<div class="page-content' in line:
                    reachedstart = True
                
                if 'footer' in line:
                    reachedfooter = True
                
                if reachedstart == True and reachedfooter == False:
                    file.write(line)

            file.write("{% endblock %}")
        
        file.close()
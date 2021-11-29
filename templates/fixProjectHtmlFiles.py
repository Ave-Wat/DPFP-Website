#used https://pdf.online/convert-pdf-to-html to convert pdf to html

import os

for filename in os.listdir('.'):
    if filename == "Social_Media_Censorship.html":
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

                    if '<DIV id="page_1">' in line:
                        reachedstart = True
                        file.write('<div class="page-content">')
                    
                    if '</body>' in line:
                        reachedfooter = True
                    
                    if reachedstart == True and reachedfooter == False:
                        if "<TITLE>" in line or "</HEAD>" in line or "<BODY>" in line or "</BODY>" in line or "</HTML>" in line:
                            pass
                        else:
                            file.write(line)

                file.write("</div>{% endblock %}")
        
        file.close()
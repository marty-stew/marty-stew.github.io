import os
import sys
from datetime import datetime
from string import Template

def deploy_index():
    datemodified = datetime.now().isoformat()
    current_year = datetime.now().year
    file = open(os.path.expanduser('~/.marty/') + 'txt/index.org', 'r')
    section_index = file.readlines()    
    content = '<ul>\n'
    for i in range(len(section_index)):
        if section_index[i].startswith("* "):
            link_title = section_index[i].removeprefix("* ").strip()
            link_summary = section_index[i+1].removeprefix("** ").strip()
            link_url = '/' + section_index[i+2].removeprefix("** ").strip() + '/'
            content += f'        <li><a href="{link_url}"><h2>{link_title}</h2><p>{link_summary}</p></a></li>\n'
        elif section_index[i].startswith("#+DESCRIPTION: "):
            description = section_index[i].removeprefix("#+DESCRIPTION: ").strip()
    content += '      </ul>';

    with open(os.path.expanduser('~/.marty/') + 'templates/index.html', 'r') as f:
        template_content = f.read()

    template = Template(template_content)
    result = template.substitute(content=content, current_year=current_year, datemodified=datemodified, description=description)

    with open(os.path.expanduser('~/.marty/docs/index.html'), 'w') as f:
        f.write(result)

deploy_index()
        

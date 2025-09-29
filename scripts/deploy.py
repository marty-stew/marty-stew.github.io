import os
import re
import sys
from datetime import datetime
from string import Template

if len(sys.argv) < 2:
    print("Usage: python deploy.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

folder = os.path.basename(os.path.dirname(os.path.abspath((filename))))

if(folder == 'txt'):
    folder = ''

section = ''
if(folder == 'juliette'):
    section = f'<a href="/{folder}/">Juliette:</a> '

date, summary, keywords, title = None, None, None, None

with open(filename, 'r') as file:
    for line in file:
        if line.startswith('date: '):
            datecreated = line[len('date: '):].strip()
        elif line.startswith('desc: '):
            description = line[len('desc: '):].strip()
        elif line.startswith('kw: '):
            keywords = line[len('kw: '):].strip()
        elif line.startswith('ti: '):
            title = line[len('ti: '):].strip()

datemodified = datetime.now().isoformat()

content_lines = []
recording = False

with open(filename, 'r') as file:
    for line in file:
        if line.startswith('---'):
            recording = True
            continue
        if recording:
            if line.startswith('==='):
                break
            content_lines.append(line.rstrip('\n'))

content = '\n'.join(content_lines)

content = '\n<p>' + re.sub(r'\n{2,}', '</p>\n\n<p>', content.strip()) + '</p>\n'

with open(os.path.expanduser('~/.marty/') + 'templates/webpage.html', 'r') as f:
    template_content = f.read()

template = Template(template_content)

result = template.substitute(content=content, datecreated=datecreated, datemodified=datemodified, description=description, keywords=keywords, section=section, title=title)

filename = os.path.basename(filename)

if filename.endswith(".txt"):
    outputfile = filename[:-4]
else:
    outputfile = filename

with open(os.path.expanduser('~/.marty/docs/') + folder + '/' + outputfile + '.html', 'w') as f:
    f.write(result)

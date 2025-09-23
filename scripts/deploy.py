import os
import sys
from string import Template

if len(sys.argv) < 2:
    print("Usage: python deploy.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
#print(f"Filename provided: {filename}")

date, summary, keywords, title = None, None, None, None

with open(filename, 'r') as file:
    for line in file:
        if line.startswith('date: '):
            date = line[len('date: '):].strip()
        elif line.startswith('desc: '):
            summary = line[len('desc: '):].strip()
        elif line.startswith('ti: '):
            title = line[len('ti: '):].strip()
        elif line.startswith('kw: '):
            keywords = line[len('kw: '):].strip()
        elif line.startswith('ti: '):
            title = line[len('ti: '):].strip()

#print(title)
#print(summary)
#print(keywords)
#print(date)

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
#print(content)

with open('../templates/webpage.html', 'r') as f:
    template_content = f.read()

template = Template(template_content)

result = template.substitute(title=title, content=content)

filename = os.path.basename(filename)

if filename.endswith(".txt"):
    outputfile = filename[:-4]
else:
    outputfile = filename

with open(os.path.expanduser('~/marty-stew.github.io/docs/') + outputfile + '.html', 'w') as f:
    f.write(result)

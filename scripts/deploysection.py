import os

def deploy_section(section_name):
    file = open(os.path.expanduser('~/.marty/') + 'txt/' + section_name + '/index.org', 'r')
    section_index = file.readlines()
    section_html = '<ul>\n'
    for i in range(len(section_index)):
        if section_index[i].startswith("* "):
            link_title = section_index[i].removeprefix("* ").strip()
            link_url = section_index[i+1].removeprefix("** ").strip()
            link_summary = section_index[i+2].removeprefix("** ").strip()
            section_html += f'<li><a href="{link_url}"><h2>{link_title}</h2><p>{link_summary}</p></li>\n'
    section_html += '</ul>';
    return(section_html)

print(deploy_section('juliette'))
        

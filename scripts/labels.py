def format_label(label):
    if(label == 'juliette'):
        formatted_label = 'Julie-ette'
    else:
        formatted_label = label.replace("-", " ").title()
    return formatted_label

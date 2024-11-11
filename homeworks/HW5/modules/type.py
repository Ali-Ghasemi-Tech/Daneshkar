def select_file_type(content_type):
    if 'text/html' in content_type:
        return '.html'
    elif 'text' in content_type:
        return '.txt'
    elif 'image' in content_type:
        return '.jpg'
    elif 'application/pdf' in content_type:
        return '.pdf'
    elif 'application/binary' in content_type:
        return '.bin'
    elif 'mp4' in content_type:
        return '.bin'
    else:
        return '.unknown'
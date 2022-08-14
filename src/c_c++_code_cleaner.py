import os
from os import path
import re

ext_set = ['.c', '.h', '.cpp', '.hpp', '.py']
replacement_spaces = ' ' * 4

def tab2spaces(url):
    file_contents = ''
    with open(url, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    file_contents = re.sub('\t', replacement_spaces, file_contents)

    with open(url, 'w', encoding='utf-8') as f:
        f.write(file_contents)

def trim_trailing_spaces(url):
    file_contents = ''
    with open(url, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    file_contents = re.sub(r"\s+$", "", file_contents)

    with open(url, 'w', encoding='utf-8') as f:
        f.write(file_contents)

def scan_files(url):
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            ext = os.path.splitext(f)[-1].lower()
            for xx in ext_set:
                if ext == xx:
                    print(real_url)
                    tab2spaces(real_url)
                    trim_trailing_spaces(real_url)
        elif path.isdir(real_url):
            scan_files(real_url)
        else:
            pass

scan_files("./")
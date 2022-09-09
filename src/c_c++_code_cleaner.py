import os
from os import path
import re
import typer
from typing import Optional
from rich.traceback import install

def tab2spaces(url):
    file_contents = ''
    
    with open(url, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    file_contents = re.sub('\t', replacement_spaces, file_contents)

    with open(url, 'w', encoding='utf-8') as f:
        f.write(file_contents)
        
def trim_trailing_spaces(url):
    line_set = []
    
    with open(url, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        if ('\n' != line or '\r' != line or '\n\r' != line or '\r\n' != line):
            line = line.rstrip()
            line += '\n'
        line_set.append(line)
        
    with open(url, 'w', encoding='utf-8') as f:
        f.writelines(line_set)
        
def remove_spaces_line(url):
    line_set = []

    with open(url, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        c = line.replace(' ', '')
        if ('\n' == c or '\r' == c or '\n\r' == c or '\r\n' == c):
            line_set.append(c)
        else:
            line_set.append(line)

    with open(url, 'w', encoding='utf-8') as f:
        f.writelines(line_set)

def scan_files(url):
    if path.isdir(url):
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
                        remove_spaces_line(real_url)
            elif path.isdir(real_url):
                scan_files(real_url)
            else:
                pass
    else:
        ext = os.path.splitext(url)[-1].lower()        
        for xx in ext_set:
            if ext == xx:
                print(url)
                tab2spaces(url)
                trim_trailing_spaces(url)
                remove_spaces_line(url)

ext_set = ['.c', '.h', '.cpp', '.hpp', '.py', '.m']
replacement_spaces = ' ' * 4
__version__ = "1.0.0"
install()

def version_callback(value: bool):
    if value:
        typer.echo(f"Version: v{__version__}")
        raise typer.Exit()

def path_callback(value: str):
    typer.secho(f"{value} begin to process ... ", fg=typer.colors.BRIGHT_WHITE, bg=typer.colors.GREEN)
    return value
        
def main(version: Optional[bool] = typer.Option(None, "--version", '-v', callback=version_callback), path: str = typer.Option("./", '--path', '-p', prompt = "Paste your path of code", help="code path", confirmation_prompt=True, callback=path_callback)):
    """
    Simple program that cleanup your c/c++/python/matlab code with utf-8.
    """
    scan_files(path)

if __name__ == '__main__':
    typer.run(main)



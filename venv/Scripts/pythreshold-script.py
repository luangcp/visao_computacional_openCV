#!c:\users\luang\documents\visao_computacional_opencv\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pythreshold==0.3.1','console_scripts','pythreshold'
__requires__ = 'pythreshold==0.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pythreshold==0.3.1', 'console_scripts', 'pythreshold')()
    )

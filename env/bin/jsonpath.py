#!/home/younggue/Desktop/ebagu0.2/env/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'jsonpath-rw==1.4.0','console_scripts','jsonpath.py'
__requires__ = 'jsonpath-rw==1.4.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('jsonpath-rw==1.4.0', 'console_scripts', 'jsonpath.py')()
    )

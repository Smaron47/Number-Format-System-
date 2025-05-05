import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['winreg','tkinter','sqlite3','time','customtkinter'],
        'include_files': ['customer.db']
    }
}


executables = [Executable('numsym.py', base=base,icon="opi.ico")]

setup(name='Number',
      version='1.2',
      description='no description',
      options=options,
      executables=executables)

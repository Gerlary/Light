from cx_Freeze import setup, Executable

setup(
    name = "menu", #просто название
    version = "1.0", #просто версия
    description = "", #просто описание 
    executables = [Executable("menu.py", base = "Win32GUI")] #menu.py название компелируемого файла, а base = "Win32GUI"
                                                             #позволяет запустить без консоли в виндоус
)
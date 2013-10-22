from cx_Freeze import setup, Executable
setup(name = "StepmaniaFileChanger", version = "0.1", description = "delete rolls from *.sm file", executables = [Executable("File_Changer_GUI.py", base="Win32GUI")])

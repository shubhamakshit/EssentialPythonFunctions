import os
import shutil

class PyShell:
    @staticmethod
    def cd(path):
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"No such file or directory: '{path}'")

    @staticmethod
    def ls(path=None):
        if path is None:
            path = os.getcwd()
        try:
            contents = os.listdir(path)
            for content in contents:
                print(content)
        except FileNotFoundError:
            print(f"No such file or directory: '{path}'")

    @staticmethod
    def rm(path):
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except FileNotFoundError:
            print(f"No such file or directory: '{path}'")

    @staticmethod
    def which(program_name):
        extensions = os.environ.get("PATHEXT", ".EXE").split(os.pathsep)
        for path in os.environ["PATH"].split(os.pathsep):
            base_path = os.path.join(path, program_name)
            options = [base_path] + [base_path + ext for ext in extensions]
            for full_path in options:
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                    return full_path
        return None

    @staticmethod
    def clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

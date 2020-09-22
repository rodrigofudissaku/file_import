import os
from fnmatch import fnmatch


 #root = '/some/directory'
#diretorio = r"C:\\Project\\Python\\file_import"
#padraoBusca = "*.py"

def obter (diretorio, padraoBusca):
    list=[]
    for path, subdirs, files in os.walk(diretorio):
        for name in files:
            if fnmatch(name, padraoBusca):
                list.append(os.path.join(path, name))
    return list

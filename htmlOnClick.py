import os
import numpy as np
import pandas as pd
import re

#incluir import e source

def obter(fname):

    # fname = os.path.join("C:\\", "Project", "Python",
    #                     "FILE_IMPORT", "html", "test.html")

    with open(fname, 'r') as file:
        data = file.read().replace('\n', ' ')

    resultado=re.findall(r'onclick="\w+',data)

    dfOnclick= pd.DataFrame(resultado,columns=["chamadanaotratada"])
    dfOnclick["filename"] = fname

    dfOnclick["functioname"] = dfOnclick.apply(
        lambda linha: re.findall("\w+", linha.chamadanaotratada)[1], axis=1)
    return dfOnclick
    
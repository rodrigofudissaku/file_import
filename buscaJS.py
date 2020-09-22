import os
import numpy as np
import pandas as pd
import re

def obterMetodosQueChamam(text,fname):
    ##text="text"

    ##fname= os.path.join("C:\\","Project","Python","FILE_IMPORT","js","helloworld.js")

    with open(fname,'r') as file:
        data= file.read().replace('\n',' ')

    count = 0
    lista = []

    while(count < len(data)):
        firstelement = data.find("function", count) if data.find(
            "function", count) != -1 else len(data)
        count = firstelement+1
        nextelement = (data.find("function", count)-1, len(data)
                        )[data.find("function", firstelement) > 0]
        if nextelement > -1:
            lista.append(data[firstelement:nextelement])



    dfCodigoJS = pd.DataFrame(lista,columns=["codigo"])
    dfCodigoJS["caminho"] = fname


    resultado = dfCodigoJS[dfCodigoJS["codigo"].str.contains(text)]

    resultado["function name"] = resultado.apply(
        lambda linha: 
        re.findall("\w+", linha.codigo)[1]
        , axis=1
        )

    return resultado



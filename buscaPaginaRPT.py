import arquivos
import buscaJS
import pandas as pd
import htmlOnClick as html


arquivosJS= arquivos.obter(r"C:\\Project\\Python\\file_import","*.js")
arquivosHTML = arquivos.obter(r"C:\\Project\\Python\\file_import", "*.html")

dataFrameJS = []
dataFrameHTML = []

for arquivoJS in arquivosJS:
    if not(len(dataFrameJS)):
        dataFrameJS = buscaJS.obterMetodosQueChamam("text", arquivoJS)
    else:
        df = buscaJS.obterMetodosQueChamam("text", arquivoJS)
        dataFrameJS = dataFrameJS.append(df, ignore_index=True)

for arquivoHTML in arquivosHTML:
    if not(len(dataFrameHTML)):
        dataFrameHTML =html.obter(arquivoHTML)
    else:
        dataFrameHTML = dataFrameHTML.append(html.obter(arquivoHTML))


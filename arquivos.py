from pathlib import Path
import os.path

#BUSCAR CAMINHO ATUAL DO SCRIPT
mypath = Path().absolute()
caminho = format(mypath)

#CRIAR ARQUIVO DE LOG
NomeLog = 'log.txt'
CaminhoLog = caminho + '\\' + NomeLog
gearararquivo = open(CaminhoLog, 'w', encoding='utf-8')

#ABRIR ARQUIVO CONTENDO A RELAÇÃO DE NUMEROS DOS RELATÓRIOS PARA CONFERIR
arquivo = caminho + '\\pasta.txt'
linhas = open(arquivo, 'r')
    

#LOOP PARA CONFERIR RELATÓRIOS
for line in linhas:
    texto = line.strip() + '.pdf'
    texto = texto
    if os.path.isfile(texto) == False:
        documento = open(CaminhoLog, 'a')
        documento.write("Arquivo não encontrado: " + texto + '\n')
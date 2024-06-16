arquivo = open(
    "C:/Users/nicol/OneDrive/Área de Trabalho/Projetos Bootcamp Dio/Primeiro programa de Python/Manipulação de Arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo ", "\n", "um", "novo", "\n", "texto"])
arquivo.close()
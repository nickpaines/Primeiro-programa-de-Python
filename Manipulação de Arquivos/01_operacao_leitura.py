arquivo = open("C:/Users/nicol/OneDrive/Área de Trabalho/Projetos Bootcamp Dio/Primeiro programa de Python/Manipulação de Arquivos/lorem.txt", "r")

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# tip
#while len(linha := arquivo.readline()) :
#    print(linha)
arquivo.close()
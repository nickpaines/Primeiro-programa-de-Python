def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"seja bem vindo {nome}!")



exibir_mensagem()
exibir_mensagem_2(nome="Nicolas")
exibir_mensagem_3()
exibir_mensagem_3(nome="Julia")
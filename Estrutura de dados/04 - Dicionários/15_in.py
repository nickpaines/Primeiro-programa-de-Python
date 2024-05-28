contatos = {
    "nicolas@gmail.com": {"nome": "Nicolas", "telefone": "996545678"},
    "valkiria@gmail.com": {"nome": "Valkiria", "telefone": "995467786"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "995894617"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "998425621"},
}

resultado = "nicolas@gmail.com" in contatos #True
print(resultado)

resultado = "nico@gmail.com" in contatos
print(resultado)  #False

resultado = "idade" in contatos["nicolas@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["valkiria@gail.com"] #True
print(resultado)
contatos = {
    "nicolas@gmail.com": {"nome": "Nicolas", "telefone": "996545678"},
    "valkiria@gmail.com": {"nome": "Valkiria", "telefone": "995467786"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "995894617"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "998425621", "extra": {"a": 1}},
}

telefone = contatos["valkiria@gmail.com"]["telefone"]
print(telefone)

extra = contatos["joao@gmail.com"]["extra"]["a"]
print(extra)

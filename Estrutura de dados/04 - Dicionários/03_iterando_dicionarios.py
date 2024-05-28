contatos = {
    "nicolas@gmail.com": {"nome": "Nicolas", "telefone": "996545678"},
    "valkiria@gmail.com": {"nome": "Valkiria", "telefone": "995467786"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "995894617"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "998425621"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
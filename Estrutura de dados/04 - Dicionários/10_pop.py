contatos = {"nicolas@gmail.com": {"nome": "Nicolas", "telefone": "996545678"}}

resultado = contatos.pop("nicolas@gmail.com")

print(resultado)

resultado = contatos.pop("nicolas@gmail.com", {})
print(resultado)
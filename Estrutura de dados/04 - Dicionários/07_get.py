contatos = {"nicolas@gmail.com": {"nome": "Nicolas", "telefone": "996545678"}}

#contatos["chave"]

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "nicolas@gmail.com", {}
)
print(resultado)
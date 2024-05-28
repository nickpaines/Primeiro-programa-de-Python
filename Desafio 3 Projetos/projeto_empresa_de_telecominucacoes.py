def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif 10 < consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo <=21:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input())
print(recomendar_plano(consumo))

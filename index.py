cuenta_base = input ("Cuando es el valor de la cuenta?")
amigos = 4
propina = (int(cuenta_base) * 0.10)
valor_total = (int(cuenta_base) + propina)
valor_divido = valor_total / amigos

print (f"el valor total es {valor_total} divido entre {amigos} amigos da {valor_divido} cada uno")
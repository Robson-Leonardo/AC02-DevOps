import os
from flask import Flask, jsonify, request

app = Flask(_name_)

@app.route('/')

def funcao():
    maximo = 99
    numero = 2
    primo = ""
    qntprimo = 0
    cont = 0
    while qntprimo < maximo:
        cont = 0
        for i in range(1,numero+1):
            if numero % i == 0:
                cont += 1
        if cont == 2:
            primo = primo + str(numero) + ", "
            qntprimo += 1
        cont = 0
        numero +=1
    primo = primo[0:len(primo) - 2]
    return primo

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)





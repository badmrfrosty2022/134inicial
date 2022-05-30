# ToDO: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import requests
import json

url= 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}


def teste_vender_pet():
    # Configura
    # Dados de entrada
    # Virao do arquivo pedido1.json

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 372166513
    pet_id_esperado = 2166513
    status_pedido_esperado = 'placed'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('//Users//eduardo//PycharmProjects//134inicial//vendors//json//pedido1.json')
    )


    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado


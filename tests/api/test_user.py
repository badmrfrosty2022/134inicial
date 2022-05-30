# Done: 1 - criar um teste que adicione um usuario
# Done: 2 - realizar o login e extrair o token da resposta

import json

import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def teste_incluir_usuario():
    # Configura
    # Dados de Entrada
    # Virão do arquivo usuario1.json

    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '6513216'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('//Users//eduardo//PycharmProjects//134inicial/vendors//json//usuario1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def teste_login():
    # Configura
    # Dados de entrada
    username = 'juca'
    password = 'bala'

    # Resultado Esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )


    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'O token = {token}')
    # Se 23:36 seriaposicao 23 até a 36. 23: é da posicao 23 até o final
    # [inicio : fim : passos


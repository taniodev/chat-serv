from app.core import lista_de_comandos, usuarios_conectados
from app.core.filtro import normalizar
from app.core.usuario import alterar_nome, definir_nome

lista_de_comandos['nome'] = alterar_nome


def _separar_comando(mensagem: str) -> tuple:
    """
    Retorne uma tupla contendo o comando e o argumento presente na mensagem.

    :param mensagem: A string de onde separar o comando.
    :return: (comando, argumento,)

    Exemplo:
    >>> separar_comando('/CoMandO Argumento')
    ('comando', 'Argumento')

    """
    argumentos = comando = ''

    for indice, letra in enumerate(mensagem):
        if indice > 0:
            if letra == ' ':
                argumentos += mensagem[indice+1:]
                break
            comando += normalizar(letra)

    return (comando, argumentos)


async def _executar_comando(usuario, mensagem: str) -> None:
    """
    Execute um comando do servidor.

    Se o comando digitado for um comando existente, execute-o passando os argumentos.
    Se o comando for correspondente a um usuário, envie uma mensagem privada apenas para este usuário.

    """
    comando, argumentos = _separar_comando(mensagem)

    if comando in lista_de_comandos:
        await lista_de_comandos[comando](usuario, argumentos)
    elif comando in usuarios_conectados:
        await usuarios_conectados[comando].msg.enviar(f'{usuario.nome} (pvt): {argumentos}')
    else:
        await usuario.msg.enviar(f'> Comando desconhecido: {comando}')


async def filtrar_comandos(usuario, mensagem: str):
    if mensagem[0] == '/':
        await _executar_comando(usuario, mensagem)
        return

    if not usuario.nome_id or not usuario.nome:
        await definir_nome(usuario, mensagem)
        return

    await usuario.msg.enviar_para_todos(f'{usuario.nome}: {mensagem}')

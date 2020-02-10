from app.core import lista_de_comandos
from app.core.usuario import alterar_nome, definir_nome

lista_de_comandos['nome'] = alterar_nome


def separar_comando(mensagem: str) -> tuple:
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
            comando += letra.lower()

    return (comando, argumentos)


async def comando_inexistente(usuario, comando: str, _) -> None:
    """Envie uma mensagem informando que o comando não foi encontrado."""
    await usuario.msg.enviar(f'> Comando desconhecido: {comando}')


async def filtrar_comandos(usuario, mensagem: str):
    if mensagem[0] == '/':
        comando, argumentos = separar_comando(mensagem)
        await lista_de_comandos.get(comando, comando_inexistente)(usuario, comando, argumentos)
        return

    if not usuario.nome_id or not usuario.nome:
        await definir_nome(usuario, mensagem)
        return

    await usuario.msg.enviar_para_todos(f'{usuario.nome}: {mensagem}')

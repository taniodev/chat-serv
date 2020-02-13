from app.core import lista_de_comandos, usuarios_conectados
from app.core.filtro import normalizar


async def nome_valido(enviar, nome: str) -> bool:
    """
    Verifique se um nome é válido para ser usado.

    :param enviar: Uma função que será usada para retornar as mensagens de erro ao usuário.
    :param nome: O nome que será avaliado.
    :return: True se o nome puder ser usado, False em caso contrário.

    """
    nome = normalizar(nome)

    if len(nome) < 2 or len(nome) > 20:
        await enviar('> O nome deve ter entre 2 e 20 caracteres')
        return False
    elif nome in usuarios_conectados:
        await enviar('> Este nome já está em uso, tente outro')
        return False
    elif nome in lista_de_comandos:
        await enviar('> Este nome é um comando do bate-papo, tente outro')
        return False

    return True

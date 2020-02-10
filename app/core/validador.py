from normality import normalize

from app.core import lista_de_comandos, usuarios_conectados


async def nome_valido(enviar, nome: str) -> bool:
    """
    Verifique se um nome é válido para ser usado.

    :param enviar: Uma função que será usada para retornar as mensagens de erro ao usuário.
    :param nome: O nome que será avaliado.
    :return: True se o nome puder ser usado, False em caso contrário.

    """
    texto_normalizado = normalize(nome)
    # A função normalize() retorna None para entradas como '', ' ', entre outras.
    nome = texto_normalizado if texto_normalizado else ''

    if len(nome) < 2 or len(nome) > 20:
        await enviar('> O nome deve ter entre 2 e 20 caracteres')
        return False
    elif usuarios_conectados.get(nome) is not None:
        await enviar('> Este nome já está em uso, tente outro')
        return False
    elif lista_de_comandos.get(nome) is not None:
        await enviar('> Este nome é um comando do bate-papo, tente outro')
        return False

    return True


async def nome_valido(enviar, nome: str) -> bool:
    """
Verifica se o nome é válido para ser usado.

:param enviar: Uma função que será usada para retornar as mensagens de erro ao usuário.
:param nome: O nome que será avaliado.
:return: True se o nome puder ser usado, False em caso contrário.

"""
    if len(nome) < 2 or len(nome) > 20:
        await enviar('> O nome deve ter entre 2 e 20 caracteres')
        return False

    return True

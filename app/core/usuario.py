from normality import normalize

from app.core import usuarios_conectados
from app.core.mensageiro import Mensageiro
from app.core.validador import nome_valido


class Usuario:
    def __init__(self, protocolo) -> None:
        self.msg = Mensageiro(usuarios_conectados, self)
        self.nome = None
        self.nome_id = None
        self.protocolo = protocolo

    async def atribuir_nome(self, nome: str) -> bool:
        """
Atribui um nome ao usuário.

:param nome: O nome que será atribuido.
:return: True se o nome foi atribuido, False em caso contrário.

"""
        if await nome_valido(self.msg.enviar, nome):
            usuarios_conectados.pop(self.nome_id, None)
            self.nome = nome
            self.nome_id = normalize(nome)
            usuarios_conectados[self.nome_id] = self
            return True


async def definir_nome(usuario: Usuario, nome: str) -> None:
    """
Define um nome para o usuário quando ele está entrando no chat.

:param usuario: O usuário que receberá o nome.
:param nome: O nome que deve ser atribuído ao usuário.

"""
    if await usuario.atribuir_nome(nome):
        await usuario.msg.enviar_para_todos(f'*. {usuario.nome} entra na conversação')

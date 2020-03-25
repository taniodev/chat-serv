from app.core import usuarios_conectados
from app.core.filtro import normalizar
from app.core.mensageiro import Mensageiro
from app.core.validador import nome_valido


class Usuario:
    def __init__(self, protocolo) -> None:
        self.esta_conectado = True
        self.msg = Mensageiro(usuarios_conectados, self)
        self.nome = None
        self.nome_id = None
        self.protocolo = protocolo

    def _separar_nome(self, texto: str) -> str:
        texto = texto.lstrip()
        texto = texto.split(' ')
        return texto[0]

    async def atribuir_nome(self, nome: str) -> bool:
        """
        Atribui um nome ao usuário.

        :param nome: O nome que será atribuido.
        :return: True se o nome foi atribuido, False em caso contrário.

        """
        nome = self._separar_nome(nome)

        if await nome_valido(self.msg.enviar, nome):
            usuarios_conectados.pop(self.nome_id, None)
            self.nome = nome
            self.nome_id = normalizar(nome)
            usuarios_conectados[self.nome_id] = self
            return True

    async def desconectou(self):
        """Chame este método antes de fechar a conexão."""
        usuarios_conectados.pop(self.nome_id, None)
        await self.msg.enviar_para_todos(f'*. Usuário {self.nome} saiu da conversação')


async def alterar_nome(usuario: Usuario, nome: str) -> None:
    """
    Altera o nome do usuário que já está conectado.

    :param usuario: O usuário que receberá o nome.
    :param nome: O nome que deve ser atribuído ao usuário.

    """
    nome_antigo = usuario.nome
    if await usuario.atribuir_nome(nome):
        await usuario.msg.enviar_para_todos(f'*. Usuário {nome_antigo} é conhecido como {usuario.nome}')


async def definir_nome(usuario: Usuario, nome: str) -> None:
    """
Define um nome para o usuário quando ele está entrando no chat.

:param usuario: O usuário que receberá o nome.
:param nome: O nome que deve ser atribuído ao usuário.

"""
    if await usuario.atribuir_nome(nome):
        await usuario.msg.enviar_para_todos(f'*. {usuario.nome} entra na conversação')

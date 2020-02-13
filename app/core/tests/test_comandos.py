from unittest.mock import AsyncMock

import pytest

from app.core import lista_de_comandos, usuarios_conectados
from app.core.comandos import _executar_comando, _separar_comando


@pytest.fixture
def setup():
    lista_de_comandos['umcomando'] = AsyncMock()
    usuarios_conectados['usuario-acucar'] = AsyncMock()
    yield
    del lista_de_comandos['umcomando']
    del usuarios_conectados['usuario-acucar']


@pytest.mark.parametrize('entrada, saida', [
    ('/CoMaNdo Argumento', ('comando', 'Argumento',)),
    ('/ÇôMãNdo Argumento', ('comando', 'Argumento',)),
    ('/Co-Man_do Argumento', ('co-man_do', 'Argumento',)),
])
def test_separar_comando(entrada, saida):
    assert _separar_comando(entrada) == saida


@pytest.mark.asyncio
async def test_executar_comando_da_lista_de_comandos(setup):
    usuario_mock = AsyncMock()
    await _executar_comando(usuario_mock, '/umcomando umargumento')
    lista_de_comandos['umcomando'].assert_called_once_with(usuario_mock, 'umargumento')


@pytest.mark.asyncio
async def test_executar_comando_inexistente_na_lista_de_comandos(setup):
    usuario_mock = AsyncMock()
    await _executar_comando(usuario_mock, '/umcomando20 umargumento')
    usuario_mock.msg.enviar.assert_called_once_with('> Comando desconhecido: umcomando20')


@pytest.mark.asyncio
@pytest.mark.parametrize('nome', [
    'usuario-acucar',
    'Usuário-Açúcar',
])
async def test_executar_comando_enviar_mensagem_privada(nome, setup):
    usuario_mock = AsyncMock()
    usuario_mock.nome = 'Fulano'
    await _executar_comando(usuario_mock, f'/{nome} teste')
    usuarios_conectados['usuario-acucar'].msg.enviar.assert_called_once_with('Fulano (pvt): teste')

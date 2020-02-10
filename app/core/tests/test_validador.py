from unittest.mock import AsyncMock

import pytest

from app.core import lista_de_comandos, usuarios_conectados
from app.core.validador import nome_valido


@pytest.fixture
def setup():
    lista_de_comandos['umcomandoqualquer'] = AsyncMock()
    usuarios_conectados['fulano'] = AsyncMock()
    yield
    del lista_de_comandos['umcomandoqualquer']
    del usuarios_conectados['fulano']


@pytest.mark.asyncio
@pytest.mark.parametrize('entrada, saida', [
    ('', '> O nome deve ter entre 2 e 20 caracteres'),
    ('a', '> O nome deve ter entre 2 e 20 caracteres'),
    ('um-nome-muito-grande9', '> O nome deve ter entre 2 e 20 caracteres'),
    ('Fulano', '> Este nome já está em uso, tente outro'),
    ('umcomandoqualquer', '> Este nome é um comando do bate-papo, tente outro'),
])
async def test_nomes_nao_validos(entrada, saida, setup):
    enviar = AsyncMock()
    resposta = await nome_valido(enviar, entrada)
    assert resposta is False
    enviar.assert_called_once_with(saida)

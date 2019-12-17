from unittest.mock import AsyncMock

import pytest

from app.core.validador import nome_valido


@pytest.mark.asyncio
@pytest.mark.parametrize('nome', [
    'a',
    'um-nome-muito-grande9',
])
async def test_nomes_nao_validos(nome):
    enviar = AsyncMock()
    resposta = await nome_valido(enviar, nome)
    assert resposta is False
    enviar.assert_called_once()

from unittest.mock import AsyncMock, Mock

import pytest

from app.servidor.telnet import telnet


@pytest.fixture
def reader_mock() -> AsyncMock:
    """Cria um objeto reader mock para os testes."""
    reader = AsyncMock()
    return reader


@pytest.fixture
def writer_mock() -> AsyncMock:
    """Cria e prepara um objeto writer mock para os testes."""
    writer = AsyncMock()

    # Um objeto AsyncMock que não é chamado com await, faz com que apareça warning ao rodar os testes
    writer.write = Mock()
    writer.close = Mock()

    return writer


@pytest.fixture
def rodar_servidor_telnet(reader_mock, writer_mock):
    """Obtenha uma função para rodar o servidor telnet."""

    async def rodar_telnet(mensagens: list) -> tuple:
        """
        Execute o servidor telnet para testes.

        :param mensagens: Simulação das mensagens enviadas pelo usuário.
        :return: Os dois objetos reader e writer para fazer as validações.

        """
        reader_mock.read.side_effect = mensagens
        try:
            await telnet(reader_mock, writer_mock)
        except StopAsyncIteration:
            pass
        return (reader_mock, writer_mock)

    return rodar_telnet

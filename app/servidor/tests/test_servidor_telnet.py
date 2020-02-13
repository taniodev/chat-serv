from unittest.mock import AsyncMock, call

import pytest

from app.core import usuarios_conectados


@pytest.fixture
def usuario_mock_interno() -> AsyncMock:
    """Cria um objeto que representa um cliente já conectado ao servidor."""
    usuario_mock = AsyncMock()
    usuarios_conectados['usr1'] = usuario_mock
    yield usuario_mock
    del usuarios_conectados['usr1']


@pytest.fixture
def digita_nome():
    """Simule um usuário que digitou o nome para entrar no chat."""
    mensagens = [b'Fulano']
    yield mensagens
    usuarios_conectados.pop('fulano', None)


@pytest.mark.asyncio
async def test_eco_da_mensagem(digita_nome, rodar_servidor_telnet):
    digita_nome.append(b'teste')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    writer_mock.write.assert_called_with(b'Fulano: teste\n')


@pytest.mark.asyncio
async def test_mensagem_para_todos_os_clientes(digita_nome, rodar_servidor_telnet, usuario_mock_interno):
    digita_nome.append(b'teste')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    usuario_mock_interno.msg.enviar.assert_called_with('Fulano: teste')


@pytest.mark.asyncio
async def test_mensagem_ao_conectar_no_servidor(digita_nome, rodar_servidor_telnet):
    calls = [
        call('> Digite o seu nome:\n'.encode(encoding='iso-8859-1')),
        call('*. Fulano entra na conversação\n'.encode(encoding='iso-8859-1')),
    ]

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    writer_mock.write.assert_has_calls(calls)


@pytest.mark.asyncio
async def test_comando_barra_nome(digita_nome, rodar_servidor_telnet):
    digita_nome.append(b'/nome Beltrano')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    writer_mock.write.assert_called_with('*. Usuário Fulano é conhecido como Beltrano\n'.encode(encoding='iso-8859-1'))


@pytest.mark.asyncio
async def test_comando_barra_nome_sem_argumentos(digita_nome, rodar_servidor_telnet):
    digita_nome.append(b'/nome')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    writer_mock.write.assert_called_with('> O nome deve ter entre 2 e 20 caracteres\n'.encode(encoding='iso-8859-1'))


@pytest.mark.asyncio
async def test_comando_inexistente(digita_nome, rodar_servidor_telnet):
    digita_nome.append(b'/umcomandoqualquer umargumento')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    writer_mock.write.assert_called_with('> Comando desconhecido: umcomandoqualquer\n'.encode(encoding='iso-8859-1'))


@pytest.mark.asyncio
async def test_envio_de_mensagem_privada(digita_nome, rodar_servidor_telnet, usuario_mock_interno):
    digita_nome.append(b'/usr1 teste')

    reader_mock, writer_mock = await rodar_servidor_telnet(digita_nome)

    usuario_mock_interno.msg.enviar.assert_called_with('Fulano (pvt): teste')

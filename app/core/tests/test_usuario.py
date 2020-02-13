from unittest.mock import Mock

import pytest

from app.core import usuarios_conectados
from app.core.usuario import Usuario


@pytest.fixture
def usuario():
    protocolo_mock = Mock()
    usr = Usuario(protocolo_mock)
    yield usr
    usuarios_conectados.pop(usr.nome_id, None)


@pytest.mark.asyncio
@pytest.mark.parametrize('nome', [
    'Açúcar',
    ' Açúcar Doce ',
])
async def test_atribuir_nome(nome, usuario):
    await usuario.atribuir_nome(nome)
    assert usuario.nome == 'Açúcar'
    assert usuario.nome_id == 'acucar'
    assert usuario.nome_id in usuarios_conectados

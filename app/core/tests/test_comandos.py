import pytest

from app.core.comandos import separar_comando


@pytest.mark.parametrize('entrada, saida', [
    ('/CoMaNdo Argumento', ('comando', 'Argumento',)),
])
def test_separar_comando(entrada, saida):
    assert separar_comando(entrada) == saida

import pytest

from app.core.filtro import normalizar


@pytest.mark.parametrize('entrada, saida', [
    ('   ', ''),
    (' Acucar  ', 'acucar'),
    ('açúcar', 'acucar'),
    (' UM-Pote_com-açúcar ', 'um-pote_com-acucar'),
])
def test_normalizar(entrada, saida):
    assert normalizar(entrada) == saida

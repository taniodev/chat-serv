from unicodedata import normalize


def normalizar(texto: str) -> str:
    """
    Normalize um texto qualquer.

    Substitui os caracteres especiais do texto.
    Exemplo:
    >>> normalizar(' AçúcAR ')
    'acucar'

    """
    texto = normalize('NFKD', texto)
    texto = texto.encode('iso-8859-1', 'ignore').decode('iso-8859-1')
    texto = texto.strip()
    return texto.lower()

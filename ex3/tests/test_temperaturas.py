import pytest
from temperaturas import maior, dia_do_maior

@pytest.mark.parametrize(
        "tempera, esperado",
        [
            ([21, 25, 19, 30, 22], 30),
            ([18], 18),
            ([30, 21], 30)
        ]
    )

def test_tempera_maior(tempera, esperado):
    maior(tempera) == esperado

@pytest.mark.parametrize(
        "tempera, esperado",
        [
            ([21, 25, 19, 30, 22], 3),
            ([18], 0),
            ([30, 21], 0)
        ]
    )

def test_tempera_dia_do_maior(tempera, esperado):
    dia_do_maior(tempera) == esperado

def test_vazio_maior():
    with pytest.raises(ValueError, match=r"^lista vazia$"):
        maior([])

def test_vazio_dia_maior():
    with pytest.raises(ValueError, match=r"^lista vazia$"):
        dia_do_maior([])

def test_maior_segundo_elemento():
    assert maior([10, 50, 20]) == 50


def test_dia_maior_lista_unico_elemento():
    assert dia_do_maior([18]) == 0


def test_dia_maior_segundo_elemento():
    assert dia_do_maior([10, 50, 20]) == 1


def test_dia_primeira_ocorrencia():
    assert dia_do_maior([30, 20, 30]) == 0
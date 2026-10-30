import pytest
from classificacao import classificar_aluno

def test_aprovado():
    classificar_aluno(8.0, 80) == "Aprovado"

def test_reprovado():
    classificar_aluno(3.0, 90) == "Reprovado"

@pytest.mark.parametrize("media", [-1, 11])
def test_media_invalida(media):
    with pytest.raises(ValueError, match=r"^Media invalida$"):
        classificar_aluno(media, 80)

@pytest.mark.parametrize("presenca", [-1, 101])
def test_presenca_invalida(presenca):
    with pytest.raises(ValueError, match=r"^Presenca invalida$"):
        classificar_aluno(8, presenca)

def test_presenca_0():
    assert classificar_aluno(8, 0) == "Reprovado por falta"

def test_reprova_falta():
    assert classificar_aluno(9, 74) == "Reprovado por falta"

def test_media_inferior():
    assert classificar_aluno(0, 75) == "Reprovado"

def test_media_superior():
    classificar_aluno(10, 75) == "Aprovado"

def test_media_limite_5():
    assert classificar_aluno(5, 75) == "Recuperacao"


def test_media_limite_7():
    assert classificar_aluno(7, 75) == "Aprovado"

def test_presenca_limite_75():
    assert classificar_aluno(8, 75) == "Aprovado"


def test_presenca_limite_100():
    assert classificar_aluno(8, 100) == "Aprovado"
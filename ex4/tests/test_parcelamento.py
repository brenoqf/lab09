import pytest
from parcelamento import parcela

@pytest.mark.parametrize(
    "valor, n, esperado",
    [
        (10,1,10),
        (10, 12, 0.98),
        (10, 2, 5),
        (10, 3, 3.33),
        (10, 4, 2.55)
    ]
)
def test_parcelas(valor, n, esperado):
    assert parcela(valor, n) == esperado

def test_vazio_0_parcelas():
    with pytest.raises(ValueError, match=r"^parcelas invalidas$"):
        parcela(20,0)

def test_vazio_13_parcelas():
    with pytest.raises(ValueError, match=r"^parcelas invalidas$"):
        parcela(20,13)
import pytest
from carrinho import total_com_desconto

def test_desconto():
    assert total_com_desconto([10.62, 20.07, 30.005, 40, 50]) == 141.69
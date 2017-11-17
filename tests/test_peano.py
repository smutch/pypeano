from peano import peano_hilbert_key, peano_hilbert_key_inverse


def test_zero():
    assert peano_hilbert_key(0, 0, 0, 3) == 0

    x, y, z = peano_hilbert_key_inverse(0, 3)
    assert x == 0
    assert y == 0
    assert z == 0

import numpy as np
from peano import peano_hilbert_key, peano_hilbert_keys
from peano import peano_hilbert_key_inverse, peano_hilbert_keys_inverse


def test_zero():
    assert peano_hilbert_key(0, 0, 0, 3) == 0

    x, y, z = peano_hilbert_key_inverse(0, 3)
    assert x == 0
    assert y == 0
    assert z == 0


def test_zeros():
    x, y, z = (np.zeros(50, np.int) for ii in range(3))
    assert np.all(peano_hilbert_keys(x, y, z, 3) == 0)

    keys = np.zeros(50, np.longlong)
    res = peano_hilbert_keys_inverse(keys, 3)
    assert np.all(r == 0 for r in res)

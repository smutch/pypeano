from numpy import int64
from ._peano import lib, ffi


def peano_hilbert_key(x: int, y: int, z: int, bits: int):
    return lib.peano_hilbert_key(x, y, z, bits)


def peano_hilbert_key_inverse(key: int64, bits: int):
    x, y, z = (ffi.new("int *") for ii in range(3))
    x[0], y[0], z[0] = (-999 for ii in range(3))
    _key = ffi.cast("long long", key)

    lib.peano_hilbert_key_inverse(_key, bits, x, y, z)
    assert x[0] != -999 and y[0] != -999 and z[0] != -999

    return x[0], y[0], z[0]

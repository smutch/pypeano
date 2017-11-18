import numba as nb
from numba import cffi_support
from numpy import array, zeros
from . import _peano

c__peano_hilbert_key = _peano.lib.peano_hilbert_key
c__peano_hilbert_key_inverse = _peano.lib.peano_hilbert_key_inverse
ffi = _peano.ffi
cffi_support.register_module(_peano)


@nb.jit(nopython=True)
def peano_hilbert_key(x, y, z, bits):
    return c__peano_hilbert_key(x, y, z, bits)


@nb.vectorize(nopython=True)
def peano_hilbert_keys(x, y, z, bits):
    return peano_hilbert_key(x, y, z, bits)


@nb.jit(nopython=True)
def peano_hilbert_key_inverse(key, bits):
    x = array([-999], nb.int32)
    y = array([-999], nb.int32)
    z = array([-999], nb.int32)

    c__peano_hilbert_key_inverse(nb.longlong(key), bits, ffi.from_buffer(x),
                                 ffi.from_buffer(y), ffi.from_buffer(z))

    return x[0], y[0], z[0]


@nb.jit(nopython=True)
def peano_hilbert_keys_inverse(keys, bits):
    x = zeros(keys.size, nb.int32)
    y = zeros(keys.size, nb.int32)
    z = zeros(keys.size, nb.int32)

    for arr in x, y, z:
        arr[:] = -999

    for ii, key in enumerate(keys):
        x[ii], y[ii], z[ii] = peano_hilbert_key_inverse(key, bits)

    return x, y, z

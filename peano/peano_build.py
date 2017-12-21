from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source("peano._peano", "",
                      sources=["cext/src/peano.c"],
                      extra_compile_args=["-std=c99"]
                      )

ffibuilder.cdef("""
    long long peano_hilbert_key(int x, int y, int z, int bits);
    void peano_hilbert_key_inverse(long long key, int bits, int *x, int *y, int
*z);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

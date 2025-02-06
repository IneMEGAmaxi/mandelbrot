/*
 *  C++ source file for module mandelbrot.CPPmandelbrot_set
 */


// See http://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html for examples on how to use pybind11.
// The example below is modified after http://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html#More-on-working-with-numpy-arrays
#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h> // add support for multi-dimensional arrays
#include <complex>
namespace nb = nanobind;

void
mandelbrot( nb::ndarray<std::complex<double>, nb::ndim<2>>  c_val // in
  , int N// in
  , nb::ndarray<double, nb::ndim<2>> img // inout
  )
{
   size_t rows = c_val.shape(0);
    size_t cols = c_val.shape(1);

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            std::complex<double> c = c_val(i, j);
            std::complex<double> z = 0;
            img(i, j) = -1.;
            for (int iter = 0; iter < N; ++iter) {
                z = z * z + c;
                if (std::abs(z) > 2.0) {
                    img(i,j) = iter + 1 - log(log(abs(z))) / 0.6931471805599453;
                    break;
                }
            }
        }
    }
}


NB_MODULE(CPPmandelbrot_set, m) {
    m.doc() = "A simple example python extension";

    m.def("mandelbrot", &mandelbrot, "calculate the mandelbrot set");

/*
    m.def("inspect"
         , [](nb::ndarray<> a)
           {
                printf("Array data pointer : %p\n", a.data());
                printf("Array dimension : %zu\n", a.ndim());
                for (size_t i = 0; i < a.ndim(); ++i) {
                    printf("Array dimension [%zu] : %zu\n", i, a.shape(i));
                    printf("Array stride    [%zu] : %zd\n", i, a.stride(i));
                }
                printf("Device ID = %u (cpu=%i, cuda=%i)\n"
                , a.device_id()
                , int(a.device_type() == nb::device::cpu::value)
                , int(a.device_type() == nb::device::cuda::value)
                );
                printf("Array dtype: int16=%i, uint32=%i, float32=%i, float64=%i\n"
                , a.dtype() == nb::dtype<int16_t>()
                , a.dtype() == nb::dtype<uint32_t>()
                , a.dtype() == nb::dtype<float>()
                , a.dtype() == nb::dtype<double>()
                );
            }
          , "inspect an array"
    );
    */
}
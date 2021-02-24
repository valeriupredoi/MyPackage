import iris
import numpy

def myfunc():
    """
    A toy function.

    Parameters
    ----------
    None

    Returns
    -------
    str
        location of installation for iris paclage
    float
        mean of (10, 20)
    """
    f = iris.__file__
    n = numpy.mean([10, 20])

    return f, n


fi, mean = myfunc()
print(fi, "\n", mean)

import unittest

from mypackage.myscript import myfunc

def test_myfunc():
    """The simplest test you'll ever see."""
    iris_file, mean = myfunc()
    assert mean == 15
    assert "iris" in iris_file


if __name__ == '__main__':
    unittest.main()

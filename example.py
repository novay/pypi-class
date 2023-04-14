# Menggunakan import:
# import pypi_class

# pypi_class.Module1().greet()
# pypi_class.Module2().greet()
# pypi_class.subpackage1.Module3().greet()
# pypi_class.subpackage1.Module4().greet()
# pypi_class.subpackage2.Module5().greet()

# Menggunakan from import:
from pypi_class import Module1, Module2
from pypi_class.subpackage1 import Module3, Module4
from pypi_class.subpackage2 import Module5

Module1().greet()
Module2().greet()
Module3().greet()
Module4().greet()
Module5().greet()
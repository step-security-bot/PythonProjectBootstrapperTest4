# ----------------------------------------------------------------------
# |
# |  Copyright (c) 2024 SSEC at Georgia Tech
# |  Distributed under the MIT License.
# |
# ----------------------------------------------------------------------
"""Unit tests for Math.py"""

from PythonProjectBootstrapperTest4.Math import *


# ----------------------------------------------------------------------
def test_Add():
    assert Add(1, 20) == 21


# ----------------------------------------------------------------------
def test_Sub():
    assert Sub(1, 20) == -19


# ----------------------------------------------------------------------
def test_Mult():
    assert Mult(2, 15) == 30


# ----------------------------------------------------------------------
def test_Div():
    assert Div(6, 3) == 2

from sympy import *
from pylatex import Document, Section, Subsection, Package, NoEscape
from pylatex.utils import italic
from pylatexenc import latexencode
import os

x, y, z, t = symbols('x y z t')

def latexify(S):
#    return latexencode.unicode_to_latex(NoEscape(latex(S)))
    return NoEscape(latex(S))

print("latexify = " + latexify(Integral(sqrt(1/x), x)))

print(simplify((x + x * y) / x))

print(solve([x + y - 2*z, y + 4*z], [x, y], dict=True))

m1 = Symbol('m_1')
m1

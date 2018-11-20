# -*- coding: utf-8 -*-
from string import Template

S = Template("$x,hello,$$ ${x}llo.$y")
S.substitute(x="he")
print(S)
"""he,hello,$ hello."""
d = {"x": "he", "y": "nice"}
S.substitute(d)

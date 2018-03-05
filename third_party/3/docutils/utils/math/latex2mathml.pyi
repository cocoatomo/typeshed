# Stubs for docutils.utils.math.latex2mathml (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

over: Any
Greek: Any
letters: Any
special: Any
sumintprod: Any
functions: Any
mathbb: Any
mathscr: Any
negatables: Any

class math:
    nchildren: int = ...
    children: Any = ...
    inline: Any = ...
    def __init__(self, children: Optional[Any] = ..., inline: Optional[Any] = ...) -> None: ...
    def full(self): ...
    def append(self, child): ...
    def delete_child(self): ...
    def close(self): ...
    def xml(self): ...
    def xml_start(self): ...
    def xml_end(self): ...
    def xml_body(self): ...

class mrow(math):
    def xml_start(self): ...

class mtable(math):
    def xml_start(self): ...

class mtr(mrow): ...
class mtd(mrow): ...

class mx(math):
    nchildren: int = ...
    data: Any = ...
    def __init__(self, data) -> None: ...
    def xml_body(self): ...

class mo(mx):
    translation: Any = ...
    def xml_body(self): ...

class mi(mx): ...
class mn(mx): ...

class msub(math):
    nchildren: int = ...

class msup(math):
    nchildren: int = ...

class msqrt(math):
    nchildren: int = ...

class mroot(math):
    nchildren: int = ...

class mfrac(math):
    nchildren: int = ...

class msubsup(math):
    nchildren: int = ...
    reversed: Any = ...
    def __init__(self, children: Optional[Any] = ..., reversed: bool = ...) -> None: ...
    def xml(self): ...

class mfenced(math):
    translation: Any = ...
    openpar: Any = ...
    def __init__(self, par) -> None: ...
    def xml_start(self): ...

class mspace(math):
    nchildren: int = ...

class mstyle(math):
    nchildren: Any = ...
    attrs: Any = ...
    def __init__(self, children: Optional[Any] = ..., nchildren: Optional[Any] = ..., **kwargs) -> None: ...
    def xml_start(self): ...

class mover(math):
    nchildren: int = ...
    reversed: Any = ...
    def __init__(self, children: Optional[Any] = ..., reversed: bool = ...) -> None: ...
    def xml(self): ...

class munder(math):
    nchildren: int = ...

class munderover(math):
    nchildren: int = ...
    def __init__(self, children: Optional[Any] = ...) -> None: ...

class mtext(math):
    nchildren: int = ...
    text: Any = ...
    def __init__(self, text) -> None: ...
    def xml_body(self): ...

def parse_latex_math(string, inline: bool = ...): ...
def handle_keyword(name, node, string): ...
def tex2mathml(tex_math, inline: bool = ...): ...
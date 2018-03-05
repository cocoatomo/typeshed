# Stubs for docutils.parsers.rst.directives.html (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes
from docutils.parsers.rst import Directive, states
from typing import Any

__docformat__: str

class MetaBody(states.SpecializedBody):
    class meta(nodes.Special, nodes.PreBibliographic, nodes.Element): ...
    def field_marker(self, match, context, next_state): ...
    def parsemeta(self, match): ...

class Meta(Directive):
    has_content: bool = ...
    SMkwargs: Any = ...
    def run(self): ...
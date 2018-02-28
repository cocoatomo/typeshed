# Stubs for docutils.writers.pseudoxml (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import writers
from typing import Any

__docformat__: str

class Writer(writers.Writer):
    supported: Any = ...
    config_section: str = ...
    config_section_dependencies: Any = ...
    output: Any = ...
    def translate(self): ...
    def supports(self, format): ...

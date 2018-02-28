# Stubs for docutils.transforms.frontmatter (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _sre import SRE_Pattern
from docutils.nodes import Bibliographic, docinfo, field_list, Node, topic, Text
from docutils.transforms import Transform
from typing import Any, ClassVar, Dict, List, Optional, Union

__docformat__: str

class TitlePromoter(Transform):
    def promote_title(self, node: Node) -> Optional[int]: ...
    def promote_subtitle(self, node: Node) -> Optional[int]: ...
    def candidate_index(self, node: Node) -> Tuple[Optional[Node], Optional[int]]: ...

class DocTitle(TitlePromoter):
    default_priority: int = ...
    def set_metadata(self) -> None: ...
    def apply(self) -> None: ...

class SectionSubTitle(TitlePromoter):
    default_priority: int = ...
    def apply(self) -> None: ...

class DocInfo(Transform):
    default_priority: int = ...
    biblio_nodes: Dict[str, Union[ClassVar[Bibliographic], ClassVar[topic]]] = ...
    def apply(self) -> None: ...
    def extract_bibliographic(self, field_list: field_list) -> List[Union[Bibliographic, topic]]: ...
    def check_empty_biblio_field(self, field: Node, name: str) -> Optional[int]: ...
    def check_compound_biblio_field(self, field: Node, name: str) -> Optional[int]: ...
    rcs_keyword_substitutions: List[Tuple[SRE_Pattern, str]] = ...
    def extract_authors(self, field: Node, name: str, docinfo: docinfo) -> None: ...
    def authors_from_one_paragraph(self, field: Node) -> List[List[Text]]: ...
    def authors_from_bullet_list(self, field: Node) -> List[List[Node]]: ...
    def authors_from_paragraphs(self, field: Node) -> List[List[Node]]: ...

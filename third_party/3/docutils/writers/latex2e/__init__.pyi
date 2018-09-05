# Stubs for docutils.writers.latex2e (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes, writers
from docutils.transforms import Transform
from types import ModuleType
from typing import Any, Dict, List, Optional, Pattern, Sequence, Tuple, Type, Union

__docformat__: str

class Writer(writers.Writer):
    supported: Tuple[str, ...] = ...
    default_template: str = ...
    default_template_path: str = ...
    default_preamble: str = ...
    table_style_values: Tuple[str, ...] = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    settings_defaults: Dict[str, int] = ...
    config_section: str = ...
    config_section_dependencies: Tuple[str, ...] = ...
    head_parts: Tuple[str, ...] = ...
    visitor_attributes: Tuple[str, ...] = ...
    output: Any = ...
    translator_class: LaTeXTranslator = ...
    def __init__(self) -> None: ...
    def get_transforms(self) -> List[Type[Transform]]: ...
    def translate(self) -> None: ...
    def assemble_parts(self) -> None: ...

class Babel:
    language_codes: Dict[str, str] = ...
    warn_msg: str = ...
    active_chars: Dict[str, str] = ...
    reporter: Any = ...
    language: str = ...
    otherlanguages: Dict[Any, Any] = ...
    def __init__(self, language_code: str, reporter: Optional[Any] = ...) -> None: ...
    setup: List[str] = ...
    def __call__(self) -> str: ...
    def language_name(self, language_code: str) -> str: ...
    def get_language(self) -> str: ...

class SortableDict(dict):
    def sortedkeys(self) -> List[Any]: ...
    def sortedvalues(self) -> List[Any]: ...

class PreambleCmds: ...

class CharMaps:
    alltt: Dict[int, str] = ...
    special: Dict[int, str] = ...
    unsupported_unicode: Dict[int, str] = ...
    utf8_supported_unicode: Dict[int, str] = ...
    textcomp: Dict[int, str] = ...
    pifont: Dict[int, str] = ...

class DocumentClass:
    document_class: str = ...
    sections: List[str] = ...
    def __init__(self, document_class: str, with_part: bool = ...) -> None: ...
    def section(self, level: int) -> str: ...

class Table:
    stubs: List[Any] = ...
    colwidths_auto: bool = ...
    def __init__(self, translator: LaTeXTranslator, latex_type: str) -> None: ...
    caption: List[str] = ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def is_open(self) -> bool: ...
    borders: List[str] = ...
    def set_table_style(self, table_style: Sequence[str], classes: Sequence[str]): ...
    def get_latex_type(self) -> str: ...
    def set(self, attr: Any, value: Any) -> None: ...
    def get(self, attr: Any) -> Any: ...
    def get_vertical_bar(self) -> str: ...
    def get_opening(self) -> str: ...
    def get_closing(self) -> str: ...
    def visit_colspec(self, node: nodes.Node) -> None: ...
    def get_colspecs(self, node: nodes.Node) -> str: ...
    def get_column_width(self) -> str: ...
    def get_multicolumn_width(self, start: int, len_: int) -> str: ...
    def get_caption(self) -> str: ...
    def need_recurse(self) -> Union[bool, int]: ...
    def visit_thead(self) -> List[str]: ...
    def depart_thead(self) -> List[str]: ...
    def visit_row(self) -> None: ...
    def depart_row(self) -> List[str]: ...
    def set_rowspan(self, cell: Any, value: Any) -> None: ...
    def get_rowspan(self, cell: Any) -> Any: ...
    def get_entry_number(self) -> Optional[int]: ...
    def visit_entry(self) -> None: ...
    def is_stub_column(self) -> Any: ...

class LaTeXTranslator(nodes.NodeVisitor):
    is_xetex: bool = ...
    compound_enumerators: bool = ...
    section_prefix_for_enumerators: bool = ...
    section_enumerator_separator: str = ...
    has_latex_toc: bool = ...
    is_toc_list: bool = ...
    section_level: int = ...
    inside_citation_reference_label: bool = ...
    verbatim: bool = ...
    insert_non_breaking_blanks: bool = ...
    insert_newline: bool = ...
    literal: bool = ...
    alltt: bool = ...
    warn: Any = ...
    error: Any = ...
    settings: Any = ...
    latex_encoding: str = ...
    use_latex_toc: bool = ...
    use_latex_docinfo: bool = ...
    hyperlink_color: str = ...
    font_encoding: str = ...
    literal_block_env: str = ...
    literal_block_options: str = ...
    bibtex: Optional[str] = ...
    language_module: ModuleType = ...
    babel: Any = ...
    author_separator: List[str] = ...
    documentoptions: str = ...
    d_class: DocumentClass = ...
    graphicx_package: str = ...
    docutils_footnotes: bool = ...
    head_prefix: List[str] = ...
    requirements: SortableDict = ...
    latex_preamble: List[Any] = ...
    fallbacks: SortableDict = ...
    pdfsetup: List[str] = ...
    title: List[str] = ...
    subtitle: List[str] = ...
    titledata: List[str] = ...
    body_pre_docinfo: List[str] = ...
    docinfo: List[str] = ...
    dedication: List[Any] = ...
    abstract: List[Any] = ...
    body: List[str] = ...
    context: List[Any] = ...
    title_labels: List[str] = ...
    subtitle_labels: List[str] = ...
    author_stack: List[List[str]] = ...
    date: List[str] = ...
    pdfinfo: List[str] = ...
    pdfauthor: List[str] = ...
    table_stack: List[Any] = ...
    active_table: Table = ...
    out: List[str] = ...
    out_stack: List[Any] = ...
    stylesheet: List[str] = ...
    hyperref_options: str = ...
    def __init__(self, document: nodes.document, babel_class: Any = ...) -> None: ...
    def stylesheet_call(self, path: str) -> str: ...
    def to_latex_encoding(self, docutils_encoding: str) -> str: ...
    def language_label(self, docutil_label: str) -> str: ...
    def encode(self, text: str) -> str: ...
    def attval(self, text: str, whitespace: Pattern[str] = ...) -> str: ...
    def is_inline(self, node: nodes.Node) -> bool: ...
    def append_hypertargets(self, node: nodes.Node) -> None: ...
    def ids_to_labels(self, node: nodes.Node, set_anchor: bool = ...) -> List[str]: ...
    def set_align_from_classes(self, node: nodes.Node) -> None: ...
    def insert_align_declaration(self, node: nodes.Node, default: Optional[Any] = ...) -> None: ...
    def duclass_open(self, node: nodes.Node) -> None: ...
    def duclass_close(self, node: nodes.Node) -> None: ...
    def push_output_collector(self, new_out: Any) -> None: ...
    def pop_output_collector(self) -> None: ...
    def visit_Text(self, node: nodes.Node) -> None: ...
    def depart_Text(self, node: nodes.Node) -> None: ...
    def visit_abbreviation(self, node: nodes.Node) -> None: ...
    def depart_abbreviation(self, node: nodes.Node) -> None: ...
    def visit_acronym(self, node: nodes.Node) -> None: ...
    def depart_acronym(self, node: nodes.Node) -> None: ...
    def visit_address(self, node: nodes.Node) -> None: ...
    def depart_address(self, node: nodes.Node) -> None: ...
    def visit_admonition(self, node: nodes.Node) -> None: ...
    def depart_admonition(self, node: Optional[nodes.Node] = ...) -> None: ...
    def visit_author(self, node: nodes.Node) -> None: ...
    def depart_author(self, node: nodes.Node) -> None: ...
    def visit_authors(self, node: nodes.Node) -> None: ...
    def depart_authors(self, node: nodes.Node) -> None: ...
    def visit_block_quote(self, node: nodes.Node) -> None: ...
    def depart_block_quote(self, node: nodes.Node) -> None: ...
    def visit_bullet_list(self, node: nodes.Node) -> None: ...
    def depart_bullet_list(self, node: nodes.Node) -> None: ...
    def visit_superscript(self, node: nodes.Node) -> None: ...
    def depart_superscript(self, node: nodes.Node) -> None: ...
    def visit_subscript(self, node: nodes.Node) -> None: ...
    def depart_subscript(self, node: nodes.Node) -> None: ...
    def visit_caption(self, node: nodes.Node) -> None: ...
    def depart_caption(self, node: nodes.Node) -> None: ...
    def visit_title_reference(self, node: nodes.Node) -> None: ...
    def depart_title_reference(self, node: nodes.Node) -> None: ...
    def visit_citation(self, node: nodes.Node) -> None: ...
    def depart_citation(self, node: nodes.Node) -> None: ...
    def visit_citation_reference(self, node: nodes.Node) -> None: ...
    def depart_citation_reference(self, node: nodes.Node) -> None: ...
    def visit_classifier(self, node: nodes.Node) -> None: ...
    def depart_classifier(self, node: nodes.Node) -> None: ...
    def visit_colspec(self, node: nodes.Node) -> None: ...
    def depart_colspec(self, node: nodes.Node) -> None: ...
    def visit_comment(self, node: nodes.Node) -> None: ...
    def depart_comment(self, node: nodes.Node) -> None: ...
    def visit_compound(self, node: nodes.Node) -> None: ...
    def depart_compound(self, node: nodes.Node) -> None: ...
    def visit_contact(self, node: nodes.Node) -> None: ...
    def depart_contact(self, node: nodes.Node) -> None: ...
    def visit_container(self, node: nodes.Node) -> None: ...
    def depart_container(self, node: nodes.Node) -> None: ...
    def visit_copyright(self, node: nodes.Node) -> None: ...
    def depart_copyright(self, node: nodes.Node) -> None: ...
    def visit_date(self, node: nodes.Node) -> None: ...
    def depart_date(self, node: nodes.Node) -> None: ...
    def visit_decoration(self, node: nodes.Node) -> None: ...
    def depart_decoration(self, node: nodes.Node) -> None: ...
    def visit_definition(self, node: nodes.Node) -> None: ...
    def depart_definition(self, node: nodes.Node) -> None: ...
    def visit_definition_list(self, node: nodes.Node) -> None: ...
    def depart_definition_list(self, node: nodes.Node) -> None: ...
    def visit_definition_list_item(self, node: nodes.Node) -> None: ...
    def depart_definition_list_item(self, node: nodes.Node) -> None: ...
    def visit_description(self, node: nodes.Node) -> None: ...
    def depart_description(self, node: nodes.Node) -> None: ...
    def visit_docinfo(self, node: nodes.Node) -> None: ...
    def depart_docinfo(self, node: nodes.Node) -> None: ...
    def visit_docinfo_item(self, node: nodes.Node, name: str) -> None: ...
    def depart_docinfo_item(self, node: nodes.Node) -> None: ...
    def visit_doctest_block(self, node: nodes.Node) -> None: ...
    def depart_doctest_block(self, node: nodes.Node) -> None: ...
    def visit_document(self, node: nodes.Node) -> None: ...
    def depart_document(self, node: nodes.Node) -> None: ...
    def visit_emphasis(self, node: nodes.Node) -> None: ...
    def depart_emphasis(self, node: nodes.Node) -> None: ...
    def insert_additional_table_colum_delimiters(self) -> None: ...
    def visit_entry(self, node: nodes.Node) -> None: ...
    def depart_entry(self, node: nodes.Node) -> None: ...
    def visit_row(self, node: nodes.Node) -> None: ...
    def depart_row(self, node: nodes.Node) -> None: ...
    def visit_enumerated_list(self, node: nodes.Node) -> None: ...
    def depart_enumerated_list(self, node: nodes.Node) -> None: ...
    def visit_field(self, node: nodes.Node) -> None: ...
    def depart_field(self, node: nodes.Node) -> None: ...
    def visit_field_argument(self, node: nodes.Node) -> None: ...
    def depart_field_argument(self, node: nodes.Node) -> None: ...
    def visit_field_body(self, node: nodes.Node) -> None: ...
    def depart_field_body(self, node: nodes.Node) -> None: ...
    def visit_field_list(self, node: nodes.Node) -> None: ...
    def depart_field_list(self, node: nodes.Node) -> None: ...
    def visit_field_name(self, node: nodes.Node) -> None: ...
    def depart_field_name(self, node: nodes.Node) -> None: ...
    def visit_figure(self, node: nodes.Node) -> None: ...
    def depart_figure(self, node: nodes.Node) -> None: ...
    def visit_footer(self, node: nodes.Node) -> None: ...
    def depart_footer(self, node: nodes.Node) -> None: ...
    def visit_footnote(self, node: nodes.Node) -> None: ...
    def depart_footnote(self, node: nodes.Node) -> None: ...
    def visit_footnote_reference(self, node: nodes.Node) -> None: ...
    def depart_footnote_reference(self, node: nodes.Node) -> None: ...
    def label_delim(self, node: nodes.Node, bracket: str, superscript: str) -> None: ...
    def visit_label(self, node: nodes.Node) -> None: ...
    def depart_label(self, node: nodes.Node) -> None: ...
    def visit_generated(self, node: nodes.Node) -> None: ...
    def depart_generated(self, node: nodes.Node) -> None: ...
    def visit_header(self, node: nodes.Node) -> None: ...
    def depart_header(self, node: nodes.Node) -> None: ...
    def to_latex_length(self, length_str: str, pxunit: Optional[Any] = ...) -> str: ...
    def visit_image(self, node: nodes.Node) -> None: ...
    def depart_image(self, node: nodes.Node) -> None: ...
    def visit_inline(self, node: nodes.Node) -> None: ...
    def depart_inline(self, node: nodes.Node) -> None: ...
    def visit_interpreted(self, node: nodes.Node) -> None: ...
    def depart_interpreted(self, node: nodes.Node) -> None: ...
    def visit_legend(self, node: nodes.Node) -> None: ...
    def depart_legend(self, node: nodes.Node) -> None: ...
    def visit_line(self, node: nodes.Node) -> None: ...
    def depart_line(self, node: nodes.Node) -> None: ...
    def visit_line_block(self, node: nodes.Node) -> None: ...
    def depart_line_block(self, node: nodes.Node) -> None: ...
    def visit_list_item(self, node: nodes.Node) -> None: ...
    def depart_list_item(self, node: nodes.Node) -> None: ...
    def visit_literal(self, node: nodes.Node) -> None: ...
    def depart_literal(self, node: nodes.Node) -> None: ...
    def is_plaintext(self, node: nodes.Node) -> bool: ...
    def visit_literal_block(self, node: nodes.Node) -> None: ...
    def depart_literal_block(self, node: nodes.Node) -> None: ...
    def visit_math(self, node: nodes.Node, math_env: str = ...) -> None: ...
    def depart_math(self, node: nodes.Node) -> None: ...
    def visit_math_block(self, node: nodes.Node) -> None: ...
    def depart_math_block(self, node: nodes.Node) -> None: ...
    def visit_option(self, node: nodes.Node) -> None: ...
    def depart_option(self, node: nodes.Node) -> None: ...
    def visit_option_argument(self, node: nodes.Node) -> None: ...
    def depart_option_argument(self, node: nodes.Node) -> None: ...
    def visit_option_group(self, node: nodes.Node) -> None: ...
    def depart_option_group(self, node: nodes.Node) -> None: ...
    def visit_option_list(self, node: nodes.Node) -> None: ...
    def depart_option_list(self, node: nodes.Node) -> None: ...
    def visit_option_list_item(self, node: nodes.Node) -> None: ...
    def depart_option_list_item(self, node: nodes.Node) -> None: ...
    def visit_option_string(self, node: nodes.Node) -> None: ...
    def depart_option_string(self, node: nodes.Node) -> None: ...
    def visit_organization(self, node: nodes.Node) -> None: ...
    def depart_organization(self, node: nodes.Node) -> None: ...
    def visit_paragraph(self, node: nodes.Node) -> None: ...
    def depart_paragraph(self, node: nodes.Node) -> None: ...
    def visit_problematic(self, node: nodes.Node) -> None: ...
    def depart_problematic(self, node: nodes.Node) -> None: ...
    def visit_raw(self, node: nodes.Node) -> None: ...
    def depart_raw(self, node: nodes.Node) -> None: ...
    def has_unbalanced_braces(self, string: str) -> bool: ...
    def visit_reference(self, node: nodes.Node) -> None: ...
    def depart_reference(self, node: nodes.Node) -> None: ...
    def visit_revision(self, node: nodes.Node) -> None: ...
    def depart_revision(self, node: nodes.Node) -> None: ...
    def visit_rubric(self, node: nodes.Node) -> None: ...
    def depart_rubric(self, node: nodes.Node) -> None: ...
    def visit_section(self, node: nodes.Node) -> None: ...
    def depart_section(self, node: nodes.Node) -> None: ...
    def visit_sidebar(self, node: nodes.Node) -> None: ...
    def depart_sidebar(self, node: nodes.Node) -> None: ...
    attribution_formats: Dict[str, Tuple[str, str]] = ...
    def visit_attribution(self, node: nodes.Node) -> None: ...
    def depart_attribution(self, node: nodes.Node) -> None: ...
    def visit_status(self, node: nodes.Node) -> None: ...
    def depart_status(self, node: nodes.Node) -> None: ...
    def visit_strong(self, node: nodes.Node) -> None: ...
    def depart_strong(self, node: nodes.Node) -> None: ...
    def visit_substitution_definition(self, node: nodes.Node) -> None: ...
    def visit_substitution_reference(self, node: nodes.Node) -> None: ...
    def visit_subtitle(self, node: nodes.Node) -> None: ...
    def depart_subtitle(self, node: nodes.Node) -> None: ...
    def visit_system_message(self, node: nodes.Node) -> None: ...
    def depart_system_message(self, node: nodes.Node) -> None: ...
    def visit_table(self, node: nodes.Node) -> None: ...
    def depart_table(self, node: nodes.Node) -> None: ...
    def visit_target(self, node: nodes.Node) -> None: ...
    def depart_target(self, node: nodes.Node) -> None: ...
    def visit_tbody(self, node: nodes.Node) -> None: ...
    def depart_tbody(self, node: nodes.Node) -> None: ...
    def visit_term(self, node: nodes.Node) -> None: ...
    def depart_term(self, node: nodes.Node) -> None: ...
    def visit_tgroup(self, node: nodes.Node) -> None: ...
    def depart_tgroup(self, node: nodes.Node) -> None: ...
    def thead_depth(self) -> int: ...
    def visit_thead(self, node: nodes.Node) -> None: ...
    def depart_thead(self, node: nodes.Node) -> None: ...
    def visit_title(self, node: nodes.Node) -> None: ...
    def depart_title(self, node: nodes.Node) -> None: ...
    def minitoc(self, node: nodes.Node, title: str, depth: int) -> None: ...
    def visit_topic(self, node: nodes.Node) -> None: ...
    def depart_topic(self, node: nodes.Node) -> None: ...
    def visit_transition(self, node: nodes.Node) -> None: ...
    def depart_transition(self, node: nodes.Node) -> None: ...
    def visit_version(self, node: nodes.Node) -> None: ...
    def depart_version(self, node: nodes.Node) -> None: ...
    def unimplemented_visit(self, node: nodes.Node) -> None: ...

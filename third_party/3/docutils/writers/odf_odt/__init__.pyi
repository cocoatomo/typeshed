# Stubs for docutils.writers.odf_odt (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .pygmentsformatter import OdtPygmentsLaTeXFormatter, OdtPygmentsProgFormatter
from docutils import nodes, writers
from docutils.readers import standalone
from typing import Any, Optional

VERSION: str
__docformat__: str
IMAGE_NAME_COUNTER: Any
WhichElementTree: str
s1: str

class PIL: ...

class _ElementInterfaceWrapper(_ElementInterface):
    def __init__(self, tag, attrib: Optional[Any] = ...) -> None: ...
    def setparent(self, parent): ...
    def getparent(self): ...

SPACES_PATTERN: Any
TABS_PATTERN: Any
FILL_PAT1: Any
FILL_PAT2: Any
TABLESTYLEPREFIX: str
TABLENAMEDEFAULT: Any
TABLEPROPERTYNAMES: Any
GENERATOR_DESC: str
NAME_SPACE_1: str
CONTENT_NAMESPACE_DICT: Any
CNSD: Any
STYLES_NAMESPACE_DICT: Any
SNSD: Any
MANIFEST_NAMESPACE_DICT: Any
MANNSD: Any
META_NAMESPACE_DICT: Any
METNSD: Any
CONTENT_NAMESPACE_ATTRIB: Any
STYLES_NAMESPACE_ATTRIB: Any
MANIFEST_NAMESPACE_ATTRIB: Any
META_NAMESPACE_ATTRIB: Any

def Element(tag, attrib: Optional[Any] = ..., nsmap: Optional[Any] = ..., nsdict: Any = ...): ...
def SubElement(parent, tag, attrib: Optional[Any] = ..., nsmap: Optional[Any] = ..., nsdict: Any = ...): ...
def fix_ns(tag, attrib, nsdict): ...
def add_ns(tag, nsdict: Any = ...): ...
def ToString(et): ...
def escape_cdata(text): ...

WORD_SPLIT_PAT1: Any

def split_words(line): ...

class TableStyle:
    border: Any = ...
    backgroundcolor: Any = ...
    def __init__(self, border: Optional[Any] = ..., backgroundcolor: Optional[Any] = ...) -> None: ...
    def get_border_(self): ...
    border_: Any = ...
    def set_border_(self, border): ...
    def get_backgroundcolor_(self): ...
    backgroundcolor_: Any = ...
    def set_backgroundcolor_(self, backgroundcolor): ...

BUILTIN_DEFAULT_TABLE_STYLE: Any

class ListLevel:
    level: Any = ...
    sibling_level: Any = ...
    nested_level: Any = ...
    def __init__(self, level, sibling_level: bool = ..., nested_level: bool = ...) -> None: ...
    def set_sibling(self, sibling_level): ...
    def get_sibling(self): ...
    def set_nested(self, nested_level): ...
    def get_nested(self): ...
    def set_level(self, level): ...
    def get_level(self): ...

class Writer(writers.Writer):
    MIME_TYPE: str = ...
    EXTENSION: str = ...
    supported: Any = ...
    default_stylesheet: Any = ...
    default_stylesheet_path: Any = ...
    default_template: str = ...
    default_template_path: Any = ...
    settings_spec: Any = ...
    settings_defaults: Any = ...
    relative_path_settings: Any = ...
    config_section: str = ...
    config_section_dependencies: Any = ...
    translator_class: Any = ...
    def __init__(self) -> None: ...
    settings: Any = ...
    visitor: Any = ...
    output: Any = ...
    def translate(self): ...
    def assemble_my_parts(self): ...
    def update_stylesheet(self, stylesheet_root, language_code, region_code): ...
    def write_zip_str(self, zfile, name, bytes, compress_type: Any = ...): ...
    def store_embedded_files(self, zfile): ...
    def get_settings(self): ...
    def get_stylesheet(self): ...
    def copy_from_stylesheet(self, outzipfile): ...
    def assemble_parts(self): ...
    def create_manifest(self): ...
    def create_meta(self): ...

class ODFTranslator(nodes.GenericNodeVisitor):
    used_styles: Any = ...
    settings: Any = ...
    language_code: Any = ...
    language: Any = ...
    format_map: Any = ...
    section_level: int = ...
    section_count: int = ...
    content_tree: Any = ...
    current_element: Any = ...
    automatic_styles: Any = ...
    body_text_element: Any = ...
    paragraph_style_stack: Any = ...
    list_style_stack: Any = ...
    table_count: int = ...
    column_count: Any = ...
    trace_level: int = ...
    optiontablestyles_generated: bool = ...
    field_name: Any = ...
    field_element: Any = ...
    title: Any = ...
    image_count: int = ...
    image_style_count: int = ...
    image_dict: Any = ...
    embedded_file_list: Any = ...
    syntaxhighlighting: int = ...
    syntaxhighlight_lexer: str = ...
    header_content: Any = ...
    footer_content: Any = ...
    in_header: bool = ...
    in_footer: bool = ...
    blockstyle: str = ...
    in_table_of_contents: bool = ...
    table_of_content_index_body: Any = ...
    list_level: int = ...
    def_list_level: int = ...
    footnote_ref_dict: Any = ...
    footnote_list: Any = ...
    footnote_chars_idx: int = ...
    footnote_level: int = ...
    pending_ids: Any = ...
    in_paragraph: bool = ...
    found_doc_title: bool = ...
    bumped_list_level_stack: Any = ...
    meta_dict: Any = ...
    line_block_level: int = ...
    line_indent_level: int = ...
    citation_id: Any = ...
    style_index: int = ...
    str_stylesheet: str = ...
    str_stylesheetcontent: str = ...
    dom_stylesheet: Any = ...
    table_styles: Any = ...
    in_citation: bool = ...
    inline_style_count_stack: Any = ...
    def __init__(self, document) -> None: ...
    def get_str_stylesheet(self): ...
    dom_stylesheetcontent: Any = ...
    def retrieve_styles(self, extension): ...
    def extract_table_styles(self, styles_str): ...
    def get_property(self, stylenode): ...
    def add_doc_title(self): ...
    def find_first_text_p(self, el): ...
    def attach_page_style(self, el): ...
    def rststyle(self, name, parameters: Any = ...): ...
    def generate_content_element(self, root): ...
    def setup_page(self): ...
    def get_dom_stylesheet(self): ...
    def setup_paper(self, root_el): ...
    def add_header_footer(self, root_el): ...
    code_none: Any = ...
    code_field: Any = ...
    code_text: Any = ...
    field_pat: Any = ...
    def create_custom_headfoot(self, parent, text, style_name, automatic_styles): ...
    def make_field_element(self, parent, text, style_name, automatic_styles): ...
    def split_field_specifiers_iter(self, text): ...
    def astext(self): ...
    def content_astext(self): ...
    def set_title(self, title): ...
    def get_title(self): ...
    def set_embedded_file_list(self, embedded_file_list): ...
    def get_embedded_file_list(self): ...
    def get_meta_dict(self): ...
    def process_footnotes(self): ...
    def append_child(self, tag, attrib: Optional[Any] = ..., parent: Optional[Any] = ...): ...
    def append_p(self, style, text: Optional[Any] = ...): ...
    def append_pending_ids(self, el): ...
    def set_current_element(self, el): ...
    def set_to_parent(self): ...
    def generate_labeled_block(self, node, label): ...
    def generate_labeled_line(self, node, label): ...
    def encode(self, text): ...
    def dispatch_visit(self, node): ...
    def handle_basic_atts(self, node): ...
    def default_visit(self, node): ...
    def default_departure(self, node): ...
    def visit_Text(self, node): ...
    def depart_Text(self, node): ...
    def visit_address(self, node): ...
    def depart_address(self, node): ...
    def visit_author(self, node): ...
    def depart_author(self, node): ...
    def visit_authors(self, node): ...
    def depart_authors(self, node): ...
    def visit_contact(self, node): ...
    def depart_contact(self, node): ...
    def visit_copyright(self, node): ...
    def depart_copyright(self, node): ...
    def visit_date(self, node): ...
    def depart_date(self, node): ...
    def visit_organization(self, node): ...
    def depart_organization(self, node): ...
    def visit_status(self, node): ...
    def depart_status(self, node): ...
    def visit_revision(self, node): ...
    def depart_revision(self, node): ...
    def visit_version(self, node): ...
    def depart_version(self, node): ...
    def visit_attribution(self, node): ...
    def depart_attribution(self, node): ...
    def visit_block_quote(self, node): ...
    def depart_block_quote(self, node): ...
    def visit_bullet_list(self, node): ...
    def depart_bullet_list(self, node): ...
    def visit_caption(self, node): ...
    def depart_caption(self, node): ...
    def visit_comment(self, node): ...
    def depart_comment(self, node): ...
    def visit_compound(self, node): ...
    def depart_compound(self, node): ...
    def visit_container(self, node): ...
    def depart_container(self, node): ...
    def visit_decoration(self, node): ...
    def depart_decoration(self, node): ...
    def visit_definition_list(self, node): ...
    def depart_definition_list(self, node): ...
    def visit_definition_list_item(self, node): ...
    def depart_definition_list_item(self, node): ...
    def visit_term(self, node): ...
    def depart_term(self, node): ...
    def visit_definition(self, node): ...
    def depart_definition(self, node): ...
    def visit_classifier(self, node): ...
    def depart_classifier(self, node): ...
    def visit_document(self, node): ...
    def depart_document(self, node): ...
    def visit_docinfo(self, node): ...
    def depart_docinfo(self, node): ...
    def visit_emphasis(self, node): ...
    def depart_emphasis(self, node): ...
    def visit_enumerated_list(self, node): ...
    def depart_enumerated_list(self, node): ...
    def visit_list_item(self, node): ...
    def depart_list_item(self, node): ...
    def visit_header(self, node): ...
    def depart_header(self, node): ...
    def visit_footer(self, node): ...
    def depart_footer(self, node): ...
    def visit_field(self, node): ...
    def depart_field(self, node): ...
    def visit_field_list(self, node): ...
    def depart_field_list(self, node): ...
    def visit_field_name(self, node): ...
    def depart_field_name(self, node): ...
    def visit_field_body(self, node): ...
    def depart_field_body(self, node): ...
    def visit_figure(self, node): ...
    def depart_figure(self, node): ...
    save_footnote_current: Any = ...
    def visit_footnote(self, node): ...
    def depart_footnote(self, node): ...
    footnote_chars: Any = ...
    def visit_footnote_reference(self, node): ...
    def depart_footnote_reference(self, node): ...
    def visit_citation(self, node): ...
    def depart_citation(self, node): ...
    def visit_citation_reference(self, node): ...
    def depart_citation_reference(self, node): ...
    def visit_label(self, node): ...
    def depart_label(self, node): ...
    def visit_generated(self, node): ...
    def depart_generated(self, node): ...
    def check_file_exists(self, path): ...
    def visit_image(self, node): ...
    def depart_image(self, node): ...
    def get_image_width_height(self, node, attr): ...
    def convert_to_cm(self, size): ...
    def get_image_scale(self, node): ...
    def get_image_scaled_width_height(self, node, source): ...
    def get_page_width(self): ...
    def generate_figure(self, node, source, destination, current_element): ...
    def generate_image(self, node, source, destination, current_element, frame_attrs: Optional[Any] = ...): ...
    def is_in_table(self, node): ...
    def visit_legend(self, node): ...
    def depart_legend(self, node): ...
    def visit_line_block(self, node): ...
    def depart_line_block(self, node): ...
    def visit_line(self, node): ...
    def depart_line(self, node): ...
    def visit_literal(self, node): ...
    def depart_literal(self, node): ...
    def visit_inline(self, node): ...
    def depart_inline(self, node): ...
    def fill_line(self, line): ...
    def fill_func1(self, matchobj): ...
    def fill_func2(self, matchobj): ...
    def visit_literal_block(self, node): ...
    def depart_literal_block(self, node): ...
    visit_doctest_block: Any = ...
    depart_doctest_block: Any = ...
    def visit_math(self, node): ...
    def depart_math(self, node): ...
    def visit_math_block(self, node): ...
    def depart_math_block(self, node): ...
    def visit_meta(self, node): ...
    def depart_meta(self, node): ...
    def visit_option_list(self, node): ...
    def depart_option_list(self, node): ...
    def visit_option_list_item(self, node): ...
    def depart_option_list_item(self, node): ...
    def visit_option_group(self, node): ...
    def depart_option_group(self, node): ...
    def visit_option(self, node): ...
    def depart_option(self, node): ...
    def visit_option_string(self, node): ...
    def depart_option_string(self, node): ...
    def visit_option_argument(self, node): ...
    def depart_option_argument(self, node): ...
    def visit_description(self, node): ...
    def depart_description(self, node): ...
    def visit_paragraph(self, node): ...
    def depart_paragraph(self, node): ...
    def visit_problematic(self, node): ...
    def depart_problematic(self, node): ...
    def visit_raw(self, node): ...
    def depart_raw(self, node): ...
    def visit_reference(self, node): ...
    def depart_reference(self, node): ...
    def visit_rubric(self, node): ...
    def depart_rubric(self, node): ...
    def visit_section(self, node, move_ids: int = ...): ...
    def depart_section(self, node): ...
    def visit_strong(self, node): ...
    def depart_strong(self, node): ...
    def visit_substitution_definition(self, node): ...
    def depart_substitution_definition(self, node): ...
    def visit_system_message(self, node): ...
    def depart_system_message(self, node): ...
    def get_table_style(self, node): ...
    current_table_style: Any = ...
    table_width: float = ...
    def visit_table(self, node): ...
    def depart_table(self, node): ...
    def visit_tgroup(self, node): ...
    def depart_tgroup(self, node): ...
    def visit_colspec(self, node): ...
    def depart_colspec(self, node): ...
    in_thead: bool = ...
    def visit_thead(self, node): ...
    def depart_thead(self, node): ...
    def visit_row(self, node): ...
    def depart_row(self, node): ...
    def visit_entry(self, node): ...
    def depart_entry(self, node): ...
    def visit_tbody(self, node): ...
    def depart_tbody(self, node): ...
    def visit_target(self, node): ...
    def depart_target(self, node): ...
    def visit_title(self, node, move_ids: int = ..., title_type: str = ...): ...
    def depart_title(self, node): ...
    def visit_subtitle(self, node, move_ids: int = ...): ...
    def depart_subtitle(self, node): ...
    def visit_title_reference(self, node): ...
    def depart_title_reference(self, node): ...
    def generate_table_of_content_entry_template(self, el1): ...
    def find_title_label(self, node, class_type, label_key): ...
    save_current_element: Any = ...
    def visit_topic(self, node): ...
    def depart_topic(self, node): ...
    def update_toc_page_numbers(self, el): ...
    def update_toc_collect(self, el, level, collection): ...
    def update_toc_add_numbers(self, collection): ...
    def visit_transition(self, node): ...
    def depart_transition(self, node): ...
    def visit_warning(self, node): ...
    def depart_warning(self, node): ...
    def visit_attention(self, node): ...
    depart_attention: Any = ...
    def visit_caution(self, node): ...
    depart_caution: Any = ...
    def visit_danger(self, node): ...
    depart_danger: Any = ...
    def visit_error(self, node): ...
    depart_error: Any = ...
    def visit_hint(self, node): ...
    depart_hint: Any = ...
    def visit_important(self, node): ...
    depart_important: Any = ...
    def visit_note(self, node): ...
    depart_note: Any = ...
    def visit_tip(self, node): ...
    depart_tip: Any = ...
    def visit_admonition(self, node): ...
    depart_admonition: Any = ...
    def generate_admonition(self, node, label, title: Optional[Any] = ...): ...
    def visit_subscript(self, node): ...
    def depart_subscript(self, node): ...
    def visit_superscript(self, node): ...
    def depart_superscript(self, node): ...

class Reader(standalone.Reader):
    def get_transforms(self): ...
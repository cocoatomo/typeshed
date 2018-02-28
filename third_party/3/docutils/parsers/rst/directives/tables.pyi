# Stubs for docutils.parsers.rst.directives.tables (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import csv
from docutils.parsers.rst import Directive
from typing import Any

__docformat__: str

def align(argument): ...

class Table(Directive):
    optional_arguments: int = ...
    final_argument_whitespace: bool = ...
    option_spec: Any = ...
    has_content: bool = ...
    def make_title(self): ...
    def process_header_option(self): ...
    def check_table_dimensions(self, rows, header_rows, stub_columns): ...
    @property
    def widths(self): ...
    def get_column_widths(self, max_cols): ...
    def extend_short_rows_with_empty_cells(self, columns, parts): ...

class RSTTable(Table):
    def run(self): ...

class CSVTable(Table):
    option_spec: Any = ...
    class DocutilsDialect(csv.Dialect):
        delimiter: str = ...
        quotechar: str = ...
        doublequote: bool = ...
        skipinitialspace: bool = ...
        strict: bool = ...
        lineterminator: str = ...
        quoting: Any = ...
        escapechar: Any = ...
        def __init__(self, options) -> None: ...
    class HeaderDialect(csv.Dialect):
        delimiter: str = ...
        quotechar: str = ...
        escapechar: str = ...
        doublequote: bool = ...
        skipinitialspace: bool = ...
        strict: bool = ...
        lineterminator: str = ...
        quoting: Any = ...
    def check_requirements(self): ...
    def run(self): ...
    def get_csv_data(self): ...
    def decode_from_csv(s): ...
    def encode_for_csv(s): ...
    def decode_from_csv(s): ...
    def encode_for_csv(s): ...
    decode_from_csv: Any = ...
    encode_for_csv: Any = ...
    def parse_csv_data_into_rows(self, csv_data, dialect, source): ...

class ListTable(Table):
    option_spec: Any = ...
    def run(self): ...
    def check_list_content(self, node): ...
    def build_table_from_list(self, table_data, col_widths, header_rows, stub_columns): ...

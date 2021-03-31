"""Utility functions for wrangling data."""

__author__ = "730395244"


from csv import DictReader


DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_27.csv"


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Values of columns."""
    column_v: list[str] = []
    i: int = 0
    while i < len(table):
        column_v.append(table[i][column])
        i += 1
    return column_v


def columnar(table_row: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table."""
    dict_columns: dict[str, list[str]] = {}
    for row in table_row[0]:
        dict_columns[row] = column_values(table_row, row)
    return dict_columns


def head(col_table: dict[str, list[str]], number_r: int) -> dict[str, list[str]]:
    """Narrow down the table."""
    dict_head: dict[str, list[str]] = {}
    for column in col_table:
        dict_head[column] = [] 
        for i in range(0, number_r):
            dict_head[column].append(col_table[column][i])
    return dict_head


def select(m_col_table: dict[str, list[str]], names_c: list[str]) -> dict[str, list[str]]:
    """New column based table with only a specific subset of the og column."""
    dict_select: dict[str, list[str]] = {}
    for columns in names_c:
        dict_select[columns] = m_col_table[columns]
    return dict_select 


def count(count_list: list[str]) -> dict[str, int]:
    """Function to count nuber of times value is in list."""
    dict_count: dict[str, int] = {}
    for item in count_list:
        if item in dict_count:
            dict_count[item] += 1
        else:
            dict_count[item] = 1
    return dict_count

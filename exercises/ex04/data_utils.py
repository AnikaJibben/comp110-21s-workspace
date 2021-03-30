"""Utility functions for wrangling data."""

__author__ = "73039524"


from csv import DictReader

DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_27.csv"

def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
        for column in row:
            row[column] = column
    def column_values(table: list[dict[str, str]], column: str) -> list[str]:
        """Values of columns."""
        column_v: list[str] = []
        for row in table:
            for dictionary in row:
                for key in dictionary:
                    if key == column:
                        column_v.append(key[value])
        return column_v
    column_values(rows, "subject_age")
    return rows


# TODO: Define the other functions here.

def columnar(v: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table."""
    dict_columns: dict[str, list[str]] = dict()
    for columns in dict_columns:
        
    return dict_columns


def head(x: dict[str, list[str]], number_r: int) -> dict[str, list[str]]
    """Produce a new table."""
    dict_head: dict[str,list[str]] = dict()
    for in 
        list_head: list[str] =[]
        for N in list_head:
            list_head.append(N)
    
    return x


def select(y: dict[str, list[str]], names_c: list[str]) -> dict[str, list[str]]:
    """New column based table with only a specific subset of the og column."""
    dict_select: dict[str, list[str]] = dict()
    for columns in names_c:

    return y 

def count(a: list[str]) -> dict[str, int]:
    """Function to count nuber of times value is in list."""
    dict_count: dict[str, int] = dict()
    for 
    return a


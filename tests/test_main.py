import pandas as pd

from src.data_processor.main import load_csv, remove_duplicates, drop_missing, fill_missing, summary_stats, format_stats, save_csv

def test_load_csv_reads_file(tmp_path):
    csv_file = tmp_path / 'tiny.csv'
    csv_file.write_text('id,name\n1,Alice\n2,Bob\n')

    df = load_csv(csv_file)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ['id', 'name']


def test_remove_duplicates_collapses_identical_rows():
    df = pd.DataFrame({
        'id': [0, 1, 1, 2],
        'name': ['Alice', 'Bob', 'Bob', 'Andrew']
    })

    result = remove_duplicates(df)

    assert len(result) == 3
    assert result['name'].tolist() == ['Alice', 'Bob', 'Andrew']
    assert result['id'].tolist() == [0, 1, 2]


def test_drop_missing_removes_rows_with_nan():
    df = pd.DataFrame({
        'id': [0, 1, None, None, 4],
        'name': ['Alice', 'Bob', None, 'Andrew', 'Stephan']
    })

    result = drop_missing(df)

    assert len(result) == 3
    assert result['name'].tolist() == ['Alice', 'Bob', 'Stephan']
    assert result['id'].tolist() == [0, 1, 4]


def test_fill_missing_replaces_nan_with_value():
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', None, 'Andrew']
    })

    result = fill_missing(df, value='Unknown')

    assert len(result) == 3
    assert result['id'].tolist() == [1, 2, 3]
    assert result['name'].tolist() == ['Alice', 'Unknown', 'Andrew']


def test_summary_stats_returns_rows_columns_and_details():
    df = pd.DataFrame({
        'a': [1, 2, None],
        'b': ['x', None, 'z']
    })

    result = summary_stats(df)
    details = result['column_details']

    assert result['rows'] == 3
    assert result['columns'] == 2
    assert details['a']['missing'] == 1
    assert details['a']['non_missing'] == 2
    assert details['b']['missing'] == 1
    assert details['b']['non_missing'] == 2


def test_format_stats_return_lines_with_rows_columns_and_details():
    stats = {
        'rows': 3,
        'columns': 2,
        'column_details':{
            'a': {'dtype': 'int64',  'non_missing': 3, 'missing': 0},
            'b': {'dtype': 'object', 'non_missing': 2, 'missing': 1},
        }
    }

    text = format_stats(stats)

    assert 'Summary' in text
    assert 'Rows:' in text
    assert '3' in text
    assert 'Columns:' in text
    assert '2' in text

    assert 'a' in text
    assert 'b' in text
    assert 'int64' in text
    assert 'object' in text


def test_save_csv_writes_dataframe_to_file(tmp_path):
    df = pd.DataFrame({
        'id':   [1, 2, 3],
        'name': ['Alice', 'Bob', 'Carol'],
    })

    output_path = tmp_path / 'out.csv'
    save_csv(df, output_path)

    assert output_path.exists()

    loaded = pd.read_csv(output_path)
    assert len(loaded) == 3
    assert loaded['id'].tolist() == [1, 2, 3]
    assert loaded['name'].tolist() == ['Alice', 'Bob', 'Carol']


def test_save_csv_excludes_index_column(tmp_path):
    df = pd.DataFrame({'a': [1, 2]})
    output_path = tmp_path / 'out.csv'

    save_csv(df, output_path)
    loaded = pd.read_csv(output_path)

    assert list(loaded.columns) == ['a']
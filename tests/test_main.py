import pandas as pd

from src.data_processor.main import load_csv, remove_duplicates, drop_missing, fill_missing, summary_stats

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


def test_summary_stats_returns_shape():
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': ['x', 'y', 'z']
    })

    result = summary_stats(df)

    assert result['rows'] == 3
    assert result['columns'] == 2
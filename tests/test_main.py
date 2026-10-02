import pandas as pd

from src.data_processor.main import load_csv, remove_duplicates

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
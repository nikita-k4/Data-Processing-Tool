import pandas as pd

from src.data_processor.main import load_csv

def test_load_csv_reads_file(tmp_path):
    csv_file = tmp_path / 'tiny.csv'
    csv_file.write_text('id,name\n1,Alice\n2,Bob\n2')

    df = load_csv(csv_file)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ['id', 'name']
    
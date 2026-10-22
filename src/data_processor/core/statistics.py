import pandas as pd



def summary_stats(df: pd.DataFrame) -> dict:
    non_missing_counts = df.notna().sum()
    missing_counts = df.isna().sum()
    dtypes = df.dtypes

    column_details = {}
    for col_name in df.columns:
        column_details[col_name] = {
            'dtype': str(dtypes[col_name]),
            'non_missing': int(non_missing_counts[col_name]),
            'missing': int(missing_counts[col_name]),
        }
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'column_details': column_details,
    }


def format_stats(stats: dict) -> str:
    lines = []
    lines.append("Summary")
    lines.append("=======")
    lines.append(f"Rows: {stats['rows']}")
    lines.append(f"Columns: {stats['columns']}")
    lines.append("")
    lines.append("Column details:")
    for col_name, details in stats['column_details'].items():
        lines.append(
            f"  {col_name:<6} "
            f"dtype={details['dtype']:<8}"
            f"non_missing={details['non_missing']:<3}"
            f"missing={details['missing']}"
        )

    return "\n".join(lines)
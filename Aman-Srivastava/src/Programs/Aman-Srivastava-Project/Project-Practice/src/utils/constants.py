from pathlib import Path

p = Path(__file__).resolve().parent.parent

method_path = p / "data_extraction"
files_path = method_path / "csv_data"
dataset_path = files_path / "individual_contribution.csv"

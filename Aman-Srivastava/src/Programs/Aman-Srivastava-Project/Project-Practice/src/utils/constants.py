from pathlib import Path

p = Path(__file__).resolve().parent.parent

files_path = p / "csv_data"
dataset_path = files_path / "individual_contribution.csv"

from pathlib import Path

path = Path(__file__).resolve().parent.parent
data_path = path / "dataset"
dataset = data_path / "heart-disease-dataset.csv"

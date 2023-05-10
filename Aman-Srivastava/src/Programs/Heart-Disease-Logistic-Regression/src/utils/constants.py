from pathlib import Path

p = Path(__file__).resolve().parent.parent
src_path = p / "heart_disease_model"
file_path = src_path / "csv"
dataset_path = file_path / "heart-disease-dataset.csv"
print(dataset_path)

import pathlib

path = pathlib.Path(__file__).resolve().parent.parent.parent
print(path)
dataset_path = path/"dataset"
print(dataset_path)
file_path = dataset_path/"fish.csv"
print(file_path)
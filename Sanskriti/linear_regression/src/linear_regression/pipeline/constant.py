import pathlib

path = pathlib.Path(__file__,encoding ="latin-1").resolve().parent.parent.parent
print(path)
dataset_path = path/"dataset"
print(dataset_path)
file_path = dataset_path/"laptop_price.csv"
print(file_path)
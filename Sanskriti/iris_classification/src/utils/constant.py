import pathlib

path = pathlib.Path(__file__).resolve().parent.parent
dataset_path = path/"dataset"
file_path = dataset_path/"iiris.csv"
model_path = path/"model"
pickle_file_path = model_path/"iris.pkl"



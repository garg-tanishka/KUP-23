from pathlib import Path

p = Path(__file__).resolve().parent.parent
module_path = p/"csv"
dataset_path = module_path/"iris.csv"


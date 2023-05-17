from pathlib import Path

path = Path(__file__).resolve().parent.parent
data_dir = path / 'dataset'
dataset_path = data_dir / 'mall_customer.csv'
util_path = path / "utils"
figure_path = util_path / "visual_figures"

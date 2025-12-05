from pathlib import Path
from datetime import datetime

NOW = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
PACKAGE_DIR = Path(__file__).parent
PROJECT_ROOT = PACKAGE_DIR.parent
DATA_DIR = PROJECT_ROOT / 'dataset'
LOG_TEMPLATE = f'[LOG - {NOW}]'
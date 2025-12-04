from src.config import PROJECT_ROOT, DATA_DIR
from src.main import run
from src.utils import log

# Package metadata

__version__ = '0.1.0'

# All exports

__all__ = [
    # Main
    'run',
    # Utils
    'log',
    # Paths
    'PROJECT_ROOT',
    'DATA_DIR'
]

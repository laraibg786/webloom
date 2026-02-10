from importlib.metadata import PackageNotFoundError, version

from webloom._cli import main
from webloom.utils import add_numbers, fibonacci, is_even, multiply_numbers

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "__version__",
    "add_numbers",
    "fibonacci",
    "is_even",
    "main",
    "multiply_numbers",
]

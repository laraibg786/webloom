from importlib.metadata import PackageNotFoundError, version

from webloom.utils import add_numbers, multiply_numbers, is_even, fibonacci

try:  # noqa: RUF067
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"

def main() -> None:
    print("Hello from webloom!")
    print(__version__)

__all__ = ["add_numbers", "multiply_numbers", "is_even", "fibonacci", "main", "__version__"]

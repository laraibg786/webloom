"""CLI entry point for Webloom."""

from importlib.metadata import PackageNotFoundError, version


def main() -> None:
    """Run the webloom CLI."""
    print("Hello from webloom!")
    try:
        print(version("webloom"))
    except PackageNotFoundError:
        print("unknown")

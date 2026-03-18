import importlib.metadata

# Import implementation modules
from correcthorse.correcthorse import clear_cache, hash, random, words

try:
    __version__ = importlib.metadata.version("correcthorse")
except importlib.metadata.PackageNotFoundError:  # pragma: nocover
    # Local copy, not installed with pip
    __version__ = "9999"


__all__ = ("__version__", "clear_cache", "hash", "random", "words")

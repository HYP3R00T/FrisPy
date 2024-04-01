"""Frispy module."""

from disc import Disc
from equations_of_motion import EOM
from model import Model

# TODO: figure out how to use poetry-bumpversion
# to keep this in line with the pyproject.toml
__version__ = "2.0.0"


__all__ = ["Disc", "EOM", "Model"]
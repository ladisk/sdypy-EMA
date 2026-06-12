from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("sdypy-EMA")
except PackageNotFoundError:  # source checkout without installed metadata
    __version__ = "0+unknown"

from .EMA import Model
from .tools import *

from . import stabilization
from . import normal_modes
from . import pole_picking

import warnings

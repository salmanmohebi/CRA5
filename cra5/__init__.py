# Copyright (c) 2021-2024, InterDigital Communications, Inc
# All rights reserved.

"""
CRA5: A large compression model for weather and climate data.
"""

__version__ = "0.0.3.dev1"

try:
    from .version import __version__, git_version
except ImportError:
    pass

__all__ = ["__version__"]

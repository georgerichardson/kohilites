try:
    from .kohilites import MetaData
except ModuleNotFoundError:  # Workaround for setup.py
    pass


# def path_to_init(_file=__file__, cast_to_str=False):
#     """Return the path to this file"""
#     from pathlib import Path

#     path = Path(_file).resolve().parent
#     return str(path) if cast_to_str else path


# def load_current_version():
#     """Load the current version of this package."""
#     path_to_version = path_to_init(__file__) / "VERSION"
#     with open(path_to_version) as f:
#         v = f.read()
#     return v


# try:
#     __version__ = load_current_version()
# except FileNotFoundError:  # Not needed on PyPI, where VERSION has not been bundled
#     pass


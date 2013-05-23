try:
    from ._speedups import pack_command
except ImportError:
    from ._backup import pack_command

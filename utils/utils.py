from typing import Any


def format_dict_strs(thing: Any, **kwargs) -> Any:
    match thing:
        case str():
            return thing.format(**kwargs)
        case list():
            return [format_dict_strs(t, **kwargs) for t in thing]
        case dict():
            return {k.format(**kwargs) if isinstance(k, str) else k: format_dict_strs(v, **kwargs) for k, v in thing.items()}
        case _:
            return thing

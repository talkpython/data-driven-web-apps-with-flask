from typing import Optional


def try_int(text) -> Optional[int]:
    try:
        return int(text)
    except:
        return 0

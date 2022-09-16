from typing import Optional

import bson


def try_int(text) -> Optional[int]:
    try:
        return int(text)
    except:
        return None


def try_object_id(text) -> Optional[bson.ObjectId]:
    try:
        return bson.ObjectId(text)
    except:
        return None

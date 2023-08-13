from typing import TYPE_CHECKING, AnyStr

if TYPE_CHECKING:
    from _typeshed import SupportsWrite, SupportsRead

CANONICAL: int
LEGACY: int
RELAXED: int

def dump(bson, fp: SupportsWrite[str]) -> None:
    """Decode the BSON bytes object `bson` and write the resulting MongoDB
    Extended JSON 2.0 relaxed mode document to `fp` (a `.write()`-supporting
    file-or-buffer-like object).

    Accepts a keyword argument `mode` which can be one of `bsonjs.RELAXED`
    `bsonjs.CANONICAL`, or `bsonjs.LEGACY`. Where `RELAXED` and `CANONICAL`
    correspond to the MongoDB Extended JSON 2.0 modes and `LEGACY` uses libbson's
    legacy JSON format.
    """
    ...

def dumps(bson: AnyStr) -> str:
    """Decode the BSON bytes object `bson` and return the resulting MongoDB
    Extended JSON 2.0 relaxed mode document as a string.

    Accepts a keyword argument `mode` which can be one of `bsonjs.RELAXED`
    `bsonjs.CANONICAL`, or `bsonjs.LEGACY`. Where `RELAXED` and `CANONICAL`
    correspond to the MongoDB Extended JSON 2.0 modes and `LEGACY` uses libbson's
    legacy JSON format.
    """
    ...

def load(fp: SupportsRead) -> bytes:
    """
    Encode the MongoDB Extended JSON 2.0 document in `fp` (a `.read()`-supporting
    file-or-buffer-like object) and return the resulting BSON bytes object.

    This function wraps `bson_init_from_json` from libbson.
    """
    ...

def loads(json: AnyStr) -> bytes:
    """
    Encode the MongoDB Extended JSON 2.0 document in `json` (a string or bytes-like
    object) and return the resulting BSON bytes object.

    This function wraps `bson_init_from_json` from libbson.
    """
    ...

import execjs
from os import path

#------------------------------------------------------------------------------

def trim(func):
    def trimmed_func(*args, **kwargs):
        return func(*args, **kwargs).strip()
    return trimmed_func

#------------------------------------------------------------------------------

curr_dir = path.dirname(path.realpath(__file__))

with open(path.join(curr_dir, 'js_resources/mathlib.js')) as f:
    MATHLIB_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/cross.js')) as f:
    CROSS_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/scramble.js')) as f:
    SCRAMBLE_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/megascramble.js')) as f:
    MEGA_SCRAMBLE_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/utilscramble.js')) as f:
    UTIL_SCRAMBLE_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/scramble_333_edit.js')) as f:
    SCRAMBLE_333_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/scramble_444.js')) as f:
    SCRAMBLE_444_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/scramble_sq1.js')) as f:
    SCRAMBLE_SQ1_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/2x2x2.js')) as f:
    SCRAMBLE_222_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/2x2x3.js')) as f:
    SCRAMBLE_223_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/1x3x3.js')) as f:
    SCRAMBLE_133_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/pyraminx.js')) as f:
    PYRAMINX_SRC = f.read()

with open(path.join(curr_dir, 'js_resources/skewb.js')) as f:
    SKEWB_SRC = f.read()

#------------------------------------------------------------------------------

_UTIL_SCRAMBLER  = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + UTIL_SCRAMBLE_SRC)
_PYRA_SCRAMBLER  = execjs.compile(MATHLIB_SRC + PYRAMINX_SRC)
_SQ1_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + SCRAMBLE_SQ1_SRC)
_133_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_133_SRC)
_222_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_222_SRC)
_223_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_223_SRC)
_333_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + CROSS_SRC + SCRAMBLE_333_SRC)
_444_SCRAMBLER   = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + SCRAMBLE_333_SRC + SCRAMBLE_444_SRC)
_MEGA_SCRAMBLER  = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + SCRAMBLE_333_SRC + MEGA_SCRAMBLE_SRC)
_SKEWB_SCRAMBLER = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + SKEWB_SRC)

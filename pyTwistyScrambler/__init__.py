from os import path

curr_dir = path.dirname(path.realpath(__file__))

def trim(func):
    def trimmed_func(*args, **kwargs):
        return func(*args, **kwargs).strip()
    return trimmed_func

#------------------------------------------------------------------------------

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

with open(path.join(curr_dir, 'js_resources/pyraminx.js')) as f:
    PYRAMINX_SRC = f.read()
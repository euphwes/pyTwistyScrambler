from . import UTIL_SCRAMBLE_SRC, SCRAMBLE_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + UTIL_SCRAMBLE_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=70):
    """ Gets a WCA scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return _scrambler.call("util_scramble.getMegaminxWCAScramble", n).replace('\n','').replace('  ',' ').replace('  ',' ')

@trim
def get_Carrot_scramble(n=70):
    """ Gets a Carrot-notation scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return _scrambler.call("util_scramble.getMegaminxCarrotScramble", n).replace('\n','').replace('  ',' ').replace('  ',' ')

@trim
def get_old_style_scramble(n=70):
    """ Gets an old-style scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return _scrambler.call("util_scramble.getMegaminxOldStyleScramble", n)
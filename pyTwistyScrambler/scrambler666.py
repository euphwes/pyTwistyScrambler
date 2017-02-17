from . import SCRAMBLE_SRC, MEGA_SCRAMBLE_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_SRC + MEGA_SCRAMBLE_SRC)

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble(n=80):
    """ Gets a WCA scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return _scrambler.call("megaScrambler.get666WCAScramble", n)

@trim
def get_SiGN_scramble(n=80):
    """ Gets a SiGN-notation scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return _scrambler.call("megaScrambler.get666SiGNScramble", n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 8. """
    return _scrambler.call("megaScrambler.get666edgesScramble", n)
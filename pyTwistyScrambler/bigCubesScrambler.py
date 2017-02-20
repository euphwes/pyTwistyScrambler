from . import _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_8x8x8_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for an 8x8x8 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get888scramble", n)

@trim
def get_9x9x9_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for a 9x9x9 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get999scramble", n)

@trim
def get_10x10x10_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for a 10x10x10 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get101010scramble", n)

@trim
def get_11x11x11_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for an 11x11x11 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get111111scramble", n)
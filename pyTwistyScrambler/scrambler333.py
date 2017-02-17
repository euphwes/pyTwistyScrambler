from . import _333_SCRAMBLER, _MEGA_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getRandomScramble")

@trim
def get_3BLD_scramble():
    """ Gets a BLD scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.get3BLDScramble")

@trim
def get_random_scramble():
    """ Gets a random scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getRandomScramble")

@trim
def get_edges_scramble():
    """ Gets an edges-only scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getEdgeScramble")

@trim
def get_corners_scramble():
    """ Gets a corners-only scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getCornerScramble")

@trim
def get_LL_scramble():
    """ Gets a last layer scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getLLScramble")

@trim
def get_LSLL_scramble():
    """ Gets a last slot last layer scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getLSLLScramble")

@trim
def get_ZBLL_scramble():
    """ Gets a Zborowski-Bruchem last layer scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getZBLLScramble")

@trim
def get_ZZLL_scramble():
    """ Gets a Zbigniew Zborowski last layer scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getZZLLScramble")

@trim
def get_ZBLS_scramble():
    """ Gets a ZBLS scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getZBLSScramble")

@trim
def get_F2L_scramble():
    """ Gets an F2L (first two layers) scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getF2LScramble")

@trim
def get_LSE_scramble():
    """ Gets an LSE (last six edges) scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getLSEScramble")

@trim 
def get_EOLine_scramble():
    """ Gets an EO line scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getEOLineScramble")

@trim
def get_CMLL_scramble():
    """ Gets a CMLL scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getCMLLScramble")

@trim
def get_CLL_scramble():
    """ Gets a CLL scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getCLLScramble")

@trim
def get_ELL_scramble():
    """ Gets an ELL scramble of a 3x3x3 cube. """
    return _333_SCRAMBLER.call("scramble_333.getELLScramble")

@trim
def get_easy_cross_scramble(n):
    """ Gets an 'easy cross' scramble, where the cross can be solved in `n` moves."""
    return _333_SCRAMBLER.call("scramble_333.getEasyCrossScramble", n)

@trim
def get_2genRU_scramble():
    """ Gets a 2-gen scramble with only RU moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_2genRU_scramble")

@trim
def get_2genLU_scramble():
    """ Gets a 2-gen scramble with only LU moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_2genLU_scramble")

@trim
def get_2genMU_scramble():
    """ Gets a 2-gen scramble with only MU moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_2genMU_scramble")

@trim
def get_3genFRU_scramble():
    """ Gets a 3-gen scramble with only FRU moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_3genFRU_scramble")

@trim
def get_3genRUL_scramble():
    """ Gets a 3-gen scramble with only RUL moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_3genRUL_scramble")

@trim
def get_3genRrU_scramble():
    """ Gets a 3-gen scramble with only RrU moves for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_3genRrU_scramble")

@trim
def get_half_turns_scramble():
    """ Gets a half turns-only scramble for a 3x3x3 cube. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get333_halfTurns_scramble")
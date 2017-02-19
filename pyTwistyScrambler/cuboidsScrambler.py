from . import _MEGA_SCRAMBLER, _223_SCRAMBLER, _133_SCRAMBLER, trim

#------------------------------------------------------------------------------

@trim
def get_1x1x2_scramble():
    """ Gets a random scramble for a 1x1x2 cuboid (lul). """
    return _MEGA_SCRAMBLER.call("megaScrambler.get112scramble")

@trim
def get_1x3x3_scramble():
    """ Gets a random scramble for a 1x3x3 cuboid. """
    return _133_SCRAMBLER.call("scrambler133.get133scramble")

@trim
def get_floppy_cube_scramble():
    """ Gets a random scramble for a 1x3x3 cuboid. Alias of 1x3x3. """
    return get_1x3x3_scramble()

@trim
def get_super_floppy_cube_scramble():
    """ Gets a random scramble for a 1x3x3 super floppy cuboid. """
    return _MEGA_SCRAMBLER.call("megaScrambler.getSuperFloppyScramble")

@trim
def get_2x2x3_scramble():
    """ Gets a random scramble for a 2x2x3 cuboid. """
    return _223_SCRAMBLER.call("scrambler223.get223scramble")

@trim
def get_3x3x2_scramble():
    """ Gets a random scramble for a 3x3x2 cuboid. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get332scramble")

@trim
def get_3x3x4_scramble():
    """ Gets a random scramble for a 3x3x4 cuboid. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get334scramble")

@trim
def get_3x3x5_scramble(n=25):
    """ Gets a random scramble for a 3x3x5 cuboid, where `n` is the length of the non-3x3x3 portion of the scramble. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get335scramble", n)

@trim
def get_3x3x6_scramble():
    """ Gets a random scramble for a 3x3x6 cuboid. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get336scramble")

@trim
def get_3x3x7_scramble(n=40):
    """ Gets a random scramble for a 3x3x7 cuboid, where `n` is the length of the non-3x3x3 portion of the scramble. """
    return _MEGA_SCRAMBLER.call("megaScrambler.get337scramble", n)
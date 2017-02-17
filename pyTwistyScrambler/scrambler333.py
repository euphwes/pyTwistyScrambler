from . import SCRAMBLE_333_SRC, MATHLIB_SRC, CROSS_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + CROSS_SRC + SCRAMBLE_333_SRC)

#------------------------------------------------------------------------------

@trim
def get_random_scramble():
	return _scrambler.call("scramble_333.getRandomScramble")
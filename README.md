# pyTwistyScrambler
A Python module for providing scrambles of various twisty puzzles, including the Rubik's cube, 4x4x4 cube, and others.
Thanks to [csTimer](https://github.com/cs0x7f/cstimer) for providing the JavaScript scrambling source code around which this project is a wrapper.

## What scrambles can be generated?
### 3x3x3 (Rubik's cube)
- Random scramble
- Edges-only and corners-only
- LL (last layer)
- F2L (first two layers)
- Specialized (LSLL, ZBLL, ZZLL, F2L, LSE, CMLL, CLL, ELL)

## Example usage

```python
from pyTwistyScrambler import scrambler333

scrambler333.get_random_scramble()
# D2 L F2 L2 F2 U2 L D2 F2 L' B' U2 F2 D' F D2 B' U2 R U'

scrambler333.get_F2L_scramble()
# R' F2 L2 B R2 U2 B U2 F2 R2 F' U2 R' U R' U B L' D2

scrambler333.get_ZBLL_scramble()
# R2 U R2 U' R' U' F R2 U R2 U' F' R'
```

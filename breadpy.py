#    BreadPy - Generates ASCII breadboard / veroboard of given rows and columns
#    Python 3.5.4
#    Author: Cryptostrike https://github.com/Cryptostrike

#    This file is part of BreadPy.
#
#    BreadPy is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    BreadPy is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

# python BreadPy.py 5 10
# Example board output for a 5 row 10 column board:
#  __________
# |          |
# |oooooooooo|
# |oooooooooo|
# |oooooooooo|
# |oooooooooo|
# |oooooooooo|
# |__________|

import Board, sys

try:
    row = int(sys.argv[1])
    column = int(sys.argv[2])

    board1 = Board.Board(row, column)
    board1.construct()

except (IndexError, ValueError):
    print("Usage: breadpy.py <rows> <columns>")
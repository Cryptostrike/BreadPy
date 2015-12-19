#    BreadPy - Generates ASCII breadboard / veroboard of given rows and columns
#    Author: Cryptostrike https://github.com/Cryptostrike
#    Python 3.5.4

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

#    This class can be used either with the command line script breadpy.py or used alone, it has no dependencies
#    Example board output for a 5 row 10 column board
#    __________
#   |          |
#   |oooooooooo|
#   |oooooooooo|
#   |oooooooooo|
#   |oooooooooo|
#   |oooooooooo|
#   |__________|


class Board:
    # Rows and columns refers to the actual holes in the board, not the overall size
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def increment(self, char, columns):
        for num in range(0, columns):
            print(char, end="")

    # Prints the first row of the board
    def firstrow(self):
        # ----- at the top of the board
        print(" ", end="")
        self.increment("_", self.columns)
        print()

        # Blank line to make it proportional to the last line
        print("|", end="")
        self.increment(" ", self.columns)
        print("|", end="")
        print()

    # Prints the last row of the board
    def lastrow(self):
        print("|", end="")
        self.increment("_", self.columns)
        print("|")

    # Prints the body of the board, this is the bit in between the top and bottom
    def body(self):
        for num in range(0, self.rows):
            print("|", end="")
            self.increment("o", self.columns)
            print("|")

    # Print the dimensions of the board
    def dimensions(self):
        print("Width: %d\nHeight: %d" % (self.columns, self.rows))

    # Construct the board using all the above functions
    def construct(self):
        self.firstrow()
        self.body()
        self.lastrow()
        self.dimensions()
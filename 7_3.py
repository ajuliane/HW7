class Cell:
    def __init__(self, number):
        self.cellnumber = number

    def __add__(self, cellsecond):
        result= Cell(self.cellnumber+cellsecond.cellnumber)
        print(result.cellnumber)


    def __sub__(self, cellsecond):
        result = Cell(self.cellnumber - cellsecond.cellnumber)
        if result.cellnumber<0:
            print('It is impossible to subtract')
        else:
            print(result.cellnumber)

    def __mul__(self, cellsecond):
                result = Cell(self.cellnumber * cellsecond.cellnumber)
                print(result.cellnumber)
    def __truediv__(self, cellsecond):
        try:
                result = Cell(self.cellnumber / cellsecond.cellnumber)
                print(result.cellnumber)
        except ZeroDivisionError:
            print('Division by zero is restricted!')
    def makeorder(self, rows):
        try:

                for i in range(self.cellnumber//rows):
                    for i in range(rows):
                        print('*')
                    print('\n')


                for y in range(self.cellnumber % rows):
                    print('*')

        except ZeroDivisionError:
            print('Division by zero is restricted!')




cell1=Cell(12)

cell2=Cell(6)

cell1 +  cell2
cell1 - cell2
cell1 * cell2
cell1 / cell2
cell1.makeorder(5)
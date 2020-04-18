class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ''.join([''.join([str(i) for i in line]) for line in self.matrix])



my_matrix = Matrix([[1, 1, 1],
                    [2, 2, 2],
                    [3, 3, 3]])
print(my_matrix)

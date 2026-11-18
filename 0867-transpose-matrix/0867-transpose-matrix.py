import numpy as np
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        if len(matrix) == 0:
            return -1

        row = len(matrix)
        columns = len(matrix[0])

        result =[]

        for j in range(columns):
            new = []
            for i in range(row):
                new.append(matrix[i][j])
            result.append(new)

        return result
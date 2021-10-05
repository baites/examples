class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Get the size of the matrix
        # assuming it is square
        size = len(matrix)

        # Locate the points from the diagonal
        # up to the center of the matrix.
        for n in range(size//2):
            # Index running over the matrix perimeter
            for m in range(n, size-n-1):

                temp1 = matrix[m][size-n-1]
                matrix[m][size-n-1] = matrix[n][m]

                temp2 = matrix[size-n-1][size-m-1]
                matrix[size-n-1][size-m-1] = temp1

                temp1 = matrix[size-m-1][n]
                matrix[size-m-1][n] = temp2

                matrix[n][m] = temp1
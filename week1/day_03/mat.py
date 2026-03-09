class Matrix:

    def __init__(self, data):

        if not data or not isinstance(data, list):
            raise TypeError("Matrix must be a non-empty list")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def size(self):
        return (self.rows, self.cols)

    def transpose(self):

        res = []

        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            res.append(row)

        return Matrix(res)

    def multiply(self, other):

        if self.cols != other.rows:
            raise ValueError("Matrix dimensions not compatible")

        res = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):

                    res[i][j] += self.data[i][k] * other.data[k][j]

        return Matrix(res)

    def det2x2(self):

        if self.rows != 2 or self.cols != 2:
            raise ValueError("Determinant defined only for 2x2 matrix")

        a = self.data[0][0]
        b = self.data[0][1]
        c = self.data[1][0]
        d = self.data[1][1]

        return a*d - b*c

    def det3x3(self):

        if self.rows != 3 or self.cols != 3:
            raise ValueError("Determinant defined only for 3x3 matrix")

        a,b,c = self.data[0]
        d,e,f = self.data[1]
        g,h,i = self.data[2]

        return (
            a*(e*i - f*h)
            - b*(d*i - f*g)
            + c*(d*h - e*g)
        )

    def inverse2x2(self):

        det = self.det2x2()

        if det == 0:
            raise ValueError("Matrix is singular")

        a = self.data[0][0]
        b = self.data[0][1]
        c = self.data[1][0]
        d = self.data[1][1]

        res = [
            [d/det, -b/det],
            [-c/det, a/det]
        ]

        return Matrix(res)

    def is_singular(self):

        if self.rows == 2:
            return self.det2x2() == 0

        if self.rows == 3:
            return self.det3x3() == 0

        raise ValueError("Singularity check only for 2x2 or 3x3")

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)
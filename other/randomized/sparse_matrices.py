class SparseMatrix:
    """Sparse matrix representation using dictionary of (row, col) -> value."""

    def __init__(
        self, rows: int, cols: int, elements: dict[tuple[int, int], float] | None = None
    ):
        self.rows = rows
        self.cols = cols
        self.elements: dict[tuple[int, int], float] = elements or {}

    @classmethod
    def from_dense(cls, matrix: list[list[float]]) -> "SparseMatrix":
        """Create sparse matrix from dense 2D list."""
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        elements = {}
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0:
                    elements[(i, j)] = matrix[i][j]
        return cls(rows, cols, elements)

    def to_dense(self) -> list[list[float]]:
        """Convert sparse matrix to dense 2D list."""
        result = [[0.0] * self.cols for _ in range(self.rows)]
        for (i, j), val in self.elements.items():
            result[i][j] = val
        return result

    def get(self, i: int, j: int) -> float:
        """Get element at position (i, j)."""
        return self.elements.get((i, j), 0.0)

    def set(self, i: int, j: int, value: float) -> None:
        """Set element at position (i, j)."""
        if value == 0:
            self.elements.pop((i, j), None)
        else:
            self.elements[(i, j)] = value

    def add(self, other: "SparseMatrix") -> "SparseMatrix":
        """Add two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        result = dict(self.elements)
        for (i, j), val in other.elements.items():
            result[(i, j)] = result.get((i, j), 0) + val
        return SparseMatrix(
            self.rows, self.cols, {k: v for k, v in result.items() if v != 0}
        )

    def transpose(self) -> "SparseMatrix":
        """Transpose the sparse matrix."""
        elements = {(j, i): v for (i, j), v in self.elements.items()}
        return SparseMatrix(self.cols, self.rows, elements)

    def multiply(self, other: "SparseMatrix") -> "SparseMatrix":
        """Multiply two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for (i, k), v1 in self.elements.items():
            for (k2, j), v2 in other.elements.items():
                if k == k2:
                    current = result.elements.get((i, j), 0)
                    result.elements[(i, j)] = current + v1 * v2
        result.elements = {k: v for k, v in result.elements.items() if v != 0}
        return result

    def density(self) -> float:
        """Return the density (non-zero ratio) of the matrix."""
        return len(self.elements) / (self.rows * self.cols)


if __name__ == "__main__":
    dense = [
        [0, 0, 3],
        [0, 5, 0],
        [7, 0, 0],
    ]
    sparse = SparseMatrix.from_dense(dense)
    print(f"Density: {sparse.density():.2%}")
    print(f"Transpose:\n{[row for row in sparse.transpose().to_dense()]}")

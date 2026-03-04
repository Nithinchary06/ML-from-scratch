# Day 02 – Matrix Operations (From Scratch)

## Objective

Implement core matrix operations from scratch to understand the mathematical foundations used in Machine Learning algorithms.

This implementation avoids external libraries like NumPy to build a deeper understanding of how matrix operations work internally.

---

## Topics Covered

- Matrix representation
- Matrix shape
- Matrix transpose
- Matrix multiplication

---

## Matrix Representation

A matrix is a 2D collection of numbers arranged in rows and columns.

Example:

A =

```
1 2 3
4 5 6
```

Shape of this matrix:

```
2 × 3
(rows × columns)
```

---

## Matrix Transpose

The transpose of a matrix swaps rows and columns.

Example:

A =

```
1 2 3
4 5 6
```

Transpose of A:

```
1 4
2 5
3 6
```

Mathematically:

```
Aᵀ[i][j] = A[j][i]
```

---

## Matrix Multiplication

Matrix multiplication is defined only when:

```
columns of A = rows of B
```

Example:

A = (2 × 3)
B = (3 × 2)

Result:

```
C = A × B → (2 × 2)
```

Formula:

```
C(i,j) = Σ A(i,k) × B(k,j)
```

This operation is essentially a **dot product between a row of A and a column of B**.

---

## Time Complexity

Matrix multiplication complexity:

```
O(n³)
```

Because three nested loops are required:

- rows
- columns
- dot product computation

---

## Why This Matters in Machine Learning

Matrix operations are fundamental to ML and Deep Learning.

They are used in:

- Linear Regression
- Neural Networks
- Principal Component Analysis (PCA)
- Image processing
- Transformer models

Neural networks compute weighted sums using matrix multiplication.

---

## Key Learning

Matrix multiplication is essentially repeated **dot products between vectors**.
Understanding this concept helps in understanding how neural networks perform computations.

---

## Next Step

Day 03 will cover:

- Determinant
- Matrix inverse
- Singular vs Non-singular matrices
- Connection to Linear Regression Normal Equation

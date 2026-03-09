# Day 03 – Determinant, Matrix Inverse, and Singular Matrices

## Objective

Implement determinant calculation and matrix inversion from scratch to understand the mathematical foundations used in many Machine Learning algorithms.

This implementation avoids external libraries like NumPy in order to build a deeper understanding of linear algebra operations.

---

## Topics Covered

- Determinant of a 2×2 matrix
- Determinant of a 3×3 matrix
- Matrix inverse (2×2)
- Singular vs Non-Singular matrices

---

## Determinant (2×2)

For a matrix:

A =

```
a  b
c  d
```

The determinant is:

```
det(A) = ad − bc
```

The determinant tells us whether a matrix can be inverted.

---

## Determinant (3×3)

For a matrix:

```
a  b  c
d  e  f
g  h  i
```

The determinant is calculated as:

```
a(ei − fh) − b(di − fg) + c(dh − eg)
```

This expansion is known as **cofactor expansion**.

---

## Matrix Inverse (2×2)

For a matrix:

```
a  b
c  d
```

The inverse is:

```
1/(ad − bc) *
|  d  -b |
| -c   a |
```

Important condition:

```
det(A) ≠ 0
```

If the determinant is zero, the matrix **does not have an inverse**.

---

## Singular vs Non-Singular Matrix

| Type                | Condition  |
| ------------------- | ---------- |
| Singular Matrix     | det(A) = 0 |
| Non-Singular Matrix | det(A) ≠ 0 |

Singular matrices cannot be inverted.

---

## Why This Matters in Machine Learning

Determinants and matrix inverses appear in many ML algorithms, including:

- Linear Regression (Normal Equation)
- Multivariate Gaussian distributions
- Covariance matrices
- Principal Component Analysis (PCA)

Example from Linear Regression:

```
θ = (XᵀX)⁻¹ Xᵀy
```

The inverse operation used here is the same mathematical concept implemented in this project.

---

## Key Learning

Understanding determinants and matrix inverses helps explain:

- Why some matrices cannot be inverted
- How linear systems are solved
- How machine learning models compute parameters mathematically

---

## Next Step

Day 04 will introduce **Probability and Statistics concepts used in Machine Learning**, including:

- Mean
- Variance
- Standard deviation
- Covariance
- Correlation

# Day 01 – Vectors, Dot Product & Cosine Similarity

## Objective

Understand vector operations without using NumPy.

## Implemented

- Custom Vector class
- Dot product (O(n))
- Magnitude calculation
- Cosine similarity

## Mathematical Intuition

Dot Product:
a · b = Σ (aᵢ × bᵢ)

Cosine Similarity:
cosθ = (a · b) / (|a||b|)

If:

- cosθ ≈ 1 → similar direction
- cosθ ≈ 0 → orthogonal
- cosθ ≈ -1 → opposite direction

## Why This Matters in ML

- Neural networks use dot product for weighted sums
- Recommendation systems use cosine similarity
- PCA relies on vector projections

## Time Complexity

Dot Product: O(n)
Magnitude: O(n)
Cosine Similarity: O(n)

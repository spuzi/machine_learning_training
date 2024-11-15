from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Sum of 2 vectors

    Args:
        v (Vector): first vector
        w (Vector): second vector

    Returns:
        Vector: sum of the 2 vectors
    """
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

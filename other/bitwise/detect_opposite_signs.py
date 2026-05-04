def detect_opposite_signs(a: int, b: int) -> bool:
    """Detect if two integers have opposite signs using bitwise operator."""
    return (a ^ b) < 0


if __name__ == "__main__":
    print(detect_opposite_signs(5, -3))
    print(detect_opposite_signs(5, 3))
    print(detect_opposite_signs(-5, -3))

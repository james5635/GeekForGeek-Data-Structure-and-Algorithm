"""Approach: Using Mathematical Formula - O(1) in Time and O(1) in Space"""


def get_min(x: float, y: float) -> float:
    """
    Utility function to return the minimum of two double values.
    
    >>> get_min(5.0, 3.0)
    3.0
    >>> get_min(2.5, 2.5)
    2.5
    """
    return x if x < y else y


def get_angle(s: str) -> float:
    """
    Calculate the minimum angle between hour and minute hands of an analog clock.
    
    Given a string s represents time in 24-hour format ("HH:MM"), determine the
    minimum angle between the hour and minute hands of an analog clock.
    
    The minute hand moves 6° per minute, while the hour hand moves 0.5° per minute.
    Thus, the hour hand's angle is calculated as hrAngle = 30 × H + 0.5 × M, and
    the minute hand's angle as minAngle = 6 × M. The difference between the two
    angles is diff = |hrAngle - minAngle|.
    
    Since the clock follows a 12-hour format, any 24-hour input should be converted
    using H = H % 12. After finding the absolute difference between the two angles,
    the smaller angle is determined using min(diff, 360 - diff).
    
    Step-by-step approach:
    1. Extract hours and minutes from "HH:MM" format
    2. Convert 24-hour time to 12-hour format (H = H % 12)
    3. Calculate hour hand angle: 0.5 × (H × 60 + M) degrees
    4. Calculate minute hand angle: 6 × M degrees
    5. Find absolute difference between the two angles
    6. Return the smaller angle: min(angle, 360 - angle)
    
    >>> abs(get_angle("06:00") - 180.0) < 0.001
    True
    >>> abs(get_angle("03:15") - 7.5) < 0.001
    True
    >>> abs(get_angle("00:00") - 0.0) < 0.001
    True
    >>> abs(get_angle("12:00") - 0.0) < 0.001
    True
    >>> abs(get_angle("12:30") - 165.0) < 0.001
    True
    """
    # Extract hours and minutes from "HH:MM"
    h = int(s[:2])
    m = int(s[3:])

    # Convert 24-hour time to 12-hour format
    h = h % 12

    # Hour hand moves 0.5 degrees per minute (30 degrees per hour)
    hr_angle = 0.5 * (h * 60 + m)

    # Minute hand moves 6 degrees per minute
    min_angle = 6 * m

    # Find the absolute difference between the two angles
    angle = abs(hr_angle - min_angle)

    # Return the smaller angle of the two possible angles
    return get_min(360.0 - angle, angle)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

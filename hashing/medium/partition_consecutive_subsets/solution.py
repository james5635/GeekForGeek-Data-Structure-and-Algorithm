"""
Partition Array into Consecutive Subsets

Problem: Given an array of integers, check if it can be partitioned into
consecutive subsequences of length >= 3. A consecutive subsequence is a sequence
where each element is one more than the previous element.

Approach: Use a hash map to count frequencies, then greedily form subsequences.
For each number, either append it to an existing subsequence ending at num-1,
or start a new subsequence with num, num+1, num+2.

Time Complexity: O(n log n) - due to sorting, or O(n) with heap/tree map
Space Complexity: O(n) - hash maps for frequency and subsequences
"""

from collections import defaultdict


def can_partition_consecutive_subsets(nums):
    """
    Check if array can be partitioned into consecutive subsequences of length >= 3.

    Args:
        nums: List of integers

    Returns:
        True if partition is possible, False otherwise
    """
    if not nums:
        return True

    freq = defaultdict(int)
    need = defaultdict(int)

    for num in nums:
        freq[num] += 1

    for num in sorted(nums):
        if freq[num] == 0:
            continue

        if need[num] > 0:
            # Append to existing subsequence ending at num-1
            need[num] -= 1
            need[num + 1] += 1
        elif freq[num + 1] > 0 and freq[num + 2] > 0:
            # Start new subsequence: num, num+1, num+2
            freq[num + 1] -= 1
            freq[num + 2] -= 1
            need[num + 3] += 1
        else:
            return False

        freq[num] -= 1

    return True


def partition_into_subsets(nums):
    """
    Partition array into consecutive subsequences and return the subsequences.

    Args:
        nums: List of integers

    Returns:
        List of subsequences if possible, empty list otherwise
    """
    if not nums:
        return []

    freq = defaultdict(int)
    subsequences = defaultdict(list)

    for num in nums:
        freq[num] += 1

    for num in sorted(nums):
        if freq[num] == 0:
            continue

        if subsequences[num - 1]:
            # Append to existing subsequence
            subseq = subsequences[num - 1].pop()
            subseq.append(num)
            subsequences[num].append(subseq)
        else:
            # Start new subsequence
            subsequences[num].append([num])

        freq[num] -= 1

    result = []
    for subs in subsequences.values():
        result.extend(subs)

    # Check if all subsequences have length >= 3
    if all(len(s) >= 3 for s in result):
        return result
    return []


if __name__ == "__main__":
    # Test Case 1: Valid partition
    nums1 = [1, 2, 3, 3, 4, 5]
    print(f"Array: {nums1}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums1)}")
    print(f"Subsets: {partition_into_subsets(nums1)}")
    print()

    # Test Case 2: Valid partition - multiple groups
    nums2 = [1, 2, 3, 4, 5]
    print(f"Array: {nums2}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums2)}")
    print(f"Subsets: {partition_into_subsets(nums2)}")
    print()

    # Test Case 3: Cannot partition
    nums3 = [1, 2, 3, 4, 4, 5]
    print(f"Array: {nums3}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums3)}")
    print(f"Subsets: {partition_into_subsets(nums3)}")
    print()

    # Test Case 4: Single element
    nums4 = [1]
    print(f"Array: {nums4}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums4)}")
    print()

    # Test Case 5: Two elements only
    nums5 = [1, 2]
    print(f"Array: {nums5}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums5)}")
    print()

    # Test Case 6: Empty array
    nums6 = []
    print(f"Array: {nums6}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums6)}")
    print()

    # Test Case 7: Duplicates that can form valid groups
    nums7 = [1, 2, 3, 3, 4, 4, 5, 6]
    print(f"Array: {nums7}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums7)}")
    print(f"Subsets: {partition_into_subsets(nums7)}")
    print()

    # Test Case 8: Non-consecutive elements
    nums8 = [1, 2, 4, 5, 6]
    print(f"Array: {nums8}")
    print(f"Can partition: {can_partition_consecutive_subsets(nums8)}")
    print(f"Subsets: {partition_into_subsets(nums8)}")

"""
Channel Assignment Problem.

Assign M transmitters to N receivers to maximize packets sent in one time slot. Each transmitter sends one packet, each receiver receives one packet per slot.

Based on: https://www.geeksforgeeks.org/channel-assignment-problem/
"""

from typing import List


class ChannelAssignment:
    """Solves channel assignment using bipartite matching."""

    def __init__(self, table: List[List[int]]):
        """
        Args:
            table: M x N matrix where table[i][j] is packets from transmitter i to receiver j.
        """
        self.table = table
        self.num_senders = len(table)
        self.num_receivers = len(table[0]) if self.num_senders > 0 else 0

    def _bpm(self, sender: int, match_r: List[int], seen: List[bool]) -> bool:
        """DFS to find receiver for sender."""
        for receiver in range(self.num_receivers):
            if self.table[sender][receiver] > 0 and not seen[receiver]:
                seen[receiver] = True
                if match_r[receiver] == -1 or self._bpm(
                    match_r[receiver], match_r, seen
                ):
                    match_r[receiver] = sender
                    return True
        return False

    def max_packets(self) -> int:
        """Compute maximum packets sent."""
        match_r = [-1] * self.num_receivers
        result = 0
        for sender in range(self.num_senders):
            seen = [False] * self.num_receivers
            if self._bpm(sender, match_r, seen):
                result += 1
        return result


if __name__ == "__main__":
    table = [[0, 2, 0], [3, 0, 1], [2, 4, 0]]
    assigner = ChannelAssignment(table)
    print(f"Maximum packets sent: {assigner.max_packets()}")  # Output: 3

"""
Maximum Bipartite Matching.

A matching in a bipartite graph is a set of edges with no shared endpoints. Maximum matching is the largest such set. Uses DFS-based approach similar to Ford-Fulkerson.

Based on: https://www.geeksforgeeks.org/maximum-bipartite-matching/
"""

from typing import List


class BipartiteMatching:
    """Solves maximum bipartite matching problems."""

    def __init__(self, bipartite_graph: List[List[int]]):
        """
        Args:
            bipartite_graph: M x N matrix where bipartite_graph[i][j] = 1 if applicant i is interested in job j.
        """
        self.graph = bipartite_graph
        self.num_applicants = len(bipartite_graph)
        self.num_jobs = len(bipartite_graph[0]) if self.num_applicants > 0 else 0

    def _bpm(self, applicant: int, match_r: List[int], seen: List[bool]) -> bool:
        """DFS to find matching for applicant."""
        for job in range(self.num_jobs):
            if self.graph[applicant][job] == 1 and not seen[job]:
                seen[job] = True
                if match_r[job] == -1 or self._bpm(match_r[job], match_r, seen):
                    match_r[job] = applicant
                    return True
        return False

    def max_matching(self) -> int:
        """Compute maximum number of matches."""
        match_r = [-1] * self.num_jobs
        result = 0
        for applicant in range(self.num_applicants):
            seen = [False] * self.num_jobs
            if self._bpm(applicant, match_r, seen):
                result += 1
        return result


if __name__ == "__main__":
    bp_graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ]
    matcher = BipartiteMatching(bp_graph)
    print(f"Maximum applicants placed: {matcher.max_matching()}")  # Output: 5

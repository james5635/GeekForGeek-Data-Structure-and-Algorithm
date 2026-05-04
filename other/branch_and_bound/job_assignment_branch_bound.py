"""Job Assignment Problem using Branch and Bound."""

from __future__ import annotations


class JobAssignment:
    """Solve Job Assignment using Branch and Bound."""

    def __init__(self, cost_matrix: list[list[int]]) -> None:
        self.cost_matrix = cost_matrix
        self.n = len(cost_matrix)
        self.best_cost = float("inf")
        self.best_assignment: list[int] = []

    def _lower_bound(
        self, worker: int, assignment: list[int], assigned_jobs: set[int]
    ) -> int:
        bound = 0
        for w in range(worker, self.n):
            min_cost = float("inf")
            for j in range(self.n):
                if j not in assigned_jobs and self.cost_matrix[w][j] < min_cost:
                    min_cost = self.cost_matrix[w][j]
            bound += min_cost
        return bound

    def _solve(
        self,
        worker: int,
        current_cost: int,
        assignment: list[int],
        assigned_jobs: set[int],
    ) -> None:
        if worker == self.n:
            if current_cost < self.best_cost:
                self.best_cost = current_cost
                self.best_assignment = assignment[:]
            return

        bound = current_cost + self._lower_bound(worker, assignment, assigned_jobs)
        if bound >= self.best_cost:
            return

        for job in range(self.n):
            if job not in assigned_jobs:
                assignment.append(job)
                assigned_jobs.add(job)
                self._solve(
                    worker + 1,
                    current_cost + self.cost_matrix[worker][job],
                    assignment,
                    assigned_jobs,
                )
                assigned_jobs.remove(job)
                assignment.pop()

    def solve(self) -> tuple[list[int], int]:
        """Find optimal job assignment.

        Returns:
            Tuple of (assignment list, total cost).
        """
        self.best_cost = float("inf")
        self.best_assignment = []
        self._solve(0, 0, [], set())
        return self.best_assignment, self.best_cost


def job_assignment_branch_bound(cost_matrix: list[list[int]]) -> tuple[list[int], int]:
    """Solve Job Assignment problem using Branch and Bound.

    Args:
        cost_matrix: NxN matrix where cost_matrix[i][j] is the cost of assigning job j to worker i.

    Returns:
        Tuple of (assignment, total_cost) where assignment[i] is the job assigned to worker i.
    """
    solver = JobAssignment(cost_matrix)
    return solver.solve()


if __name__ == "__main__":
    cost_matrix = [
        [3, 2, 4, 5],
        [5, 4, 2, 3],
        [4, 6, 3, 2],
        [2, 3, 5, 4],
    ]
    assignment, total_cost = job_assignment_branch_bound(cost_matrix)
    print(f"Optimal assignment: {assignment}")
    print(f"Total cost: {total_cost}")
    for i, job in enumerate(assignment):
        print(f"Worker {i} -> Job {job} (cost: {cost_matrix[i][job]})")

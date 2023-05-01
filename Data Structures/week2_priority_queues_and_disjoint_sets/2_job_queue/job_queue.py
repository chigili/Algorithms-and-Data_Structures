# python3
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

Job_Processing = namedtuple("Job_Processing", ["started_at", "worker"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs_fast(n_workers, jobs):

    assigned_workers = [None] * len(jobs)
    start_times = [None] * len(jobs)
    worker_heap = [Job_Processing(0, i) for i in range(n_workers)]
    heapq.heapify(worker_heap)

    for i in range(len(jobs)):
        time, worker = heapq.heappop(worker_heap)
        assigned_workers[i] = worker
        start_times[i] = time
        time += jobs[i]
        heapq.heappush(worker_heap, Job_Processing(time, worker))

    for i in range(len(jobs)):
        print(assigned_workers[i], start_times[i])


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # assigned_jobs = assign_jobs(n_workers, jobs)

    # for job in assigned_jobs:
    #     print(job.worker, job.started_at)
    assign_jobs_fast(n_workers, jobs)


if __name__ == "__main__":
    main()

![Demo](asset/pdc_mpiexec-ezgif.com-optimize.gif)

**Reflection Questions**

1. How did you distribute orders among worker processes?
Orders were distributed using MPI’s comm.send() from the master process. The master assigns each order to a worker using a simple round-robin approach:

The worker is chosen using:

worker = (i % num_workers) + 1

Here, i is the order index and num_workers is the number of worker processes. The modulo operation cycles through the workers, while +1 ensures the master (rank 0) is skipped.
This method evenly spreads orders across all workers (e.g., worker 1 → worker 2 → worker 3 → repeat), preventing overload on a single process and improving overall efficiency.

2. What happens if there are more orders than workers?
3. How did processing delays affect the order completion?
4. How did you implement shared memory, and where was it initialized?
5. What issues occurred when multiple workers wrote to shared memory simultaneously? When multiple workers attempted to write to the shared memory (the shared_orders list) at the same time without synchronization, a race condition occurred. This led to data inconsistency where some order results were overwritten or lost entirely. By using a Lock(), we created a critical section that ensured only one worker could append to the list at a time, guaranteeing consistent and complete results.
6. How did you ensure consistent results when using multiple processes?

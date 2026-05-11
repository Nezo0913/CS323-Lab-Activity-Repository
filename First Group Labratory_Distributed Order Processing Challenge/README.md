![Demo](asset/pdc_mpiexec-ezgif.com-optimize.gif)

**Reflection Questions**

1. How did you distribute orders among worker processes?
   Orders were distributed using MPI’s comm.send() from the master process. The master assigns each order to a worker using a simple round-robin approach
   
   The worker is chosen using:
   worker = (i % num_workers) + 1

   Here, i is the order index and num_workers is the number of worker processes. The modulo operation cycles through the workers, while +1 ensures the master (rank 0) is skipped.
   This method evenly spreads orders across all workers (e.g., worker 1 → worker 2 → worker 3 → repeat), preventing overload on a single process and improving overall efficiency.

3. What happens if there are more orders than workers?
   If there are more orders than workers, the system reuses workers in a cycle.
   This is handled automatically by the *modulo (%)* distribution, ensuring no order is left unassigned.
   
4. How did processing delays affect the order completion?
   Each worker uses time.sleep(random.uniform(1, 3)), this creates random processing delays. Because of this the following simulations are produced; orders do not finish in the same order they     were assigned, faster workers may complete later orders first, and lastly the completion order becomes unpredictable, this simulates real-world systems where tasks take different amounts of     time.

5. How did you implement shared memory, and where was it initialized?
   Shared memory was implemented using a Python list *shared_orders = []*, it was initialized inside the master process section (rank 0).

6. What issues occurred when multiple workers wrote to shared memory simultaneously? When multiple workers attempted to write to the shared memory (the shared_orders list) at the same time         without synchronization, a race condition occurred. This led to data inconsistency where some order results were overwritten or lost entirely. By using a Lock(), we created a critical           section that ensured only one worker could append to the list at a time, guaranteeing consistent and complete results.
   
7. How did you ensure consistent results when using multiple processes?
   Consistency was ensured by:
   - Using MPI message passing (comm.send / comm.recv) instead of direct shared access
   - Collecting all results at the master process only
   - Using a controlled loop to receive exactly the number of expected results
   - Applying a Lock() when writing to the shared list (for safety in structure, even though only master writes in the final version)

   This ensures:
   - No lost data
   - No race conditions
   - Deterministic final output in the master process


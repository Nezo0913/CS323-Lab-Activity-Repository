**Reflection Questions**

1. How did you distribute orders among worker processes?
2. What happens if there are more orders than workers?
3. How did processing delays affect the order completion?
4. How did you implement shared memory, and where was it initialized?
5. What issues occurred when multiple workers wrote to shared memory simultaneously? When multiple workers attempted to write to the shared memory (the shared_orders list) at the same time without synchronization, a race condition occurred. This led to data inconsistency where some order results were overwritten or lost entirely. By using a Lock(), we created a critical section that ensured only one worker could append to the list at a time, guaranteeing consistent and complete results.
6. How did you ensure consistent results when using multiple processes?

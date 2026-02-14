# Fist Lab Activity
Persistent-Python-Calculator-1.0

# Second Lab Activity
Exploring Multithreading and Multiprocessing in Python

# Thrid Lab Activty
Applying Task and Data Parallelism Using Concurrent.Futures

- Lab Activity Q&A

## 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.

    In this laboratory activity, we explored two types of parallel computing: task parallelism and data parallelism. Both aim to improve performance by running operations simultaneously, but they differ in how the workload is divided.

    Task parallelism focuses on executing different tasks at the same time using the same data. In the first program, this is demonstrated using ThreadPoolExecutor. For each employee, the payroll system splits the computation into four separate deduction tasks—SSS, PhilHealth, Pag-IBIG, and tax. These deductions are submitted as independent tasks and executed concurrently. The workload is divided by task type, meaning different operations are performed in parallel for one employee’s salary.

    In contrast, data parallelism focuses on dividing the data and applying the same operation to each part simultaneously. The second program demonstrates this using ProcessPoolExecutor. Instead of splitting deduction types, the program distributes employees across multiple CPU cores. Each process runs the same compute_employee_payroll() function but on different employees. Here, the workload is divided by data, with each core handling a subset of employees.

## 2. Explain how concurrent.futures managed execution,including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.

    In this lab, the concurrent.futures module is what handles the parallel execution in both programs. It gives us tools like ThreadPoolExecutor, ProcessPoolExecutor, submit(), map(), and Future objects to make concurrency easier to manage.

    For task parallelism, we used ThreadPoolExecutor. The submit() method assigns each deduction task to a thread, and it returns a Future object. A Future basically holds the result of a task that is still running. Then we use as_completed() to get the results as soon as each task finishes, so the program doesn’t wait for them one by one.

    For data parallelism, we used ProcessPoolExecutor to use multiple CPU cores. Instead of submit(), we used map(), which automatically applies the same function to all employees and distributes them across processes. It handles the scheduling and Futures internally and returns the results in order.

    The with statement is important because it automatically starts and properly shuts down the executor. It makes sure all threads or processes are cleaned up after execution, so we don’t have to manually call shutdown().

    Overall, concurrent.futures makes parallel programming more organized and easier to control.

## 3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?

    In the task parallelism code, we used ThreadPoolExecutor, which runs on threads. However, in CPython, threads are limited by the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time.

    Since heavy_computation() is CPU-bound, the threads compete for the GIL. Even though multiple threads were created, only one could run at a time. This means the program achieved concurrency, but not true parallelism across multiple CPU cores.

    Therefore, true parallelism did not occur with ThreadPoolExecutor in this case. Real parallel execution happens in the ProcessPoolExecutor version, where separate processes use separate GILs and can fully utilize multiple CPU cores.

## 4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.

    ProcessPoolExecutor enables true parallelism because it creates multiple independent processes instead of threads. Each process runs its own Python interpreter with a separate memory space and its own Global Interpreter Lock (GIL).

    Since the GIL only restricts threads within the same process, using multiple processes bypasses this limitation. As a result, different CPU cores can execute tasks simultaneously, making ProcessPoolExecutor ideal for CPU-bound operations such as mathematical computations and data processing.

## 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?

    If the system increases from 5 to 10,000 employees, Data Parallelism using ProcessPoolExecutor scales better for CPU-intensive tasks.

    With a large dataset, dividing employee salary computations across multiple processes allows full utilization of available CPU cores. Threads, on the other hand, are limited by the GIL for CPU-bound tasks and cannot achieve true parallel execution.

    However, for I/O-bound operations (such as fetching employee data from databases or APIs), a thread-based approach may still scale efficiently because threads can overlap waiting time.

## 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.

    In a real-world payroll system, Task Parallelism would be used for I/O-bound tasks like retrieving employee data, fetching tax information, and generating reports, using a ThreadPoolExecutor to handle multiple tasks simultaneously. Data Parallelism would be applied when computing salaries, taxes, and deductions for thousands of employees, using a ProcessPoolExecutor to distribute CPU-bound calculations across multiple cores for true parallel execution.

Contribution in the Activty:
- Task Parallelism Code
n/
 Patlonag, Pailagao
- Data Parallelism Code 
 Baring, Donos
- Q&A 
 Patlonag, Pailagao, Baring, Donos



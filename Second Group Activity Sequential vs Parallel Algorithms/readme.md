Sequential vs Parallel Algorithms - Individual Reflections

Ralph Laurenz Baring -


Franilyn Y. Pailagao -  in this activity, the Sequential searching algorithm using a linear search approach. the implementation followed a strict step by step order, checking each element against the target from index 0 to N-1 . During testing, i observed a clear linear relationship between the dataset size and execution time as the data scaled from 1,000 to 1,000,000 elements, the search time increased proportionally . A key insight from my part of the task was the impact of overhead. While parallel execution is designed for speed, my sequential search was highly efficient for the small dataset because it didn't incur the cost of process creation or inter-process communication. However, for the large dataset, the limitations of a single-core execution became obvious as the search took significantly longer than the parallel version managed by my groupmates. This experience highlighted that while sequential algorithms are easier to debug and have lower complexity, they lack the scalability required for modern, high volume data processing.


Dane Alexa C. Patlonag -


Dae Jay B. Doños - 
The activity demonstrated that the sequential linear search was faster than the parallel version for every dataset size. The main reason is that parallel processing adds extra work, such as creating multiple processes, splitting the data, and passing results through queues. Even with a dataset of 1,000,000 elements, the linear search stayed quick and efficient, while the overhead of parallelism slowed things down.

This makes it clear that parallel processing is not always better than sequential execution. It only becomes useful when the problem is very large and requires heavy computation, where the extra work is worth it. For simple tasks like linear search, sequential methods are usually more efficient because they avoid unnecessary complexity.

Overall, this activity helped me see that choosing between sequential and parallel algorithms depends on the size and difficulty of the problem. Parallelism works best for big, complex tasks, while sequential approaches are often the smarter choice for simpler ones.

Joshua Ganas - 

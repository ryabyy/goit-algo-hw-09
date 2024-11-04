**Goal:** Make functions that calculate the coins to be chosen, with their corresponding quantities for them, which would add up to a specified amount. Functions are to be implemented in greedy and in dynamic flavor, and their performance compared for time complexity.

**Algorithms used:**
- _Greedy algorithm_
- _Dynamic algorithm_

- **Results:**
The analysis of the performance of the algorithms demonstrates, as expected, that the greedy algorithm is performing significantly faster, which is especially visible for the relatively big target amounts.
This is an expected result, since the greedy algorithm is only assessing the next best move, not all different combinations that can lead to the target result.
Another advantage of the greedy algorithm is less usage of memory, since it's not keeping track of the target amounts and how to reach them (not doing memoization).
It should be noted, however, that the dynamic algorithm is guaranteed to produce the best result, an overall optimal one, which may differ from the results produced by the greedy algorithm, which makes a combination of local optima instead.

# Tasks 1 and 2: Side Channel Attacks via CPU Caches

In these first tasks we will study the technique **FLUSH+RELOAD** in order to perform a side channel (*CPU cache*) attack to steal a protected secret.


## Task 1: Reading from Cache versus from Memory

The cache memory is faster than the main memory. The goal of this task is to observe and take conclusions on the time difference in terms of providing data.

We start by compiling and running the *CacheTime.c* file 10 times.

The results we obtained in terms of memory access time are the following:

| Element      | Time (1) | Time (2) | Time (3) | Time (4)     | Time (5) | Time (6)  | Time (7) | Time (8)  | Time (9) | Time (10)  | Average Time Taken |  
| :----:       |  :----:  |   :----: |  :----:  |    :----:    |   :----: |  :----:   |  :----:  |   :----:  | :----:   |   :----:   |       :----:       |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this| Here's this        |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|Here's this         |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   | 
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|      Here's this   |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this|Here's this         |
| Header       | Title    | Here's th|Header    | Title        | Here's th|Header     | Title    | Here's thi|Title     | Here's this| Here's this        |




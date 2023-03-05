# Tasks 1 and 2: Side Channel Attacks via CPU Caches

In these first tasks we will study the technique **FLUSH+RELOAD** in order to perform a side channel (*CPU cache*) attack to steal a protected secret.


## Task 1: Reading from Cache versus from Memory

The cache memory is faster than the main memory. The goal of this task is to observe and take conclusions on the time difference in terms of providing data.

We start by compiling and running the *CacheTime.c* file 10 times.

The results we obtained in terms of memory access time (measured in CPU cycles) are the following:

| Element [k*4096]     | Time (1) | Time (2) | Time (3) | Time (4)     | Time (5) | Time (6)  | Time (7) | Time (8)  | Time (9) | Time (10)  | Average Time Taken |  
| :----:       |  :----:  |   :----: |  :----:  |    :----:    |   :----: |  :----:   |  :----:  |   :----:  | :----:   |   :----:   |       :----:       |
| A[0]      | 132    | 138|1290    | 120        | 124 |160     | 100    | 126|  104    | 174| **245**       |
| A[1]       |  260   | 860|372    | 304       | 418| 232     | 282    | 242| 288     | 1174| **443**        |
| A[2]       | 300    | 392|374    | 334        | 268|256     | 256    | 416| 264     | 278|   **314**   |
| A[3]       | 60    | 114|432    | 102        | 114|118     | 154    | 234| 124     | 168|      **162**   |
| A[4]       | 228    | 960| 304   | 240        | 262 |202     |  270   | 428| 260    | 308|      **346**   | 
| A[5]       |   232  | 216|308    |  340       | 256|  282   | 200    | 422| 234     | 282|      **277**   |
| A[6]       | 216    | 252|214    |    234     | 274|  206    | 266    | 448| 276     | 390 |      **278**   |
| A[7]       | 86    | 122|138    |     114    | 134| 140     | 124    | 278| 114     | 168 |      **142**   |
| A[8]       | 296    | 230|512    | 236       | 260| 238     |  234  | 372| 278     |  306| **296**         |
| A[9]       | 244   | 260|272    | 246        | 270|  236    | 250    | 420| 240     | 274| **295**        |




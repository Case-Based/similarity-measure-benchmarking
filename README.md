# Benchmarking of similarity measure algorithms
This repository aims to benchmark different similarity measure algorithms on their performance, especially with large data sets.

It's part of a scientific paper on case-based reasoning, and it will determine which similarity measure algorithms and the CBR library written in Python we will use for the work.

## List of similarity measure algorithms
These are selected similarity measure algorithms that will be benchmarked in this repository.

- Euclidian Distance
- Squared Euclidian Distance
- Manhatten Distance
- Chebychev Distance
- Cosine Distance
- Pearson Distance
- Canberra Distance

## Results
Each algorithm is compared to all the others, which is how we can determine the fastest algorithm to calculate the distance between two data points.
Additionally, we compared the time it took to get the 5 or 10 nearest neighbors of a specified algorithm compared to another. 
Since we're using k-nearest-neighbors in our original library, this is an important metric to capture.

All benchmarks have been made with 100.000 randomly generated numeric data entries. Each data entry has ten items, which make up 1.000.000 items combined.

<img width="1216" alt="Screenshot 2024-08-04 at 19 11 37" src="https://github.com/user-attachments/assets/89cbbd5d-1465-400b-837e-af791048753c">
<img width="1216" alt="Screenshot 2024-08-04 at 19 12 02" src="https://github.com/user-attachments/assets/431cf077-9ddb-4da0-aa61-8c3ab49e3ca9">


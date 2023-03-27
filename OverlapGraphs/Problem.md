# Overlap Graphs

问题详见：

https://rosalind.info/problems/grph/

**Given:** A collection of [DNA strings](https://rosalind.info/glossary/dna-string/) in [FASTA format](https://rosalind.info/glossary/fasta-format/) having total length at most 10 [kbp](https://rosalind.info/glossary/kbp/).

**Return:** The adjacency list corresponding to O3O3. You may return edges in any order.

## Sample Dataset

```
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
```

## Sample Output

```
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
```
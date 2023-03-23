## Finding a Most Likely Common Ancestor

In [“Counting Point Mutations”](https://rosalind.info/problems/hamm/), we calculated the minimum number of symbol mismatches between two strings of equal length to model the problem of finding the minimum number of point mutations occurring on the evolutionary path between two [homologous](https://rosalind.info/glossary/homologous/) [strands](https://rosalind.info/glossary/strand/) of [DNA](https://rosalind.info/glossary/dna/). If we instead have several homologous strands that we wish to analyze simultaneously, then the natural problem is to find an average-case strand to represent the most likely common ancestor of the given strands.



## Problem

https://rosalind.info/problems/cons/



**Given:** A collection of at most 10 [DNA strings](https://rosalind.info/glossary/dna-string/) of equal length (at most 1 [kbp](https://rosalind.info/glossary/kbp/)) in [FASTA format](https://rosalind.info/glossary/fasta-format/).

**Return:** A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

## Sample Dataset

```
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
```

## Sample Output

```
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
```
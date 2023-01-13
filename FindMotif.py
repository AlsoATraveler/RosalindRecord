with open('subs.txt', 'r') as f:
    Seq = f.readline().strip()
    Motif = f.readline().strip()
    SeqLen = len(Seq)
    MotifLen = len(Motif)
    ListAddr = []
    for i in range(SeqLen):
        SubSeq = Seq[i : i + MotifLen]
        # Use "is" when judging, then the length of ListAddr is 0 
        # (note the difference between "is" and "==").
        if(SubSeq == Motif): 
            ListAddr.append(i+1)
    # One of the methods of printing list in python3 (default space separated)
    print(*ListAddr)

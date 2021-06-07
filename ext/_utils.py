def allcases(string):
    n = len(string)
    mx = 1 << n
    inp = string.lower()
    allcombs = []
      
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
   
        temp = ""
        for i in combination:
            temp += i
        allcombs.append(temp)
    return allcombs
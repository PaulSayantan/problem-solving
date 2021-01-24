def pageCount(n, p):
    if p % 2 == 0:
        start = 2
        end = n if n % 2 == 0 else n-1
        if p == start:
            return 1
        if p == end:
            return 0
        if p == start + 1:
            return 2
        if p == end - 1:
            return 0
    else:
        start = 1
        end = n if n % 2 != 0 else n-1
        if p == start or p == end:
            return 0
        if p == start + 1:
            return 1
        if p == end - 1:
            return 0
    count = 0
    if p >= (end + start) // 2:
        # at the end
        while end != p:
            end -= 2    
            count += 1
            if p == end:
                break
    else:
        # at the beginning
        while start != p:
            start += 2
            count += 1
            if p == start:
                break
    
    return count

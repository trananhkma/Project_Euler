def is_increasing_num(n):
    """
    Return True if n is increasing number
    Return None if n is bouncy number
    """
    s = str(n)
    s = s[0] + s.lstrip(s[0])
    if len(s) == 1:
        return True
    for i in range(len(s)):
        if i == 1:
            if int(s[i]) > temp:
                increasing_num = True
            else:
                increasing_num = False
        if i > 1:
            if increasing_num == True:
                if int(s[i]) >= temp:
                    continue
                else:
                    return None
            else:
                if int(s[i]) <= temp:
                    continue
                else:
                    return None
        temp = int(s[i])
    return increasing_num


if __name__ == '__main__':
    n = 1
    bouncys = 0
    while n < 1000:
        if is_increasing_num(n) is None:
            bouncys += 1
        n += 1
    print bouncys

    count = 0
    proportion = 50.0000000
    # proportion = 90.000000
    i = 100
    while True:
        if is_increasing_num(i) is None:
            count += 1
        a = float(count)*100/i
        if a == proportion:
            print i
            break
        i += 1

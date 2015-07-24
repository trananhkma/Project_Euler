def is_bouncy(n):
    s = str(n)
    inc = False
    dec = False
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            inc = True
        if s[i] < s[i+1]:
            dec = True
        if inc and dec:
            return True
    return False

if __name__ == '__main__':
    count = 0
    proportion = 99.000
    i = 100
    while True:
        if is_bouncy(i):
            count += 1
        a = float(count)*100/i
        if a == proportion:
            print i
            break
        i += 1

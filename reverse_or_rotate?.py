def revrot(string, sz):
    def reverse_or_rotate(s):
        if len(s) < sz:
            return ""
        if sum(int(d) ** 3 for d in s) % 2 == 0:
            return s[::-1]
        return s[1:] + s[0]

    if string == "" or sz <= 0 or len(string) < sz:
        return ""
    return ''.join(map(reverse_or_rotate,
                       [string[i:i+sz] for i in range(0, len(string), sz)]))

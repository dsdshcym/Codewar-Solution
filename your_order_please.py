import re

def order(sentense):
    if not sentense:
        return ""
    words = sentense.split()
    ans = [""] * len(words)
    for word in words:
        order = re.search(r"\d", word).group(0)
        ans[int(order) - 1] = word
    return " ".join(ans)

assert(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
print("tests passed")

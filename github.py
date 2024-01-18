import random as r

with open("randint","w",encoding="utf-8") as f:
    a=[str(r.randint(1,10)) for i in range(10)]
    for i in range(10):
        f.write(a.pop(0)+' ')
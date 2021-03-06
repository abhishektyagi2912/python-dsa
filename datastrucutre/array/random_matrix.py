def random_matrix(n):
   
    from random import shuffle

    a = list(range(n + 1))
    shuffle(a)

    m = [a[i:] + a[:i] for i in range(n + 1)]

    shuffle(m)

    m = list(map(list, zip(*m)))  
    shuffle(m)

    return m


m = random_matrix(9)
print('\n'.join(map(str, m)))

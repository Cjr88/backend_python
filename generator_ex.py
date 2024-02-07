def my_gen():
    n= 1
    print('First print, n = a {}'.format(n))
    yield n

    n += 1
    print('Second print, n = a {}'.format(n))
    yield n

    n += 1
    print('Third print, n = a {}'. format(n))
    yield n
    
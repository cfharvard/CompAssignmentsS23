def sum(lst, n):
    # Your code here!
    total = 0
    for i in lst:
        total += i
    return total == n


def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()

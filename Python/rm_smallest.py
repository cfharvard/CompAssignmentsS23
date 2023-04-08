def rm_smallest(d):
    # Your code here!
    if not bool(d):
        return d
    d.pop(min(zip(d.values(), d.keys()))[1])
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()

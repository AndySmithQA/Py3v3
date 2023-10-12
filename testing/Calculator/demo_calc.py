def add(*args):
    """
    Takes a variable number of numbers and adds them together
    >>> add(3,4)
    7
    >>> add(10,20,30)
    60
    """
    total = 0
    for nums in args:
        total += nums
    return total

def mul(*args):
    """
    Takes a variable number of numbers and adds them together
    >>> mul(3,4)
    12
  """
    total = 1
    for nums in args:
        total *= nums
    return total

def div(x, z):
    """
    Takes a variable number of numbers and adds them together
    >>> div(4,3)
    1.333
    """
    return float(f"{x/z:.3f}")

def main():
    print(f"4 + 3 = {add(4,3)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
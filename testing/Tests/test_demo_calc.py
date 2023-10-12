from Calculator import demo_calc

def test_add():
    assert demo_calc.add(4, 3) == 7, "Error, Should return 7"
    assert demo_calc.add(10,20,30) == 60, "Should be 60"
    return None

def test_mul():
    assert demo_calc.mul(4,3) == 12, "Should be 12"
    return None

def test_div():
    assert demo_calc.div(4,3) == 1.333, "Should Return 1.333"
    return None

def main():
    test_add()
    test_mul()
    test_div()
    print("Everything passed")

if __name__ == "__main__":
    main()
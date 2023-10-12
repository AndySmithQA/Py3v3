from Calculator import shapes


def test_rect():
    assert shapes.rect(5,6) == 31, "Should be 30"

def main():
    test_rect()

if __name__ == "__main__":
    main()
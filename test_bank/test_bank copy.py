import bank

def test_starts_with_hello():
    assert bank.value("hello, world") == 0
    assert bank.value("Hello, everyone") == 0
    assert bank.value("HELLO") == 0

def test_starts_with_h():
    assert bank.value("hi there") == 20
    assert bank.value("Hey, how are you?") == 20
    assert bank.value("Holidays") == 20

def test_starts_with_other():
    assert bank.value("goodbye") == 100
    assert bank.value("What's up?") == 100
    assert bank.value("12345") == 100

if __name__ == "__main__":
    test_starts_with_hello()
    test_starts_with_h()
    test_starts_with_other()
    print("All tests passed!")

from jar import Jar


def test_init():
    # Test default initialization
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

    # Test initialization with custom capacity
    jar2 = Jar(8)
    assert jar2.capacity == 8
    assert jar2.size == 0

    # Test initialization with invalid capacity
    try:
        Jar(-5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative capacity"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # Test depositing more than capacity
    try:
        jar.deposit(10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for exceeding capacity"

    # Test depositing negative number of cookies
    try:
        jar.deposit(-2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative number of cookies"


def test_withdraw():
    jar = Jar()
    jar.deposit(5)

    jar.withdraw(3)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

    # Test withdrawing more cookies than present
    try:
        jar.withdraw(5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for withdrawing more cookies than present"

    # Test withdrawing negative number of cookies
    try:
        jar.withdraw(-2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative number of cookies"


if __name__ == "__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

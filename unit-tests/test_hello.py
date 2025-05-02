from hello import hello

def test_hello():
    assert hello("world") == "Hello, world!"
    assert hello("Alice") == "Hello, Alice!"
    assert hello() == "Hello, world!"  # Test default value
    assert hello("Bob") == "Hello, Bob!"  # Test with a different name
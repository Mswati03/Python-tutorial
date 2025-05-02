from hello import hello

def test_default():
    assert hello() == "Hello, world!"  # Test default value
    

def test_argument():
    assert hello("Charlie") == "Hello, Charlie!"  # Test with a different name

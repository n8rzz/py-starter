from src.greeter import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"
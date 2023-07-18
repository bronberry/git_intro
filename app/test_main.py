import pytest
from main import print_hello

def test_answer():
    assert print_hello() == 'hello'
import pytest

import pytest
from main import addme

def test_addme():
    assert addme(1, 2) == 3
    assert addme(10, 20) == 30
    assert addme(10, -2) == 8

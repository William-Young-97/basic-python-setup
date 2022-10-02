from msilib.schema import Error
from maths import Basics

def test_add():
    basics = Basics()
    assert basics.add(2, 2) == 4

def test_error():
    basics = Basics()
    raise basics.forceError()

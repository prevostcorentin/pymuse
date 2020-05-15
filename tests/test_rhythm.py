from ..pymuse import rhythm
from ..pymuse import Signature
import pytest

def test_multiply():
    rhythm_2 = Signature(2, 4)
    rhythm_3 = Signature(3, 4)
    assert rhythm.multiply(rhythm_2, rhythm_3) == Signature(6, 4)

def test_multiple_of():
    rhythm_2 = Signature(2, 4)
    rhythm_3 = Signature(6, 4)
    assert rhythm_2.multiple_of(rhythm_3)

def test_not_multiple_of():
    rhythm_2 = Signature(2, 4)
    rhythm_3 = Signature(3, 4)
    assert not rhythm_2.multiple_of(rhythm_3)
	
def test_multiply_wrong_divisors():
	with pytest.raises(rhythm.WrongDivisor):
		rhythm.multiply(rhythm.Signature(2, 6), rhythm.Signature(2, 8))

def test_common_signature_primes():
    rhythm_2 = Signature(2, 4)
    rhythm_7 = Signature(7, 4)
    assert rhythm.common_signature(rhythm_2, rhythm_7) == Signature(2 * 7, 4)

def test_common_signature_binary():
    rhythm_4 = Signature(4, 4)
    rhythm_2 = Signature(2, 4)
    assert rhythm.common_signature(rhythm_4, rhythm_2) == Signature(2, 4)

def test_common_signature_ternary():
    rhythm_3 = Signature(3, 4)
    rhythm_12 = Signature(12, 4)
    assert rhythm.common_signature(rhythm_3, rhythm_12) == Signature(3, 4)

def test_common_signature_ternary_binary():
    rhythm_4 = Signature(4, 4)
    rhythm_3 = Signature(3, 4)
    assert rhythm.common_signature(rhythm_4, rhythm_3) == Signature(4 * 3, 4)

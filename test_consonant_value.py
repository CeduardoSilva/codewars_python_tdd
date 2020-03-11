import pytest

def solve(str):
    result = 0
    for char in str:
        if not(isVowel(char)): 
            if characterValue(char) > result: result = characterValue(char)
    return result

def characterValue(char):
    return(ord(char)-96)

def isVowel(char):
    return char in ['a','e','i','o','u']

## TESTS

def test_a_single_vowel():
    assert(solve("a") == 0)

def test_a_single_consonant():
    assert(solve("b") == 2)

def test_a_vowel_string():
    assert(solve("aaiiee") == 0)

def test_zodiac_string():
    assert(solve("zodiac") == 26)
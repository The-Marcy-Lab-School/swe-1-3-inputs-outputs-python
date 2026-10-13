from from_scratch import (
    censor,
    clean_username,
    describe_total,
    extract_domain,
    format_name,
    rotate,
    rounder,
    starts_with_vowel,
)

TEST_SUITE_NAME = "From Scratch Tests"


def test_format_name():
    """format_name - capitalizes each name properly"""
    assert format_name("MarY", "JAne") == "Mary Jane"
    assert format_name("ada", "lovelace") == "Ada Lovelace"
    assert format_name("ZO", "SMITH") == "Zo Smith"


def test_starts_with_vowel():
    """starts_with_vowel - True when the word begins with a vowel"""
    assert starts_with_vowel("apple") is True
    assert starts_with_vowel("Iguana") is True
    assert starts_with_vowel("banana") is False
    assert starts_with_vowel("Zebra") is False
    # An empty word starts with nothing, so it does not start with a vowel.
    # Watch out: `"" in "aeiou"` is True, which catches people here.
    assert starts_with_vowel("") is False


def test_extract_domain():
    """extract_domain - returns everything after the @"""
    assert extract_domain("user@example.com") == "example.com"
    assert extract_domain("simple@test") == "test"
    assert extract_domain("a.b@mail.co.uk") == "mail.co.uk"


def test_rotate():
    """rotate - moves characters from the end to the front"""
    assert rotate("hello", 1) == "ohell"
    assert rotate("hello", 3) == "llohe"
    assert rotate("xyz", 3) == "xyz"
    assert rotate("test", 0) == "test"


def test_clean_username():
    """clean_username - trims the spaces and lowercases what is left"""
    assert clean_username("  Ada  ") == "ada"
    assert clean_username("ZO\n") == "zo"
    assert clean_username("Mixed Case") == "mixed case"
    assert clean_username("already") == "already"


def test_describe_total():
    """describe_total - formats the amount to two decimal places"""
    assert describe_total("Coffee", 3.5) == "Coffee: $3.50"
    assert describe_total("Tax", 0.07) == "Tax: $0.07"
    assert describe_total("Books", 12) == "Books: $12.00"
    assert describe_total("Odd", 1.005) == "Odd: $1.00"


def test_censor():
    """censor - replaces every copy of the word with stars"""
    assert censor("I love beets", "beets") == "I love *****"
    assert censor("no match here", "beets") == "no match here"
    assert censor("beets and beets", "beets") == "***** and *****"
    assert censor("", "beets") == ""

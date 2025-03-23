"""Test file for dictionary code"""

__author__: str = "730650345"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert1() -> None:
    """Test use case for invert function"""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert2() -> None:
    """Test another use case for invert function"""
    assert invert({"comp": "110", "North": "Carolina"}) == {
        "110": "comp",
        "Carolina": "North",
    }


def test_invert3() -> None:
    """Test edge case for invert function"""
    assert invert({}) == {}


def test_count1() -> None:
    """Test use case for count function"""
    assert count(["dog", "cat", "dog"]) == {"dog": 2, "cat": 1, "dog": 2}


def test_count2() -> None:
    """Test another use case for count function"""
    assert count(["unc", "duke", "ncsu", "wake", "unc"]) == {
        "unc": 2,
        "duke": 1,
        "ncsu": 1,
        "wake": 1,
        "unc": 2,
    }


def test_count3() -> None:
    """Test edge case for count function"""
    assert count([]) == {}


def test_favorite_color1() -> None:
    """Test use case for favorite_color function"""
    assert (
        favorite_color(
            {
                "Sam": "Blue",
                "Will": "Green",
                "James": "Blue",
                "Greg": "Yellow",
                "Tim": "Yellow",
            }
        )
        == "Blue"
    )


def test_favorite_color2() -> None:
    """Test another use case for favorite_color"""
    assert (favorite_color({"g": "red", "f": "blue", "s": "red", "a": "blue"})) == "red"


def test_favorite_color3() -> None:
    """Test edge case for favorite_color"""
    assert (favorite_color({})) == ""


def test_bin_len1() -> None:
    """Test use case for bin_len"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    """Test another use case for bin_len"""
    assert bin_len(["am", "go", "great"]) == {2: {"am", "go"}, 5: {"great"}}


def test_bin_len3() -> None:
    """Test edge case for bin_len"""
    assert bin_len([]) == {}

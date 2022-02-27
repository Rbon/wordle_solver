from hypothesis import given, strategies as st
from torch import get_rng_state
import wordle_solver as current
from tests import stable_functions as stable

@given(st.tuples(st.text()), st.characters())
def test_filter_contains(xs, y):
    assert current.filter_contains(xs, y) == stable.filter_contains(xs, y)

@given(st.tuples(st.text()), st.characters())
def test_remove_matches(xs, ys):
    assert current.remove_matches(xs, ys) == stable.remove_matches(xs, ys)

@given(st.characters())
def test_generate_words(chars):
    assert current.generate_words(chars) == stable.generate_words(chars)

@given(st.tuples(st.text()), st.text(), st.integers(max_value=99))
def test_filter_at_position(xs, y, pos):
    assert (
        current.filter_at_position(xs, y, pos)
        == stable.filter_at_position(xs, y, pos)
    )
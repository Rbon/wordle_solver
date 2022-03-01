from hypothesis import given, strategies as st
from torch import get_rng_state, miopen_depthwise_convolution
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
    output = current.generate_words(chars)
    assert output == stable.generate_words(chars)
    assert type(output) is tuple
    assert type(output[0]) is tuple
    assert type(output[0][0]) is str

@given(
    st.lists(st.text(min_size=5, max_size=5)),
    st.characters(), st.integers(min_value=0, max_value=4))
def test_filter_not_at_position(xs, y, pos):
    assert current.filter_not_at_position(xs, y, pos) \
        == stable.filter_not_at_position(xs, y, pos)

@given(
    st.lists(st.text(min_size=5, max_size=5)),
    st.characters(), st.integers(min_value=0, max_value=4))
def test_filter_at_position(xs, y, pos):
    assert current.filter_at_position(xs, y, pos) \
        == stable.filter_at_position(xs, y, pos)

# @given(st.iterables(st.text()))
# def test_fancy_print(iterable):
#     assert current.fancy_print(iterable) == stable.fancy_print(iterable)

@given(st.text(), st.text())
def test_parse(left, right):
    command = left + " = " + right
    assert current.parse(command) == stable.parse(command)

@given(st.lists(st.tuples(st.characters(), st.characters())))
def test_make_info(pairs):
    assert current.make_info(pairs) == stable.make_info(pairs)

@given(st.lists(st.tuples(st.text(min_size=5, max_size=5))))
def test_filter_actual_words(guesses):
    assert current.filter_actual_words(guesses) \
        == stable.filter_actual_words(guesses)

@given(
    st.lists(st.tuples(
        st.characters(whitelist_categories=["Ll"]),
        st.integers(min_value=0, max_value=4))),
    st.lists(st.tuples(
        st.characters(whitelist_categories=["Ll"]),
        st.characters(whitelist_categories=["Ll"]),
        st.characters(whitelist_categories=["Ll"]),
        st.characters(whitelist_categories=["Ll"]),
        st.characters(whitelist_categories=["Ll"]))))
def test_filter_with_greens(greens, words):
    assert current.filter_with_greens(greens, words) \
        == stable.filter_with_greens(greens, words)

# def filter_with_yellows(yellows, unknown, words):
#     "filtering yellows..." |> print
#     output = words
#     for i in yellows:
#         output = filter_not_at_position(output, i[0], i[1])
#         output = filter_at_any_of(output, i[0], unknown)
#     output = output |> tuple
#     'yellow guesses: ' + (output |> len |> str) |> print
#     return output

# def filter_at_any_of(xs, y, ps) =
#     xs |> filter$(at_any_of$(y, ps)) |> tuple

# def at_any_of(y, ps, x):
#     for p in ps:
#         if x[p] == y:
#             return True
#     return False

# def count_vowels(word) = word |> filter $ (x -> x in 'aeiouy') |> tuple |> len

# def reveal_4_vowel_words(word):
#     if (word |> count_vowels) == 4:
#         if not (len(word) != len(set(word))): # filter dupes
#             print word

# def reveal_5_vowel_words(word):
#     if (word |> count_vowels) == 5:
#         if not (len(word) != len(set(word))): # filter dupes
#             print word   

# @given(

#     st.lists(st.tuples(
#         st.characters(whitelist_categories=["Ll"]),
#         st.integers(min_value=0, max_value=4))),

#     st.lists(st.tuples(
#         st.characters(whitelist_categories=["Ll"]),
#         st.integers(min_value=0, max_value=4))),

#     st.lists(st.characters(whitelist_categories=["Ll"])),
#     st.lists(st.integers(min_value=0, max_value=4)))

# this is not ideal, but this function takes forever to generate tests
# def test_step():
#     info = {
#         'greens': [('a', 0), ('p', 1), ('l', 3)],
#         'yellows': [('p', 4)],
#         'bads':['d'],
#         'unknown': [2, 4]}
#     assert current.step(info) == stable.step(info)
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
    assert current.generate_words(chars) == stable.generate_words(chars)

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

# def step(info) =
#     'abcdefghijklmnopqrstuvwxyz' \
#     |> remove_matches$(info["bads"]) \
#     |> exec_time$(generate_words) \
#     |> exec_time$(filter_with_greens$(info['greens'])) \
#     |> exec_time$(filter_with_yellows$(info['yellows'], info['unknown'])) \
#     |> exec_time$(filter_actual_words)

# def filter_actual_words(guesses):
#     "filtering actual words..." |> print
#     output = [x for x in guesses if ''.join(x) in words.all_words]
#     'possible solutions: ' + (output |> tuple |> len |> str) |> print
#     return output


# def exec_time(f, *args):
#     start_time = time.perf_counter()
#     output = f(*args)
#     end_time = time.perf_counter()
#     "finished in: " + (end_time - start_time |> str) + '\n' |> print
#     return output

# def filter_with_greens(greens, words):
#     "filtering greens..." |> print
#     output = words
#     for i in greens:
#         output = filter_at_position(output, i[0], i[1])
#     output = output |> tuple
#     'green guesses: ' + (output |> len |> str) |> print
#     return output

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
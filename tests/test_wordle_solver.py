from hypothesis import given, strategies as st
from torch import get_rng_state, miopen_depthwise_convolution
import wordle_solver as current
from tests import stable_functions as stable

# this is not ideal, but this function takes forever to generate tests
def test_step():
    assert current.step("apdlp = ggbgy") == stable.step("apdlp = ggbgy")
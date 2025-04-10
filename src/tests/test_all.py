import pytest
import rspx


def test_sum_as_string():
    assert rspx.sum_as_string(1, 1) == "2"

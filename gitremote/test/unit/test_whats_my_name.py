import pytest

from gitremote.whats_my_name import my_name_is


def test_my_name_is():
    assert "Hu" == my_name_is()
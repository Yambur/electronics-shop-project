from src.keyboard import Keyboard
import pytest

"""Тесты для keyboard с использованием pytest"""


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    assert str(kb) == "Dark Project KD87A"
    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"

    kb.change_lang()
    assert kb.language == "EN"
    #  gpt
    with pytest.raises(AttributeError, match="Скажем другому языку - НЕ СЕГОДНЯ!"):
        kb.language = "CH"


"""Tests for ReplayLine - pure parsing and formatting logic."""

import pytest
import sys
import os

# Helper_Scripts is the script directory; ensure imports resolve
sys.path.insert(0, os.path.dirname(__file__))

from replay_line import ReplayLine, TEMPLATE_STRING, COUNT_PLACEHOLDER, DATE_PLACEHOLDER


SAMPLE = "### Replay Count = 42 (as of 03/06/26)"


class TestReplayLineParsing:
    def test_parses_count(self):
        r = ReplayLine(SAMPLE)
        assert r.replayCount == 42

    def test_parses_date(self):
        r = ReplayLine(SAMPLE)
        assert r.date == "03/06/26"

    def test_parses_large_count(self):
        r = ReplayLine("### Replay Count = 1234 (as of 01/01/25)")
        assert r.replayCount == 1234

    def test_parses_count_zero(self):
        r = ReplayLine("### Replay Count = 0 (as of 01/01/25)")
        assert r.replayCount == 0


class TestReplayLineToString:
    def test_roundtrip(self):
        r = ReplayLine(SAMPLE)
        assert r.to_string() == SAMPLE

    def test_contains_count(self):
        r = ReplayLine(SAMPLE)
        assert "42" in r.to_string()

    def test_contains_date(self):
        r = ReplayLine(SAMPLE)
        assert "03/06/26" in r.to_string()

    def test_format_matches_template_structure(self):
        r = ReplayLine(SAMPLE)
        line = r.to_string()
        assert line.startswith("### Replay Count = ")
        assert " (as of " in line
        assert line.endswith(")")


class TestIsReplayLine:
    def test_matching_line_returns_true(self):
        assert ReplayLine.is_replay_line(SAMPLE) is True

    def test_matching_line_with_newline_returns_true(self):
        assert ReplayLine.is_replay_line(SAMPLE + "\n") is True

    def test_non_matching_returns_false(self):
        assert ReplayLine.is_replay_line("# Regular heading") is False

    def test_empty_string_returns_false(self):
        assert ReplayLine.is_replay_line("") is False

    def test_partial_prefix_returns_false(self):
        assert ReplayLine.is_replay_line("## Replay Count") is False


class TestReplayLineEquality:
    def test_equal_counts_are_equal(self):
        a = ReplayLine("### Replay Count = 42 (as of 01/01/25)")
        b = ReplayLine("### Replay Count = 42 (as of 02/02/26)")
        assert a == b

    def test_different_counts_are_not_equal(self):
        a = ReplayLine("### Replay Count = 42 (as of 01/01/25)")
        b = ReplayLine("### Replay Count = 43 (as of 01/01/25)")
        assert a != b

    def test_not_equal_to_non_replay_line(self):
        r = ReplayLine(SAMPLE)
        assert r != "not a ReplayLine"

    def test_not_equal_to_none(self):
        r = ReplayLine(SAMPLE)
        assert r != None

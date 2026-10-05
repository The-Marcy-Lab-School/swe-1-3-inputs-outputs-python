import builtins

from modify import order_summary, print_receipt

TEST_SUITE_NAME = "Modify Tests"


def printed(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def feed(monkeypatch, answers):
    """Stand in for a person typing, one answer per input() call."""
    supply = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda *a: next(supply))


def test_order_summary_asks_for_everything(monkeypatch, capsys):
    """order_summary - takes its values from input()"""
    feed(monkeypatch, ["Tea", "3", "1.25", "n"])
    order_summary()
    assert printed(capsys) == ["3 x Tea", "Total: $3.75"]


def test_order_summary_gift_is_a_boolean(monkeypatch, capsys):
    """order_summary - turns a Y or N answer into a boolean"""
    feed(monkeypatch, ["Mug", "1", "10", "y"])
    order_summary()
    assert printed(capsys) == ["1 x Mug", "Total: $10.00", "Gift wrapped."]

    feed(monkeypatch, ["Mug", "1", "10", "Y"])
    order_summary()
    assert "Gift wrapped." in printed(capsys)


def test_print_receipt_uses_sep_and_end(capsys):
    """print_receipt - prints the items on one line and keeps the total inline"""
    print_receipt(["Tea", "Mug"], 11.25)
    assert printed(capsys) == ["Tea, Mug", "Total: $11.25"]

    print_receipt(["Solo"], 1)
    assert printed(capsys) == ["Solo", "Total: $1.00"]

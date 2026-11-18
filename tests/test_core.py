import tempfile
from pathlib import Path

from parades_toxins_1r_kit.core import ParadesToxins1rTool


def test_summarize_numeric_column():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.csv")
        path.write_text("x,y\n1,2\n3,4\n", encoding="utf-8")
        stats = ParadesToxins1rTool().summarize(path)
        assert stats["x"]["n"] == 2 and stats["x"]["mean"] == 2.0


def test_missing_file_returns_empty():
    assert ParadesToxins1rTool().summarize("/no/such.csv") == {}


def test_skips_non_numeric_rows():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "b.csv")
        path.write_text("x\n1\nnot-a-number\n", encoding="utf-8")
        assert ParadesToxins1rTool().summarize(path)["x"]["n"] == 1

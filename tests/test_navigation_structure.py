from pathlib import Path

APP = Path(__file__).resolve().parents[1] / "app.py"


def test_five_primary_navigation_tabs_are_declared():
    source = APP.read_text(encoding="utf-8")
    expected = [
        "1 · TỔNG QUAN",
        "2 · DÒNG TIỀN & BẪY GIÁ",
        "3 · SCANNER",
        "4 · PHÂN TÍCH CHI TIẾT",
        "5 · SWING TRADING",
    ]
    start = source.index("main_tabs = st.tabs([")
    end = source.index("])", start)
    nav = source[start:end]
    assert all(label in nav for label in expected)
    assert source.count("with main_tabs[0]:") == 1
    assert source.count("with main_tabs[1]:") == 1
    assert source.count("with main_tabs[2]:") == 1
    assert source.count("with main_tabs[3]:") == 2  # Quant/analysis and assistant share this tab.
    assert source.count("with main_tabs[4]:") == 1

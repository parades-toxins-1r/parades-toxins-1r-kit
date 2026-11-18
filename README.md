# parades-toxins-1r-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m parades_toxins_1r_kit.cli --help
```

```python
from parades_toxins_1r_kit.core import ParadesToxins1rTool

tool = ParadesToxins1rTool()
print(tool)
```

## Layout

```
parades_toxins_1r_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 parades-toxins-1r

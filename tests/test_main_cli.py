import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def test_help_exits_zero() -> None:
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "main.py"), "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "RepoTutor" in result.stdout

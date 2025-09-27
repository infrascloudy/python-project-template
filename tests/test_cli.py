from typer.testing import CliRunner
from project_name.cli import app

def test_hello():
    runner = CliRunner()
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.stdout

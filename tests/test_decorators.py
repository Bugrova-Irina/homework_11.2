import pytest

from src.decorators import log


def test_log():
    @log("/logs/my_log.txt")
    def my_function(a, b):
        return a + b

    assert my_function(1, 2) == 3


def test_filename_decorator():
    @log("/logs/my_log.doc")
    def my_function(a, b):
        return a + b

    with pytest.raises(NameError, match="Файл с неверным расширением"):
        my_function(1, 2)


def test_no_filename(capsys):
    # @wraps(test_no_filename)
    @log()
    def my_function(a, b):

        return a + b

    "Function my_function started"
    my_function(1, 2)
    "Function my_function finished"
    captured = capsys.readouterr()
    assert captured.out == "Function my_function started\n3\nmy_function ok\nFunction my_function finished\n"

from pie_package import __version__
from pie_package import pie_package

def test_version():
    assert __version__ == '0.1.0'

def test_show_pies():
    assert type(pie_package.show_pie()) == type("str")
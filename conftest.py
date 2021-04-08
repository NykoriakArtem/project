import os
import pytest
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--wd", action="store", default="local", help="WD host URL: local")


def pytest_configure(config):
    os.environ["SIMPLE_SETTINGS"] = "settings.base"
    if config.getoption("wd") == "local":
        os.environ["WD_URL"] = "http://localhost:4444/wd/hub"
    else:
        pytest.exit("Incorrect --wd option. WD Host URL: local")
    return config

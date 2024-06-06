import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome.options import Options

from utils.constants import download_dir
from datetime import datetime, timezone


chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Tensor HTML Report"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Tensor test"


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.now(timezone.utc)}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

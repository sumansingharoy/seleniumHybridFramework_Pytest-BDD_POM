import logging
import os
import subprocess
import pytest
import allure
from datetime import datetime
from selenium import webdriver

from testFolder.config.ReadConfigurations import ReadConfigurations
from testFolder.util.WebDriverFactory import WebDriverFactory # using config.ini
from allure_commons.types import AttachmentType


@pytest.fixture(scope="session")
def config():
    """Reads config.ini using your ReadConfigurations class"""
    read_config = ReadConfigurations()
    return {
        "browser": read_config.read_configurations("Basic Info", "browser"),
        "url": read_config.read_configurations("Basic Info", "url"),
        "headless": read_config.read_configurations("Basic Info", "headless") == "yes",
        "implicit_wait": int(read_config.read_configurations("Basic Info", "implicit_wait")),
    }


@pytest.fixture(scope="function")
def browser(config):
    """Initialize WebDriver using WebDriverFactory"""
    driver = WebDriverFactory().get_driver(config)
    driver.implicitly_wait(config["implicit_wait"])
    driver.maximize_window()
    driver.get(config["url"])
    # logging.info(f"BROWSER RESOLUTION: {str(driver.get_window_size())}")
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    outcome = yield  # Let the step run first
    try:
        driver = request.getfixturevalue("browser")

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            step_name = step.name.replace(" ", "_").replace("/", "_")
            screenshot_dir = r"C:\Users\suman\PycharmProjects\pythonHybridFramework\behaveBDDHybridFrameworkPageObjModel - Copy\seleniumSelfFramework\testFolder\SupportFiles\screenShot"
            os.makedirs(screenshot_dir, exist_ok=True)  # Ensure folder exists
            screenshot_path = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")

            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name=step.name, attachment_type=AttachmentType.PNG)

            # Enrich report dynamically
            allure.dynamic.description(f"Step: {step.name}")
            allure.dynamic.title(f"Scenario: {scenario.name}")
            allure.dynamic.feature(feature.name)

    except Exception as e:
        print(f"[ERROR] Failed to capture screenshot for step '{step.name}': {e}")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    try:
        results_dir = r"C:\Users\suman\PycharmProjects\pythonHybridFramework\behaveBDDHybridFrameworkPageObjModel - Copy\seleniumSelfFramework\testFolder\reports\allure-results"
        report_dir = r"C:\Users\suman\PycharmProjects\pythonHybridFramework\behaveBDDHybridFrameworkPageObjModel - Copy\seleniumSelfFramework\testFolder\reports\allure-report"
        # Remembter/Note that (Run the test like this):--
        #  pytest testFolder/project/tutorialDemo/step_defination/test_search_step.py --alluredir=testFolder/reports/allure-results

        # Ensure directories exist
        if not os.path.exists(results_dir):
            print(f"[WARNING] Allure results directory not found: {results_dir}")
            return

        # Generate the Allure report
        allure_path = r"C:\Users\suman\AppData\Roaming\npm\node_modules\allure-commandline\dist\bin\allure.bat"
        subprocess.run([allure_path, "generate", results_dir, "-o", report_dir, "--clean"], check=True)
        print(f"\n✅ Allure report generated successfully at: {os.path.abspath(report_dir)}")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Allure report generation failed (subprocess error): {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error during Allure report generation: {e}")


        # Run this command to generate the report ->> allure serve "./testFolder\reports\allure-results"

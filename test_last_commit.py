from pytest_bdd import given, when, then, scenario
from selenium.webdriver.common.by import By


@scenario('Features/git_last_commit.feature',
          'Last commit on django main page')
def test_last_commit_in_header():
    pass


@given("I have number of last commit on commits git django page")
def get_last_commit_rev(driver):
    driver.get("https://github.com/django/django/commits/master")
    last_commit_rev_number = driver.find_elements(
        By.CSS_SELECTOR, ".commit-links-cell a.sha")[0].text
    return last_commit_rev_number


@when("I open main git django page")
def open_main_django_page(driver):
    driver.get("https://github.com/django/django")


@then("Number of commit in header is the same as number of last commit")
def check_commit_rev_num_in_proj_header(get_last_commit_rev, driver):
    commit_number_from_header = driver.find_element(
        By.CSS_SELECTOR, ".commit-tease a.commit-tease-sha").text
    assert commit_number_from_header == get_last_commit_rev, "Commit numbers " \
                                                             "are not equal"

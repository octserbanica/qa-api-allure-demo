
import requests
import allure

BASE_URL = "https://api.github.com"

@allure.feature("GitHub API")
@allure.story("Get valid user")
def test_valid_user():
    response = requests.get(f"{BASE_URL}/users/octocat")

    with allure.step("Validate status code"):
        assert response.status_code == 200

    with allure.step("Validate response content"):
        data = response.json()
        assert data["login"] == "octocat"


@allure.feature("GitHub API")
@allure.story("Invalid user")
def test_invalid_user():
    response = requests.get(f"{BASE_URL}/users/user_that_should_not_exist_123")

    with allure.step("Check 404 response"):
        assert response.status_code == 404

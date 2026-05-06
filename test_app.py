from selenium import webdriver

def test_homepage():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    assert "App Connected" in driver.page_source
    driver.quit()
def test_title():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    assert driver.title != ""
    driver.quit()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global Mname,Yof,Dirname,Distributor,Producer,driver
    Mname = input("Enter the movie name")
    Yof = input("Enter the movie released year :")
    Dirname = input("enter the director name")
    Distributor = input("enter the distributor")
    Producer = input("Enter the producing company")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.close()
    time.sleep(5)

def test_Moviedata(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(Mname)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(Yof)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(Dirname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)

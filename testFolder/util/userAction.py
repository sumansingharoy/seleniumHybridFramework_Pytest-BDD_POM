from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

ecWait = 30
class UserAction:

    def __init__(self, browser):
        self.browser = browser

    def click(self, byLocator):
        elm = WebDriverWait(self.browser, ecWait).until(EC.element_to_be_clickable(byLocator))
        try:
            # scroll into view to avoid MoveTargetOutOfBounds
            self.browser.execute_script("arguments[0].scrollIntoView(true);", elm)
            elm.click()
        except Exception as e:
            print(f"[ERROR] Failed to click element {byLocator}: {e}")
            raise

    def getTitle(self):
        return self.browser.title
    
    def sendKeys(self, byLocator, txt:str, clear=True):
        if clear:
            WebDriverWait(self.browser,ecWait).until(EC.visibility_of_element_located(byLocator)).clear()
        WebDriverWait(self.browser, ecWait).until(EC.visibility_of_element_located(byLocator)).send_keys(txt)

    def getText(self, byLocator):
        elm = WebDriverWait(self.browser, ecWait).until(EC.visibility_of_element_located(byLocator))
        return elm.text
    
    def getAttributeValue(self, byLocator):
        elm = WebDriverWait(self.browser, ecWait).until(EC.visibility_of_element_located(byLocator))
        return elm.get_attribute("value")
        
    
    def getAttributeByName(self, byLocator, name:str):
        elm = WebDriverWait(self.browser, ecWait).until(EC.visibility_of_element_located(byLocator))
        return elm.get_attribute(name)
    
    def is_product_link_visible(self, byLocator):
        elm = WebDriverWait(self.browser,ecWait).until(EC.visibility_of_element_located(byLocator))
        try:
            return elm.is_displayed()
        except TimeoutException:
            return False
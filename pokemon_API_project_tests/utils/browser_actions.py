from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementNotVisibleException, NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BrowserActions:
    def element_is_present(self, browser, xpath):
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True


browser_action = BrowserActions()

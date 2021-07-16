from selenium import webdriver

WEBDRIVERS = {"chrome": webdriver.Chrome, "firefox": webdriver.Firefox, "edge": webdriver.Edge}


def init_driver(browser_name, driver_path):
    if browser_name.lower() in WEBDRIVERS:
        driver = WEBDRIVERS[browser_name](driver_path)
    else:
        raise Exception("invalid browser name")

    return driver


def search_items(driver, search_link):
    # todo keep searching for items until found
    # return link
    pass


def purchase_item(driver, link, payment_method):
    # todo purchase the item using the link
    # purchase the item return bool
    pass

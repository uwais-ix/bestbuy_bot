from selenium import webdriver

WEBDRIVERS = {"chrome": webdriver.Chrome, "firefox": webdriver.Firefox, "edge": webdriver.Edge}


def init_driver(browser_name, driver_path):
    if browser_name.lower() in WEBDRIVERS:
        driver = WEBDRIVERS[browser_name](driver_path)
    else:
        raise Exception("invalid browser name")

    return driver


def search_items(driver, search_link, wait_time=2, partial_link_text_target="Available to ship"):
    while True:
        try:
            driver.get(search_link)
            driver.implicitly_wait(wait_time)
            elem = driver.find_element_by_partial_link_text(partial_link_text_target)
        except:
            continue
        else:
            return elem


def add_to_cart(driver, link, cart_class_name_target="addToCartLabel_YZaVX"):
    try:
        link.click()
    except:
        raise Exception("invalid item link, purchase failed")
    else:
        driver.implicitly_wait(2)
        elem = driver.find_element_by_class_name(cart_class_name_target)
        elem.click()


def checkout(driver, payment_method, cvv, place_order_class_name="content_3Dbgg", cvv_class_name="content_3Dbgg"):
    try:
        driver.get("https://www.bestbuy.ca/en-ca/basket")
        elem = driver.find_element_by_class_name(place_order_class_name)
        elem.click()
        elem = driver.find_element_by_id("cvv")
        elem.clear()
        elem.send_keys(cvv)
        elem = driver.find_element_by_class_name(cvv_class_name)
        elem.click()
    except:
        raise Exception("failed to checkout")

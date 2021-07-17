from selenium import webdriver
import selenium

WEBDRIVERS = {"chrome": webdriver.Chrome, "firefox": webdriver.Firefox, "edge": webdriver.Edge}


def init_driver(browser_name, driver_path):
    if browser_name.lower() in WEBDRIVERS:
        driver = WEBDRIVERS[browser_name](driver_path)

    else:
        raise Exception("invalid browser name")

    return driver


def enter_text(element, text):
    element.clear()
    element.send_keys(text)


def find_target_element(driver, target_method, target_name):
    driver_dict = {
        "id": driver.find_element_by_id,
        "name": driver.find_element_by_name,
        "xpath": driver.find_element_by_xpath,
        "link_text": driver.find_element_by_link_text,
        "partial_link_text": driver.find_element_by_partial_link_text,
        "tag_name": driver.find_element_by_tag_name,
        "class_name": driver.find_element_by_class_name,
        "css_selector": driver.find_element_by_css_selector
    }
    if target_method in driver_dict:
        target_func = driver_dict[target_method]
        try:
            elem = target_func(target_name)
            return elem
        except:
            raise Exception("failed to target element: ", "target name")
    else:
        print('invalid')
        raise Exception("invalid target method")


def wait(driver, params):
    driver.implicitly_wait(int(params['wait_time']))


def load(driver, params):
    driver.get(params['url'])
    wait(driver, params)



def search(driver, params):
    while True:
        try:
            load(driver, params)
            wait(driver, params)
            elem = find_target_element(driver, params['target_method'], params['target_name'])
            elem.click()
            break
        except:
            continue


def input_text(driver, params):
    elem = find_target_element(driver, params['target_method'], params['target_name'])
    try:
        enter_text(elem, params['text'])
    except:
        raise Exception("unable to input text")


def click(driver, params):
    elem = find_target_element(driver, params['target_method'], params['target_name'])
    try:
        elem.click()
    except:
        raise Exception("unable to click on element")


def execute_actions(driver, actions):
    ACTIONS = {"load": load, "search": search, "input text": input_text, "click": click, "wait": wait}
    for (task_name, params) in actions.items():
        print("Executing :", task_name)
        print(params["action"])
        ACTIONS[params["action"]](driver, params)
    return True


# BestBuy Bot

**Script** written in Python and uses  [Selenium](https://selenium-python.readthedocs.io/index.html) to automatically purchase an item (gpu recommended) once it is in stock. 

The script can also be configured to work on any website if the purchase can be made using the supported action sets.

Actions : 

Load -> loads requested webpage

Search -> keeps searching for targeted element until found and clicks on it

Wait -> implicitly wait for async elements on the page to load

Input Text -> inputs text into the targeted element 

Click -> clicks on the targeted element



# Setup
- download and install [python](https://www.python.org/downloads/) 
- install [selenium driver](https://selenium-python.readthedocs.io/installation.html) (section 1.5) for the browser you are going to use
- setup [venv](https://docs.python.org/3/tutorial/venv.html) and install [selenium using pip](https://selenium-python.readthedocs.io/installation.html#1.2)
- configure config.json
- run script (main.py)
- script will start searching
- log in into your account in a new tab


## config.json

| settings  | actions |
|--|--|
| selenium setup  | actions executed by bot |


## Settings

| browser name | driver path |
|--|--|
| "chrome" | path of [driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) on local machine|
| "firefox" | path of [driver](https://github.com/mozilla/geckodriver/releases) on local machine |
| "edge" | path of [driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) on local machine |
	

## Element Targetting

Only **single element** target supported. 
See [documentation](selenium-python.readthedocs.io/locating-elements.html) to understand how target works. 

> dictionary key = target_method
> 
> target_name = target_method parameter

 

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
       

 
## Supported Actions 

		   "task 1 name":{
		     "action": "load",
		     "url" : "page you want to load here",
		     "wait_time" : "1"
		    },
           "task 2 name": {
             "action": "search",
        	 "url": "conduct search in this url",
             "target_method": "",
             "target_name": "",
             "wait_time": "2"
           },
           "any name you like" : {
             "action" : "input text",
             "target_method": "",
             "target_name": "",
             "text": "cvv"
           },
           "name here": {
             "action" : "click",
             "target_method" : "",
             "target_name" : ""
           },
           "name of task here": {
             "action": "wait",
             "wait_time" : "2"
           }

## Note / Issues
- runs only once, stops on Exception
- tested with google chrome only
- everything lowercase in config file
- use wait to avoid targeting async elements that have not yet loaded
- see the config.json to see example of best buy bot


# Buying Bot

### Overview

A configurable bot written using Python and Selenium.

### Motive

During the current silicon shortage, it has been overly difficult to buy a graphics card (and other components) as they are being sold out minutes after being restocked. 

This configurable bot supports a set of actions that should allow you to automatically purchase any products you want once correctly configured.

# Setup

 - Selenium WebDriver
 - Selenium API
 - Python Script
 - Actions
 - Config File   
 - Usage 
 
## Selenium WebDriver  

> Selenium WebDriver is a browser automation framework that accepts commands and sends them to a browser. It is implemented through a browser-specific driver.

In other words, Selenium WebDriver allows your browser to be controlled by the script.  

So you need to download the correct WebDriver for the browser you wish to use the script with.

| Browser Name | Driver  |
| --| --|
|Chrome 			| [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads) |
|Firefox			| [Download](https://github.com/mozilla/geckodriver/releases) |
|Edge 				| [Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |

If links are outdated, try [here](https://selenium-python.readthedocs.io/installation.html#drivers).

## Selenium API

The API provides bindings (in python) to access functionality of the WebDriver.

This script uses the API for

 1. Single Element Targeting
 2. Wait 

### Single Element Targeting
The end user should know about the DOM to be able to target their desired elements.

Refer to the Selenium documentation [here](https://selenium-python.readthedocs.io/locating-elements.html#) for more details.
\
The script uses the following driver dictionary to provide a mapping to selenium API functions.
```
driver_dict = {  
	 	 "id"			  : driver.find_element_by_id,  
	  	 "name"	          	  : driver.find_element_by_name,  
	  	 "xpath"		  : driver.find_element_by_xpath,  
	  	 "link_text"	  	  : driver.find_element_by_link_text,  
	  	 "partial_link_text"      : driver.find_element_by_partial_link_text,  
	  	 "tag_name"	 	  : driver.find_element_by_tag_name,  
	  	 "class_name"		  : driver.find_element_by_class_name,  
	  	 "css_selector"	  	  : driver.find_element_by_css_selector  
	      }
```
\
In the **config file**, the key of the `driver_dict` is referred as the value for the following

``` "target_method" :   ```

\
For example if you want to target an element by `driver.find_element_by_id`, you will have the following in your config file

``` "target_method" : "id" ```

\
You will also have to provide the id of what you want to target in your config file.

``` "target_name" : "id-being-targeted-here" ```

You can think of the `target_name` as a parameter or argument for the `target_method`


###  Wait

> When a page is loaded by the browser, the elements within that page may load at different time intervals. This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception. Using waits, we can solve this issue.


The script supports only implicit wait and not explicit waits. 

This means that you will have to tell WebDriver to wait x seconds in the config file.

> "wait_time" : "2" 

## Python Script

This script has two classes:

 1. Configuration
 2. Selenium bot
 
 The settings and actions executed by the script is configurable using the config.json file.
 
 The code in Selenium bot currently throws exception when an action fails. 
 You can modify the code to do something to handle that exception.
 For example : use a logger, repeat the action or execute a different action..

## Actions

### Load
Example in config file : 

```
"load cart": {  
	        "action" 	: "load",  
		"url" 		: "https://www.bestbuy.ca/en-ca/basket",  
		"wait_time" 	: "100"
             }
```

\
Loads a requested `"url"`  

### Search 
 Example in config file : 

```
"search page until stock found": {
				    "action" 		: "search",  
				    "url" 		: "https://www.bestbuy.ca/en-ca/search?search=rtx+laptop",  
				    "wait_time" 	: "2",  
				    "target_method" 	: "partial_link_text",  
				    "target_name" 	: "Available to ship"  
                                 }
```

\
This action keeps reloading the page at an interval of `"wait_time"` until **targeted element** is **found** and **clicks** on it.

### Wait 
You can and should wait for async elements on the page to load before continuing to execute your actions.

Example in config file of explicitly waiting 2 sec : 

```
"wait for checkout page to load completely": {  
						"action" : "wait",  	
						"wait_time" : "2"  
					     }
```

### Input Text
This action inputs text into the targeted element. 

You should use this to login (or other related actions) before you start executing other actions.

Example in config file :

```
"enter cvv in text field": {  
			        "action" 	: "input text",  
				"target_method" : "id",  
				"target_name" 	: "cvv",  
				"text"		: "123"  
			   }
```

### Click 
This action clicks on the  targeted element.

Example in config file :

```
"click on place order" : {  
			      "action" 		: "click",  
			      "target_method" 	: "class_name",  
			      "target_name" 	: "content_3Dbgg"  
			  }
```

## Config File
The config.json file is used to configure the script. 

The JSON file consists of the following:

 1. Settings
 2. Actions

```
{
	"settings": { 
			"browser name" : "chrome", 
			"driver path"  : "WebDriver path here"
		    }
	
	"actions" " {
			"action1name" { 
					 "property1" : "value1",
					 "property2" : "value2"
				      } 
		    }			
}
```  




### Supported Actions
Full list of all the supported actions 

```
 "actions": {  
 		"action 1 name": {
					"action"    : "load",  
					"url"       : "load url here",  
					"wait_time" : "1"  
		},  
		
		"action 2 name": {  	
					"action"    	: "search",  	
					"url"       	: "url",  
					"target_method"	: "",  
					"target_name"	: "",  
					"wait_time"	: "2"  
		},  
			  
		"action 3 name": {  
					"action" 	: "input text",  
					"target_method" : "",  
					"target_name"	: "",  
					"text"		: "cvv"  
		},  
		
		"action 4 name": {  
					"action" 	: "click",  
					"target_method" : "",  
					"target_name" 	: ""  
		},  
		
		"action 5 name": {  
					"action"    : "wait",  
					"wait_time" : "2"  
		}  
}
```

You give actions whatever name you would like to.

But the properties and values for each action is always required otherwise an Exception will be thrown.

For example : 

 - `"action":"wait"` should always have a `"wait_time" : "value here"
 -  Likewise for all the other actions listed above should have their all their properties and respective values



## Usage

 - Have [python](https://www.python.org/downloads/) installed.
 - Install [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html) for the browser you are going to use.
 - Setup a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and install [selenium using pip](https://selenium-python.readthedocs.io/installation.html#1.2).
 - Configure config.json
 - Run Script (<span>main.py</span>)
 
 Recommended configuration order:
 
 - Login first
 - The use search actions

# Conclusion

## Suggested Improvements

 - Create GUI interface
 - Create browser extension that can auto target elements, so that it can be used by non programmers
 - Use threads to implement multiple tabs support and multiple element targeting support
 - Implement explicit wait support
 - Regularly updated pre configured config files
 - Implement a logger
 - Auto notifier when a certain action occurs

## Notes
- Use \\ for driver path in config file 
- Use lowercase
- If an action fails, Exception is thrown
- Use wait to avoid targeting async elements that have not yet loaded
- Tested in chrome only

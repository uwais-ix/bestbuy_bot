# BestBuy Bot

**Script** written in Python and uses  [Selenium](https://selenium-python.readthedocs.io/index.html) to automatically purchase an item (gpu recommended) from the search list once it is in stock.  

# Setup
- download and install [python](https://www.python.org/downloads/) 
- install [selenium driver](https://selenium-python.readthedocs.io/installation.html) (section 1.5) for the browser you are going to use
- setup [venv](https://docs.python.org/3/tutorial/venv.html) and install [selenium using pip](https://selenium-python.readthedocs.io/installation.html#1.2)
- configure config.json
- run script (main.py)
- script will start searching
- log in into your account in a new tab


## config.json

All the following *keys* are **required** in the *config* file

- > payment method : "card" || "paypal"
- > search_url : "valid search url"
- > browser_name : "chrome" || "firefox" || "edge"
- > driver_path : "driver path of downloaded selenium driver" **use \\\ for the path**
- > cvv : "123" your cvv required for check out

## searching / search url

use the default search and filter options

 or

use " " for an exact match to the name of the product
>"product 1 name" "product 2 name" ..

## Issues
- tested with chrome browser only 
- functional with card payment only atm
- targeted elements change over time, will later update config to support targeted elements too
- runs only once, stops on Exception
- ..

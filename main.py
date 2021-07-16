from configuration import Configuration
import selenium_bot as bot

def main():
    config = Configuration()
    driver = bot.init_driver(config.browser_name,config.driver_path)
    item = bot.search_items(driver, config.search_url)
    purchase = bot.purchase_item(driver, item, config.payment_method)

if __name__ == '__main__':
    main()
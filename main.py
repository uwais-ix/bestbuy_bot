from configuration import Configuration
import selenium_bot as bot

def main():
    config = Configuration()
    driver = bot.init_driver(config.browser_name,config.driver_path)
    item = bot.search_items(driver, config.search_url)
    bot.add_to_cart(driver,item)
    if bot.checkout(driver, config.payment_method, config.cvv):
        print("checkout successful")

if __name__ == '__main__':
    main()
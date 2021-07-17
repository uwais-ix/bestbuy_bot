from configuration import Configuration
import selenium_bot as bot


def main():
    config = Configuration()
    driver = bot.init_driver(config.browser_name, config.driver_path)
    if bot.execute_actions(driver, config.actions):
        print("purchased item")


if __name__ == '__main__':
    main()

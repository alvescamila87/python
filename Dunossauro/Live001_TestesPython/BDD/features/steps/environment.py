from selenium import webdriver

driver = webdriver.Chrome()

def before_feature(context, feature):
    context.driver = webdriver.Chrome()


def after_feature(context, feature):
    context.driver.quit()
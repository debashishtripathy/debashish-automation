from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

# Dropdown Handlers:

def select_ddl_by_index(element_ddl,index):
    sct=Select(element_ddl)
    sct.select_by_index(index)


def select_ddl_by_value(element_ddl,value):
    sct=Select(element_ddl)
    sct.select_by_index(value)


def select_ddl_by_visible_text(element_ddl,text):
    sct=Select(element_ddl)
    sct.select_by_index(text)


def deselect_ddl_by_index(element_ddl,index):
    sct=Select(element_ddl)
    sct.select_by_index(index)


def deselect_ddl_by_value(element_ddl,value):
    sct=Select(element_ddl)
    sct.deselect_by_index(value)

def deselect_ddl_by_visible_text(element_ddl,text):
    sct=Select(element_ddl)
    sct.deselect_by_index(text)


def deselect_ddl_by_all(element_ddl):
    sct = Select(element_ddl)
    sct.deselect_by_all

#Features to handel mouse operations:


def mouse_hover_on_element(browser,element):
    act=ActionChains(browser)
    act.move_to_element(element).perform()


def drag_and_drop_elements(browser,src_element,target_element):
    act=ActionChains(browser)
    act.drag_and_drop(src_element,target_element).perform()


def right_click_on_element(browser,element):
    act=ActionChains(browser)
    act.context_click(element).perform()


def double_click_on_element(browser,element):
    act=ActionChains(browser)
    act.double_click(element).perform()





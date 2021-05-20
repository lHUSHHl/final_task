from .pages.product_page import ProductPage


def test_message_disappeared(browser):
    link = ' http://selenium1py.pythonanywhere.com/' \
           'catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_form()
    page.should_not_be_success_message()

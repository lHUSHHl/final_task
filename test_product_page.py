from .pages.product_page import ProductPage
from .pages.locators import AddProduct


def test_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" \
           "catalogue/" \
           "the-shellcoders-handbook_209/" \
           "?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_form()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add()
    page.should_be_price()

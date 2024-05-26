import pytest
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestProduct:
    def test_hp(self):
        home_page = HomePage(self.driver)
        home_page.select_laptop()
        home_page.add_to_cart()
        home_page.guest_account_and_purchase_product()
        home_page.payment_product()
        home_page.order_confirmation()

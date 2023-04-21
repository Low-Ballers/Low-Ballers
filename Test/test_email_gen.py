import pytest
from Low_Ballers.email_gen import data_email


def test_exists_data_email():
    actual = data_email('Amazon: 39.99 , amazon.com/shop?=34r3243242',
               'Best buy: 29.99 , walmart.com/shop?=34232424234',
               'Sears: 42.99, sears.com/shop?= 34234224',
               'Target: 36.99 target.com/shop?=3243243242',
               'Walmart: price not available',
               'Exchange: $50.00 , www.exchange.com')
    assert actual is None

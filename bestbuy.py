import asyncio
from playwright.async_api import async_playwright, ElementHandle

async def search_product_price(model_number: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to Best Buy website and search for the product
        await page.goto('https://www.bestbuy.com/')
        await page.click('#gh-search-input')
        await page.fill('#gh-search-input', model_number)
        await page.click('#search-button')

        # Wait for the search results to load and click on the first product
        await page.wait_for_selector('.sku-title a')
        product_link: ElementHandle = (await page.query_selector_all('.sku-title a'))[0]
        await product_link.click()

        # Wait for the product page to load and extract the price
        await page.wait_for_selector('.priceView-customer-price')
        price_element: ElementHandle = await page.query_selector('.priceView-customer-price')
        price = await price_element.inner_text()

        await browser.close()
    return price

asyncio.run(search_product_price('QN50LS03BAFXZA'))

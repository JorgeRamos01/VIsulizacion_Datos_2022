from playwright.sync_api import sync_playwright
#import asyncio
 
def main():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.simplyhired.mx/company/Teleperformance')
 
        all_items = page.query_selector_all('div[class="col-md-8 CompanyReviews"] > article')
        books = []
        for item in all_items:
            book = {}
            value = item.query_selector('div:nth-child(1) > span')
            book['value'] = value.inner_text()
            temp = item.query_selector('div:nth-child(2)')
            temp = str(temp.inner_text()).split("|")
            book['puesto']= temp[0][:-1]
            book['lugar']= temp[1][1:-1]
            book['dateReview']= temp[2][1:]
            try:
            	button= item.query_selector('div:nth-child(4) > button')
            	button = str(button.inner_text())
            	if button=="... más":
            		item.query_selector('div:nth-child(4) > button').click()
            		review = item.query_selector('div:nth-child(4) > span')
            		book['review'] = review.inner_text()
            except:
            	review = item.query_selector('div:nth-child(4) > span')
            	book['review'] = review.inner_text()

            books.append(book)
        print(books)
        browser.close()
 
if __name__ == '__main__':
	main()
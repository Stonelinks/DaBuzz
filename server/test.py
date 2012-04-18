import html_extract
import company_extract
import string

#url = """http://www.marketwatch.com/news/story.asp?guid=%7B2E738CC0-8963-11E1-82E5-002128049AD6%7D&siteid=rss&rss=1"""
#html = html_extract.text_from_url(url)
#words = html_extract.bag_of_words(html)

words = """
san francisco marketwatch canadian equities traded mostly lower wednesday with technology shares leading the decline but health care stocks provided some support on the heels of a rally in sxc health solutions corp the bank of canada released its full quarterly monetary policy report a day after the central bank held its overnight lending rate at 1 the report has helped to provide some support to markets as it reiterated tuesdays comments that the central bank may start to withdraw monetary stimulus said colin cieszynski market analyst at cmc markets in emailed comments on balance the themes of communiqu were repeated but by virtue of having more space the messaging sounds more balanced than the communiqu said david tulk chief canada macro strategist at td securities in a note while this may help canadian fixed income and the currency consolidate following its recent moves nothing has fundamentally changed with respect to the outlook for the overnight rate he said under pressure from wall street energy companies and lawmakers on capitol hill the nations commodity hong kong marketwatch china petroleum chemical corp better known as sinopec was in talks to sscs us made ultimate aero lefteasily tops 200 mph check out 10 of the worlds fastest super cars the action you requested requires a marketwatch community display name marketwatch community is a free service that lets you discover organize and share marketwatch stories with other readers the action you requested is only available to marketwatch members
"""

print company_extract.tickers_from_text(words)

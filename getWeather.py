from requests_html import HTMLSession

s = HTMLSession()

location = 'Lang lang'
url = f'https://www.google.com.au/search?q=weather+{location}'

r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first = True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
humidity = r.html.find('span#wob_hm', first = True).text

print(location, temp + unit, "Humidity " + humidity)
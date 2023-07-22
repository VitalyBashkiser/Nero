import asyncio, aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://www.hltv.org/team/4608/natus-vincere#tab-matchesBox"
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await response.text()
            soup = BS(r, "html.parser")
            items = soup.find_all("table", {"class": "table-container match-table"})
            for item in items:
                title = item.find("td", {"class": "team-center-cell"}).text.strip()
                image_container = item.find("span", {"class": "team-logo-container"})
                image_url = image_container.find("img")["src"] if image_container else None
                date = item.find("td", {"class": "date-cell"}).text.strip()

                print(title)
                print(date)
                print("URL:", image_url)
                print("Match")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

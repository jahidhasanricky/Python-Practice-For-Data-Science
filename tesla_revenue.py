import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in str(table):
        rows = table.find_all("tr")
        tesla_revenue = []
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) == 2:
                date = cols[0].text.strip()
                revenue = cols[1].text.strip().replace("$", "").replace(",", "")
                tesla_revenue.append([date, revenue])
        break

tesla_revenue_df = pd.DataFrame(tesla_revenue, columns=["Date", "Revenue"])
print(tesla_revenue_df.tail())

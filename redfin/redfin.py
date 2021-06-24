import os
import csv
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from db import Postgres


class Scraper:
    def __init__(self, url):
        self.url = url

        self.PATH = str(Path(__file__).parent)

        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://www.redfin.com/",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "text/plain;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        }

    def get_html(self, url):
        time.sleep(2.5)

        try:
            r = requests.get(url, headers=self.headers)
        except (requests.ConnectionError):
            print("Check your Internet connection!")
            return 0

        if r.status_code == 200:
            return r.text

        elif r.status_code == 403:
            print("You have been blocked!")
            return 0

        elif r.status_code == 404:
            print("Wrong URL...")
            return 0

    def main_link(self, page):
        url = self.url + f"/page-{page}"

        html = self.get_html(url)

        if html:
            papka_ind = 0
            path2 = f"{self.PATH}/osnova"
            rest = []
            csv_file = []
            path_for_img = []

            picture_blocks = self.soup.find_all("div", class_="bottomV2")

            list_price = None
            pricesqqft = None
            est_mo_payment = None
            buyers_crokerage_compensation = None
            redfin_estimate = None
            hoa_dues = None
            status = None
            time_on_redfin = None
            property_type = None
            year_built = None
            style = None
            community = None
            lot_size = None
            mls = None

            for block in picture_blocks:
                loko = []

                os.mkdir(path2 + "/" + str(papka_ind))

                path3 = path2 + f"/{papka_ind}"

                path_for_img.append(path3)
                oson = block.a

                page_url = oson["href"]
                page_url = "https://www.redfin.com" + page_url
                opa = self.get_html(page_url)
                page_soup_html = BeautifulSoup(opa, "html.parser")

                blocks_img = page_soup_html.find_all("img", class_="landscape")
                for img_block in blocks_img:
                    img_link = img_block["src"]

                    os.system(f"wget {img_link} -P {path3}")
                papka_ind += 1

            osnova = page_soup_html.find_all(
                "div", class_="keyDetail font-weight-roman font-size-base"
            )
            for norm_or_none in osnova:
                norm_or_none = norm_or_none.text
                if "List Price" in norm_or_none:
                    list_price = norm_or_none[11:].replace(",", "")
                if "Price/Sq.Ft." in norm_or_none:
                    pricesqqft = norm_or_none[13:].replace(",", "")
                if "Est. Mo. Payment" in norm_or_none:
                    est_mo_payment = norm_or_none[17:].replace(",", "")
                if "Buyer's Brokerage Commission" in norm_or_none:
                    buyers_crokerage_compensation = norm_or_none[28:]
                if "Redfin Estimate" in norm_or_none:
                    redfin_estimate = norm_or_none[16:].replace(",", "")
                if "HOA Dues" in norm_or_none:
                    hoa_dues = norm_or_none[9:]
                if "Status" in norm_or_none:
                    status = norm_or_none[6:]
                if "Time on Redfin" in norm_or_none:
                    time_on_redfin = norm_or_none[14:]
                if "Property Type" in norm_or_none:
                    property_type = norm_or_none[13:]
                if "Year Built" in norm_or_none:
                    year_built = norm_or_none[10:]
                if "Style" in norm_or_none:
                    style = norm_or_none[5:]
                if "Community" in norm_or_none:
                    community = norm_or_none[9:]
                if "Lot Size" in norm_or_none:
                    lot_size = norm_or_none[8:]
                if "MLS#" in norm_or_none:
                    mls = norm_or_none[4:]

            csv_file.append(
                list_price,
                pricesqqft,
                est_mo_payment,
                buyers_crokerage_compensation,
                redfin_estimate,
                hoa_dues,
                status,
                time_on_redfin,
                property_type,
                year_built,
                style,
                community,
                lot_size,
                mls,
            )

            addres = page_soup_html.find_all("div", class_="street-address")
            for addr in addres:
                ad = addr.span.text
                loko.append(ad)

            bed_bath = page_soup_html.find_all("div", class_="statsValue")
            for mnogoe in bed_bath:
                prin = mnogoe.text
                loko.append(prin)

            areas = page_soup_html.find_all("span", class_="statsValue")
            for area in areas:
                ar = area.text
                loko.append(ar)

            rest.append(loko)

            with open(f"{self.PATH}/infa.csv", "a") as csvfile:
                wr = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                wr.writerow(
                    [
                        "Price",
                        "Bedrooms",
                        "Bathrooms",
                        "Addres",
                        "Rest",
                        "List Price",
                        "Price Sq.Ft",
                        "Est. Mo. Payment",
                        "Buyer",
                        "Brokerage Compensation",
                        "Redfin estimate",
                        "HOA Dues",
                        "Status",
                        "Time on Redfin",
                        "Property Type",
                        "Year Built",
                        "Style",
                        "Community",
                        "Lot Size",
                        "MLS#",
                        "path_for_img",
                    ]
                )
            for i in range(len(csv_file)):
                wr.writerow([rest[i] + csv_file[i] + path_for_img])
            yield csv_file

    def amount_of_pages(self):
        html = self.get_html(self.url)

        if html:
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.find_all("a", class_="clickable goToPage")
            pages = []
            for block in pagination:
                span_block = block.text
                if span_block == "»":
                    pass
                else:
                    pages.append(int(span_block))

            return max(pages)
        else:
            return 0


if __name__ == "__main__":
    # dbname = input("The name of database: ")
    # dbuser = input("Username of database: ")
    # dbpswd = input(f"{dbuser}'s password: ")

    dbname = input("Your database name: ")
    dbuser = input("Your database user: ")
    dbpswd = input("Your database password: ")

    postgres = Postgres(db_name=dbname, user=dbuser, pswd=dbpswd)

    # site_url = input("Please type URL: ")
    site_url = "https://www.redfin.com/city/1826/MA/Boston"

    scraper = Scraper(url=site_url)
    pages_number = scraper.amount_of_pages()

    for page in range(1, pages_number + 1):
        scraper.main_link()

    postgres.end()

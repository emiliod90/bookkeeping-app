from random import choice
import httpx
from selectolax.parser import HTMLParser
from datetime import datetime


def httpx_get_company_info(company_number: str):
    """
    get_company_info
    ------------------
    Dependencies:
    - Companies House: Dependent on the company search service working as expected: https://find-and-update.company-information.service.gov.uk/search
    - httpx: Dependent on the HTTP client for HTTPX for web scraping. If required, code can be changed to utlise another HTTP client such as requests.

    References:
    - https://www.python-httpx.org/

    """
    company_number = str(company_number)
    user_agent_list = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.1; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    )

    user_agent = choice(user_agent_list)

    test_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "user-agent": user_agent,
    }

    with httpx.Client(http2=True) as client:
        response = client.get(
            f"https://find-and-update.company-information.service.gov.uk/company/{company_number}",
            headers=test_headers,
        )

    try:
        # print(response.http_version)
        response.raise_for_status()
        return {
            "html": response.text,
            "code": response.status_code,
            "error": "",
            "status": True,
        }
    except httpx.RequestError as exc:
        # print(f"An error occurred while requesting {exc.request.url!r}.")
        return {"html": "", "code": "HTTP Error", "error": exc, "status": False}
    except httpx.HTTPStatusError as exc:
        # print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return {"html": "", "code": response.status_code, "error": exc, "status": False}


def selectolax_parse_company_info(html: str):
    """
    parse_company_info
    ------------------
    Dependencies:
    - Companies House: The HTML/CSS website structure for Companies House information service does not change. Example: https://find-and-update.company-information.service.gov.uk/company/08085218
    - selectolax: Dependent on the selectolax HTML5 parser for use. If required, code can be changed to utlise another HTML5 Parser such as BS4.

    References:
    - https://selectolax.readthedocs.io/en/latest/parser.html
    - https://www.w3schools.com/cssref/css_selectors.php

    """
    parsed_html = HTMLParser(html)
    try:
        co_name = parsed_html.css_first("p.heading-xlarge").text()
        crn = parsed_html.css_first("p#company-number strong").text()
        co_address = parsed_html.css_first("dd.text").text().strip()
        co_status = parsed_html.css_first("dd#company-status").text().strip()
        co_type = parsed_html.css_first("dd#company-type").text().strip()
        inc_date = parsed_html.css_first("dd#company-creation-date").text().strip()
        accounts_date = (
            parsed_html.css_first("h2.heading-medium + p strong").text().strip()
        )
        sic_list = [
            each_node.text().strip()
            for each_node in parsed_html.css("h2#sic-title + ul li")
        ]
        inc_date__c = (
            datetime.strptime(inc_date, "%d %B %Y").date().strftime("%d/%m/%y")
        )
        accounts_date__c = (
            datetime.strptime(accounts_date, "%d %B %Y").date().strftime("%d/%m/%y")
        )

        return {
            "name": co_name,
            "crn": crn,
            "address": co_address,
            "status": co_status,
            "type": co_type,
            "inc_date": inc_date__c,
            "accounts_date": accounts_date__c,
            "sic_list": sic_list,
        }
    except ValueError:
        return {
            "name": co_name,
            "crn": crn,
            "address": co_address,
            "status": co_status,
            "type": co_type,
            "inc_date": inc_date,
            "accounts_date": accounts_date,
            "sic_list": sic_list,
        }
    except AttributeError:
        return {"error": "Company is either dissolved or could not be found"}

    else:
        return {"error": "Unknown error during html parsing - website may have changed"}


def scrape_company_info_service(company_number: str):
    scraped_html = httpx_get_company_info(company_number=company_number)
    if scraped_html["status"]:
        parsed_html = selectolax_parse_company_info(scraped_html["html"])
        return parsed_html
    else:
        error = scraped_html["code"]
        return {"error": error}


# scrape_company_info_service(10081688)

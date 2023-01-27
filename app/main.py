from fastapi import FastAPI
from dataclasses import dataclass
import random
import httpx
from selectolax.parser import HTMLParser

#https://www.python-httpx.org/advanced/
#https://stackoverflow.com/questions/71031816/how-do-you-properly-reuse-an-httpx-asyncclient-wihtin-a-fastapi-application
#https://www.scrapingbee.com/blog/best-python-http-clients/
#https://curlconverter.com/
#https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/
#https://find-and-update.company-information.service.gov.uk/company/14143549

app = FastAPI(title="Emilio FastAPI Demo")

def get_company_info(company_number: str):
    company_number = str(company_number)
    user_agent_list = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.1; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        )
        
    user_agent = random.choice(user_agent_list)

    test_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "user-agent": user_agent,
    }
        
    with httpx.Client() as client:
        response = client.get(f'https://find-and-update.company-information.service.gov.uk/company/{company_number}', headers=test_headers)

    try:
        response.raise_for_status()
        return {"html": response.text, "code": response.status_code, "error": "", "status": True}
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
        return {"html": "", "code": "HTTP Error", "error": exc, "status": False}
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return {"html": "", "code": response.status_code, "error": exc, "status": False}



test = get_company_info(141438)
test["html"]
test["status"]
test["error"]
test["code"]

test2 = get_company_info(14143549)
test2["html"]
test2["status"]
test2["error"]
test2["code"]

@dataclass
class Company:
    id_num: str
    name: str
    address: str
    status: str
    type: str
    date: str
    

def parse_html_company_house(html, company_number: str):
    parsed_html = HTMLParser(html.text)
    try:
        name = parsed_html.css_first("p.heading-xlarge").text()
        id_num: parsed_html.css_first("p.heading-xlarge").text()
        return name
    except AttributeError:
        return "Could not be found"


company = get_company_info("z")
company_name = parse_html_company_house(company)


company_name

# def get_company(comapany_id):
#     soup = BeautifulSoup(requests.get("https://find-and-update.company-information.service.gov.uk/company/{company_id}").content, "html.parser")
#     key = soup.find("p",class_="heading-xlarge")
#     return key

# get_company(14143549)


@app.get("/")
async def root():
    return {"message": "working"}

@dataclass
class Account:
    id: int
    name: str
    email: str



def get_my_company_service(company_number: str):
    get_company_info()
    return { Company()} 


@app.get("/company/{company_id}")
def find_company(company_id):
    html = get_company_info(company_id)
    # name = parse_html_company_house(html)
    return {"company_id": company_id, "name": html}
    
from datetime import date, timedelta, datetime

# datetime.date(2010, 6, 16).isocalendar().week

date.today().isoformat()


test1 = "31/05/2023"
test2 = "02 February 2023"
test3 = "2023-02-02"

datetime.strptime(test1, "%d/%m/%Y")
datetime.strptime(test2, "%d %B %Y").date().strftime("%d/%m/%y")

# datetime.date

# datetime.date(year=2023, month=2, day=2)


## Accounting period - Year End
# Date that my business fiscal year ends
## Eg., 31 May, start 1 June
##


def all_dates(year: int, month: int, day: int):
    input = date(year=year, month=month, day=day)
    short_date = input.strftime("%d/%m/%y")
    long_date = input.strftime("%d %B %Y")
    day = input.strftime("%A")
    isoformat = input.isoformat()
    isocalendar = input.isocalendar()

    return {
        "short_date": short_date,
        "long_date": long_date,
        "day": day,
        "isoformat": isoformat,
        "isoweekday": isocalendar.weekday,
        "isoweek": isocalendar.week,
    }


all_dates(year=2023, month=2, day=2)


def construct_tax(year: int, month: int = 4, day: int = 5):
    start = date(year=year, month=month, day=day)
    delta = timedelta(year=1)
    return start + delta


construct_tax(year=2022, month=4, day=5)


# First Accounts
"""
https://www.gov.uk/first-company-accounts-and-return
When you set up your limited company, you automatically get different reporting dates for the first:
- Annual accounts you send to Companies House
- Company Tax Return you send to HM Revenue and Customs (HMRC)

You may also have to send (‘file’) 2 tax returns to cover your first year in business.
"""

"""
Annual Accounts
Your company’s annual accounts - called ‘statutory accounts’ - are prepared from the company’s financial records at the end of your company’s financial year.
You must send copies to:
- all shareholders
- people who can go to the company’s general meetings
- Companies House
- HM Revenue and Customs (HMRC) as part of your Company Tax Return

You have different deadlines for sending your accounts to Companies House and your tax return to HMRC, but you may be able send them at the same time.

Statutory accounts must include:
- a ‘balance sheet’, which shows the value of everything the company owns, owes and is owed on the last day of the financial year
- a ‘profit and loss account’, which shows the company’s sales, running costs and the profit or loss it has made over the financial year
- notes about the accounts
- a director’s report

The balance sheet must have the name of a director printed on it and must be signed by a director.

Accounting Standards
Your statutory accounts must meet either:
- International Financial Reporting Standards
- New UK Generally Accepted Accounting Practice
"""


"""
Company Tax Returns
-------------------
Your company or association must file a Company Tax Return if you get a ‘notice to deliver a Company Tax Return’ from HM Revenue and Customs (HMRC).

You must still send a return if you make a loss or have no Corporation Tax to pay.

You do not send a Company Tax Return if you’re self-employed as a sole trader or in a partnership - but you must send a Self Assessment return.

When you file your tax return, you work out your:
- profit or loss for Corporation Tax (this is different from the profit or loss shown in your annual accounts)
- Corporation Tax bill

You can either get an accountant to prepare and file your tax return or do it yourself.

If you have a limited company, you may be able to file your accounts with Companies House at the same time as your tax return.

The deadline for your tax return is 12 months after the end of the accounting period it covers. You’ll have to pay a penalty for late filing if you miss the deadline.

There’s a separate deadline to pay your Corporation Tax bill. It’s usually 9 months and one day after the end of the accounting period.

"""

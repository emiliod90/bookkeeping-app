# Accounting glossary

https://www.xero.com/uk/glossary/
https://www.businessaccountingbasics.co.uk/bookkeeping-terms/
https://onlineaccountingguide.com/what-is-gross-profit-and-what-does-it-tell-us/
http://www.payrollsolutionsltd.co.uk/blog/wp-content/uploads/2022/01/Tax-Week-and-Month-calendar-2021-2022.pdf
https://paulcunningham.dev/python-date-time-fiscal-year/
https://blog.moneyfarm.com/en/financial-planning/uk-tax-year-dates-2022/#:~:text=When%20is%20the%20new%20tax,close%20on%20April%205th%2C%202023.

# Account

- Country
- First Name
- Last Name
- Company Name
- Company Number
- Registered office address (extract from company house)
- Company status (extract from company house)
- Incorporation date (extract from company house)
- Company Address (extract from company house)

## Search Company function

Link: https://find-and-update.company-information.service.gov.uk/company/{Company Number}

Use q = { Company Number }

For example

https://find-and-update.company-information.service.gov.uk/company/14143549

This should present the match found from company house:

web crawl the website for:

Compnay Name = <p class="heading-xlarge">ANALYSTS JOURNAL LTD</p>
Company Number = { Company Number }
Registered office address = 



# Starling Bank

https://github.com/Dullage/starlingbank
https://developer.starlingbank.com/docs#introduction-1

# Accounting period

- Select accounting period
- Tax Year 2022/2023
- Tax Year Start (auto: Apr 6 2022)
- Tax Year End (auto: Apr 5 2023)
- Calendar (auto generations)
- Corporation Tax rate
- Income Tax rates \*
- Dividend Tax rates \*

# Client/Customer

- Client Name
- Client Address
- Client Contact No.
- Client ID (auto generate)
- Client VAT no. (optional)

# Log Timesheet

User should specify:

- Client Name (dropdown)
- Period Week Start (Mondays only)
- Period Week End (Auto calculate)
- Day Rate
- Days worked
- Weekly total (auto calculate)
- Status (auto generate - draft - pending assignment - assigned)

# Log Expenses

User should specify:

- Period Week Start (Mondays only)
- Period Week End (Auto calculate)
- Days with expenses
- Expense type (dropdown)
- Expense amount
- Day total expense amount (auto calculate)
- Weekly total (auto calculate)
- Status (auto generate - draft - complete)

# Invoice

User should choose from "pending" timesheets

User should specify:

- VAT %
- Net
- VAT
- Total
- Invoice Date
- Invoice No. (auto generate or optional)
- Estimated/Expected pay date
- VAT No. (auto generate)
- Company No. (auto generate)
- Company Name (auto generate)
- Company Address (auto generate)
- Director Name (auto generate)
- Client Name (auto generate)
- Client Address (auto generate)
- Financial Week (auto generate)
- Financial Month (auto generate)
- Status (auto generate - draft - sent - settled)

When Invoice moves to sent, change timesheet status to assigned
When Invoice income is received, change Invoice to settled

# Reporting

Per work week based on period start and period end

- Period Start
- Period End
- Financial Year (auto generate)
- Financial Month (auto generate)
- Financial Week (auto generate)
- Invoice Date
- Expected Pay Date
- Days worked
- Day rate
- Net Revenue
- VAT %
- VAT (£)
- Gross Revenue
- Expe
- Corporation Tax %

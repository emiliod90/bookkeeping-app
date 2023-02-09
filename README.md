# Bookkeeping App
By Emilio


## Accounting glossary

https://www.xero.com/uk/glossary/
https://www.businessaccountingbasics.co.uk/bookkeeping-terms/
https://onlineaccountingguide.com/what-is-gross-profit-and-what-does-it-tell-us/
http://www.payrollsolutionsltd.co.uk/blog/wp-content/uploads/2022/01/Tax-Week-and-Month-calendar-2021-2022.pdf
https://paulcunningham.dev/python-date-time-fiscal-year/
https://blog.moneyfarm.com/en/financial-planning/uk-tax-year-dates-2022/#:~:text=When%20is%20the%20new%20tax,close%20on%20April%205th%2C%202023.

# How to setup python projects with Poetry and VSCode

https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2

# Account (Application)

This is the account for the application.

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

# Use cases

## Time tracking

### Scenario 1 - Emilio needs to fill out a timesheet for a work week

Assumptions:

- Emilio is doing contractual work - a single client contracted at a specified rate with a start and end date, with an agreed upon timesheet structure e.g., Client A weekly timesheet billed at rate A, Client B fortnightly timesheet billed at rate B
  - Data Entities: Client, Contract --> Time length, time structure, pay structure, pay rate
- Weekly time period - Monday start and Sunday end: Assumes UK western based work week. For other continents, work week is different, e.g., Dubai (UAE) is Sunday start - Sat end.
- Time worked per day - Full day, 3/4 day, 1/2 day, 1/4 day vs hours logged
  - For this scenario, all that matters is billable hours
- Rates applied

  - This could be based on a prepopulated custom rate selected by the user vs a free text field
  - scenarios where an end user works for more than one client at a time, on a given day, there could be different hours associated to one client, on one particular rate, vs a different rate for another client
  - will a timesheet be created on a per-client basis, or should the client be a filterable option per time worked within a timesheet (thus allowing multiple clients)
  - For other scenarios,

Data:

- Contract/Job

  - What is the job?: Context, Description
  - Who is the job for?: Client -- Name, Address, Contact Person VAT Number (if applicable), Agency -- Name, Address, Contact Person, VAT Number (if applicable)
  - When does the job begin?:
  - How long is the job for?: In days, weeks, months from start date (Job Term)
  - Working Hours (Normal working hours) AM - PM equivalent of working day: e.g., 8 hours = 1 Day
  - Working Days (work week): Mon - Sun
  - How much you charge for the job
    - Time based rate: rate per hour or rate per day or flat fee
    - If flat fee - work out what the day rate is,
    - If day rate - work out what the total is

  ### Scenario 2 - Emilio has freelance work

  - Timesheet needs to allow entry of adhoc work - a single client contracted at a specific rate for a piece of work
    - Need to think about whether the

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

# Theory

Modular programming - a software design approach that emphasizes separating the functionality of a program into groups or blocks of independent and interchangeable modules. Modules can be classes, functions or groups of classes and functions.

Cohesion:
Coupling:

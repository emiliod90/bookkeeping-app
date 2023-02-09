from dataclasses import dataclass
from datetime import datetime
from customer import Customer
from supplier import Supplier


@dataclass
class SelfBillInvoice:
    """
    SelfBillInvoice
    ---------------
    - Self-billing is an arrangement between a supplier and a customer.
    - Both customer and supplier must be VAT registered.
    - The customer prepares the supplier’s invoice and forwards a copy to the supplier with the payment.

    See more here:
    - https://www.gov.uk/guidance/vat-self-billing-arrangements
    - https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021#vat-invoices---the-basics
    - https://www.inniaccounts.co.uk/guides/agencies/self-billing/
    """
    id: int
    invoice_date: datetime
    pay_date: datetime
    pdf_url: str
    supplier: Supplier
    customer: Customer
    line_item: list[InvoiceLineItem]


@dataclass
class InvoiceLineItem:
    line_id: int
    week_start: datetime
    description: str
    quantity: int
    unit_price: float
    VAT_rate: int
    net: float = quantity * unit_price
    VAT: float = quantity * unit_price * VAT_rate
    gross: float = VAT + net
    currency: str = "£"
    week_end: datetime = week_start + 7
    





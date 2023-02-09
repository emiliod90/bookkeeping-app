from dataclasses import dataclass

@dataclass
class Supplier:
    """
    Supplier
    --------
    - name: Name of the company supplying the goods or services.
    - address: address of the company.
    - CRN: A company registration number is a combination of 8 numbers or 8 alpha-numeric characters.
    - VATREG: the VAT number of the company.
    """
    name: str
    address: str
    VATREG: str
    CRN: str 
    

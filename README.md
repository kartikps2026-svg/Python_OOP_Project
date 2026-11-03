# Employee Payroll System (Python OOP)

A small program demonstrating core Object-Oriented Programming concepts in Python.

## Concepts demonstrated

| Concept | Where |
|---|---|
| **Abstraction** | `Employee` is an abstract base class with the abstract method `calculate_pay()` |
| **Inheritance** | `SalariedEmployee`, `HourlyEmployee` extend `Employee`; `Manager` extends `SalariedEmployee` |
| **Polymorphism** | `run_payroll()` calls `calculate_pay()` on any employee type |
| **Encapsulation** | Private `__salary` with a validating `@property` setter |
| **Class attributes / classmethods** | `Employee._count` and `total_employees()` |
| **`super()` and dunder methods** | `Manager.calculate_pay()`, `__str__` |

## Run

```bash
python payroll.py
```

No external dependencies; requires Python 3.8+.

## Sample output

```
=== Monthly Payroll ===
[101] Alice (SalariedEmployee) -> Rs. 60,000.00
[102] Bob (HourlyEmployee) -> Rs. 54,750.00
[103] Carol (Manager) -> Rs. 105,000.00

Total payout: Rs. 219,750.00
```

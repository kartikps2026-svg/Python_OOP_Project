"""
Employee Payroll System
-----------------------
Demonstrates the Python OOP concepts of:
  * Abstraction     - abstract base class (ABC) with an abstract method
  * Inheritance     - subclasses reuse and extend the base class
  * Polymorphism    - one interface (calculate_pay), many behaviours
  * Encapsulation   - private attribute with property validation
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract base class: every employee must know how to calculate pay."""

    _count = 0  # class attribute shared by all instances

    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id
        Employee._count += 1

    @abstractmethod
    def calculate_pay(self) -> float:
        """Monthly pay. Each subclass must implement this."""

    def describe(self) -> str:
        return f"[{self.emp_id}] {self.name} ({self.__class__.__name__})"

    @classmethod
    def total_employees(cls) -> int:
        return cls._count

    def __str__(self) -> str:
        return f"{self.describe()} -> Rs. {self.calculate_pay():,.2f}"


class SalariedEmployee(Employee):
    """Fixed monthly salary."""

    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id)
        self.__salary = 0  # private attribute (name-mangled)
        self.salary = salary  # goes through the validated setter

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    def calculate_pay(self) -> float:
        return self.salary


class HourlyEmployee(Employee):
    """Paid per hour, with 1.5x overtime beyond 160 hours."""

    REGULAR_HOURS = 160

    def __init__(self, name, emp_id, rate, hours):
        super().__init__(name, emp_id)
        self.rate = rate
        self.hours = hours

    def calculate_pay(self) -> float:
        overtime = max(0, self.hours - self.REGULAR_HOURS)
        regular = self.hours - overtime
        return regular * self.rate + overtime * self.rate * 1.5


class Manager(SalariedEmployee):
    """Inherits from SalariedEmployee and adds a bonus plus a team."""

    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus
        self.team = []

    def add_member(self, employee: Employee):
        self.team.append(employee)

    def calculate_pay(self) -> float:
        # Extend the parent's behaviour instead of rewriting it
        return super().calculate_pay() + self.bonus


def run_payroll(employees):
    """Works with ANY Employee subclass - that's polymorphism."""
    total = 0.0
    for emp in employees:
        print(emp)
        total += emp.calculate_pay()
    return total


if __name__ == "__main__":
    alice = SalariedEmployee("Alice", 101, 60000)
    bob = HourlyEmployee("Bob", 102, rate=300, hours=175)
    carol = Manager("Carol", 103, salary=90000, bonus=15000)
    carol.add_member(alice)
    carol.add_member(bob)

    staff = [alice, bob, carol]

    print("=== Monthly Payroll ===")
    total = run_payroll(staff)
    print(f"\nTotal payout: Rs. {total:,.2f}")
    print(f"Total employees created: {Employee.total_employees()}")
    print(f"Carol manages: {[m.name for m in carol.team]}")

    # Abstraction: the base class cannot be instantiated
    try:
        Employee("Ghost", 999)
    except TypeError as err:
        print(f"\nAbstraction check: {err}")

    # Encapsulation: validation in the setter
    try:
        alice.salary = -100
    except ValueError as err:
        print(f"Encapsulation check: {err}")

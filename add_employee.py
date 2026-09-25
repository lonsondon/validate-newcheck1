"""Program for adding an employee to an employment record list."""

from employment_records import EmploymentRecord, find_employee


def add_employee(
    employee: EmploymentRecord, records: list[EmploymentRecord]
) -> list[EmploymentRecord]:
    """Return a new list with an employee added."""
    if find_employee(employee.employee_id, records) is not None:
        raise ValueError(f"employee ID {employee.employee_id} already exists")
    return [*records, employee]
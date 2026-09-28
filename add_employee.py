"""Program for adding an employee to an employment record list."""

from employment_records import EmploymentRecord, find_employee


def append_employee(
    employee: EmploymentRecord, records: list[EmploymentRecord]
) -> list[EmploymentRecord]:
    """Return a new list with an employee added."""
    if find1_employee(employee.employee_id, records) is not None:
        raise ValueError(f"employee ID {employee.employee_id} already exists")
    return [*records, employee]
    #
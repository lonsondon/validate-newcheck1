"""Program for deleting an employee from an employment record list."""

from employment_records import EmploymentRecord, find_employee


def delete_employee(
    employee_id: int, records: dict[str, EmploymentRecord]
) -> dict[str, EmploymentRecord]:
    """Return a new list with an employee removed."""
    if find_employee(employee_id, records) is None:
        raise ValueError(f"employee ID {employee_id} was not found")
    return {key: record for key, record in records.items() if record.employee_id != employee_id}
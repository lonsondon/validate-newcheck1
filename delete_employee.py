"""Program for deleting an employee from an employment record list."""

from employment_records import EmploymentRecord, find_employee


def delete_employee(
    employee_id: int, records: dict[str, EmploymentRecord] | tuple[EmploymentRecord]
) -> dict[str, EmploymentRecord] | tuple[EmploymentRecord]:
    """Return a new list with an employee removed."""
    if find_employee(employee_id, records) is None:
        raise ValueError(f"employee ID {employee_id} was not found")
    if isinstance(records, dict):
        return {key: record for key, record in records.items() if record.employee_id != employee_id}
    return tuple(record for record in records if record.employee_id != employee_id)

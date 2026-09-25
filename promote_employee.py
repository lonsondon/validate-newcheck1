"""Program for promoting an employee in an employment record list."""

from dataclasses import replace

from employment_records import EmploymentRecord, find_employee


def promote_employee(
    employee_id: str,
    new_job_title: str,
    new_salary: str,
    records: dict[str, EmploymentRecord],
    new_department: str | None = None,
) -> tuple[EmploymentRecord]:
    """Return a new list with an employee's role and salary updated."""
    employee = find_employee(employee_id, list(records.values()))
    if employee is None:
        raise ValueError(f"employee ID {employee_id} was not found")
    if new_salary < employee.salary:
        raise ValueError("promotion salary must not be lower than the current salary")

    promoted_employee = replace(
        employee,
        job_title=new_job_title,
        salary=new_salary,
        department=employee.department if new_department is None else new_department,
    )
    return [
        promoted_employee if record.employee_id == employee_id else record
        for record in records
    ]

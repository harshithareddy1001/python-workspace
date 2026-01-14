# salary_utils.py

total_working_days = 30
total_paid_leaves = 15

def get_bonus(designation, salary):
    if designation == "coder":
        return salary * 0.10
    elif designation == "designer":
        return salary * 0.15
    elif designation == "manager":
        return salary * 0.05
    else:
        return 0

def calc_salary(designation, salary, leaves):
    bonus = get_bonus(designation, salary)
    total_salary = salary + bonus

    unpaid = leaves - total_paid_leaves if leaves > total_paid_leaves else 0
    per_day = total_salary / total_working_days
    deduction = unpaid * per_day

    final_salary = total_salary - deduction
    return bonus, deduction, final_salary
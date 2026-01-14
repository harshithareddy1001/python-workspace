# main.py
import logging
logging.basicConfig(level=logging.INFO)
logging.info('program started')
from salary_utils import calc_salary

designation = input("enter designation (coder/designer/manager): ").strip().lower()
if designation not in ["coder", "designer", "manager"]:
    logging.warning("this is warning")
salary = float(input("enter base salary: "))
leaves = int(input("enter number of leaves taken: "))
# logging

bonus, deduction, final_salary = calc_salary(designation, salary, leaves)
logging.info("this is ending")

print("\n--- salary calculation ---")
print("bonus:", bonus)
print("deduction:", deduction)
print("final salary:", final_salary)
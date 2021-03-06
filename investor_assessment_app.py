# Import required libraries
from numpy import save
import questionary
import fire
from questionary.constants import NO, YES, YES_OR_NO
import csv
import sys
from sqlalchemy import column
# Define the clients general information
def general_info():
    full_name = questionary.text("What's your name?").ask()
    phone_number = questionary.text("What's your phone number?").ask()
    email_address = questionary.text("What's your email address?").ask()
    
    return full_name, phone_number, email_address
# Define the clients financial information
def financial_info():
    annual_income = questionary.text("What's your annual income?").ask()
    investing_experience = questionary.text("How many years of investing experience do you have?").ask()
    investment_amount = questionary.text("What is the amount you wish to start investing?").ask()
    annual_expenses = questionary.text("What are your annual expenses?").ask()
    income_stability = questionary.text(f"Is your source of income stable, YES or NO").ask(YES_OR_NO)
    
    annual_income = float(annual_income)
    investing_experience = int(investing_experience)
    investment_amount = float(investment_amount)
    annual_expenses = float(annual_expenses)
    income_stability = str(income_stability)
    
    
    return annual_income, investing_experience, investment_amount, annual_expenses, income_stability
# Define the clients financial goals
def financial_goals():
    risk_level = questionary.select(
        "What is your level of risk?",
        choices=["Low", "Moderate", "High"],
    ).ask()
    
    investment_strategy = questionary.checkbox(
        "What do you want to do with this investment, you may select more than one.",
        choices=["Income", "Growth", "Safety", "Speculative"],
    ).ask()
    
    investment_length = questionary.select(
        "How long do you plan to invest the money",
        choices=["1-4yrs", "5-9yrs", "10yrs+"],
    ).ask()
    return risk_level, investment_strategy, investment_length
def save_questionary_data():
    
    columns = (['full_name', 'phone_number', 'email_address', 'annual_income', 'investing_experience', 'investment_amount', 'annual_expenses', 'income_stability', 'risk_level', 'investment_strategy', 'investment_length'])
    
    client_data = []
    
    filename = "portfolio_creation_data.csv"
    
    stored_data = questionary.text("Would you like to save the data, YES or NO?").ask(YES_OR_NO)
    
    if YES:
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(columns)
            
            for row in client_data:
                csvwriter.writerow(row.values())
            
    if NO:
        sys.exit(f"Thank you for completing our survey!")
    return columns, client_data
def run():
   
   full_name, phone_number, email_address = general_info()
   annual_income, investing_experience, investment_amount, annual_expenses, income_stability = financial_info()
   risk_level, investment_strategy, investment_length = financial_goals()
   columns, client_data = save_questionary_data()
if __name__ == "__main__":
    fire.Fire(run)

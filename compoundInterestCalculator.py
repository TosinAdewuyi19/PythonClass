def calculate_compound_interest(principal, monthly_contribution, years, annual_rate, frequency):
    rate_per_period = annual_rate / 100 / frequency
    total_periods = years * frequency
    total_amount = principal

    for _ in range(total_periods):
        total_amount *= (1 + rate_per_period)

    return total_amount


def main():
    
    initial_investment = float(input("Enter initial investment: "))
    monthly_contribution = float(input("Enter monthly contribution: ") or 0)
    time_years = int(input("Enter length of time in years: "))
    annual_interest_rate = float(input("Enter estimated annual interest rate (in %): "))
    compound_frequency = int(input("Enter compound frequency (e.g., 1 for annually, 4 for quarterly, 12 for monthly, 365 for daily): "))

    total_amount = calculate_compound_interest(initial_investment, monthly_contribution, time_years, annual_interest_rate, compound_frequency)

    
    print(f"Total Amount: ${total_amount:.2f}")


if __name__ == "__main__":
    main()

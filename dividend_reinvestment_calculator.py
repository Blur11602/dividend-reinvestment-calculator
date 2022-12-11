# Dividend re-investment calculator
# Tested against https://www.tipranks.com/tools/dividend-calculator
import datetime

print("Welcome to the dividend re-investment calculator!")
print("This calculator will only work for annual dividend distributions.")

attempt = 1
loop = True
while loop == True:
	try:
		print(f"\nAttempt {attempt}")
		price = float(input("Enter the current price of the stock (in $):\n > "))
		dividend = float(input("Enter the current dividend yield (as a %):\n > "))
		shares = float(input("Enter the number of shares you own:\n > "))
		loop = False
	except Exception as e:
		attempt += 1
		loop = False if e == KeyboardInterrupt else print("Please enter a valid decimal or integer. Do not include symbols")

dividend /= 100

total = price * shares * dividend
initial_shares = shares
initial_dividend = dividend
initial_price = price
initial_total = shares * price

print(f"\nIf the price does not change at all you will receive roughly ${total:.2f} in dividends per year without reinvestment.")

cont = input("\nWould you like to reinvest your dividends each year? (y/n)\n > ")
if cont.lower() == "y":
	years = int(input("How many years of reinvesting would you like to calculate?\n > "))
	print(f"\nIf the price does not change at all...")
	print(f"""{datetime.datetime.now().year}:
	{shares:.2f} shares
	Worth ${(shares * price):.2f}
	${total:.2f} p.a.""")
	for year in range(1, years + 1):
		shares += total / price
		total = shares * price * dividend
		print(f"""{datetime.datetime.now().year + year}:
	{shares:.2f} shares
	Worth ${(shares * price):.2f}
	${total:.2f} p.a.

	{initial_shares:.2f} initial shares
	${initial_total:.2f} initial total
	${(shares * price) - initial_total:.2f} total profit""")
elif cont.lower() == "n":
	years = int(input("How many years would you like to calculate?\n > "))
	print(f"\nIf the price does not change at all...")
	total = shares * price * dividend * years
	print(f"""	{shares:.2f} shares
	Worth ${(shares * price):.2f}
	${total:.2f} total dividends""")

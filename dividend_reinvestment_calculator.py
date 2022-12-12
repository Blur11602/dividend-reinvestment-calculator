# Dividend re-investment calculator
# Tested against https://www.tipranks.com/tools/dividend-calculator
import datetime
import requests
import json

print("Welcome to the dividend re-investment calculator!")
print("This calculator will only work for annual dividend distributions.")

# function to get stock price from the ASX API
def get_stock_info(symbol):
	try:
		# make a GET request to the ASX API
		response = requests.get(f"https://www.asx.com.au/asx/1/share/{symbol}")

		# parse the response as JSON
		json_data = json.loads(response.text)

		data = [json_data["last_price"], json_data["annual_dividend_yield"]]

		# return the stock price
		return data
	except:
		# return 0 if an error occurred
		return 0

data = []

attempt = 1
loop = True
while loop == True:
	try:
		print(f"\nAttempt {attempt}")
		symbol = input("Enter the ASX stock symbol (only Australian stocks or securities are accepted):\n > ").upper()
		info = get_stock_info(symbol)
		price = float(info[0])
		dividend = float(info[1]) / 100
		shares = float(input("Enter the number of shares you own:\n > "))
		data.append([symbol, price, dividend, shares, price * shares * dividend])
		loop = False
	except Exception as e:
		attempt += 1
		loop = False if e == KeyboardInterrupt else print("Please enter a valid decimal or integer.")

initial_shares = data[0][3]
initial_dividend = data[0][2]
initial_price = data[0][1]
initial_total = initial_shares * initial_price

print(f"\nIf the price does not change at all you will receive roughly ${data[0][4]:.2f} in dividends per year without reinvestment.\n[{data[0][2] * 100}% of ${data[0][1]:.2f} per share]")

cont = input("\nWould you like to reinvest your dividends each year? (y/n)\n > ")
if cont.lower() == "y":
	years = int(input("How many years of reinvesting would you like to calculate?\n > "))
	print(f"\nIf the price does not change at all...")
	print(f"""{datetime.datetime.now().year}:
	{data[0][0]}: ${data[0][1]:.2f}
	{data[0][3]:.2f} shares
	Worth ${(data[0][3] * data[0][1]):.2f}
	${data[0][4]:.2f} in dividends p.a.""")
	for year in range(1, years + 1):
		data[0][3] += data[0][4] / data[0][1]
		data[0][4] = data[0][3] * data[0][1] * data[0][2]
		print(f"""{datetime.datetime.now().year + year}:
	{data[0][3]:.2f} shares
	Worth ${(data[0][3] * data[0][1]):.2f}
	${data[0][4]:.2f} in dividends p.a.

	{initial_shares:.2f} initial shares
	${initial_total:.2f} initial total
	${(data[0][3] * data[0][1]) - initial_total:.2f} total profit""")
elif cont.lower() == "n":
	years = int(input("How many years would you like to calculate?\n > "))
	print(f"\nIf the price does not change at all...")
	data[0][4] *= years
	print(f"""	{data[0][3]:.2f} shares
	Worth ${(data[0][3] * data[0][1]):.2f}
	${data[0][4]:.2f} total dividends""")

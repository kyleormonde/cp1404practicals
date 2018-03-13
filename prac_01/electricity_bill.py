# TODO: Electricity bill estimator
# TODO: INPUTS SHOULD BE:
# TODO: price per kWh in cents
# TODO: daily use in kWh
# TODO: number of days in the billing period

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator")
tariff = int(input("Tariff 11 or 31?: "))
daily_usage = float(input("Enter Daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

convert_to_dollars = daily_usage * billing_days

while 31 != tariff != 11:
    print("Invalid Tariff")
    tariff = int(input("Tariff 11 or 31?: "))

if tariff == 31:
    cost = TARIFF_31 * convert_to_dollars
else:
    cost = TARIFF_11 * convert_to_dollars

print("Estimated bill: ${:.2f}".format(cost))


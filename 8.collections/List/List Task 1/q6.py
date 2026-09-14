#6. Product Price Report
#Write a function price_report().
#•  Store product prices.
#•  Find the second highest price.
#•  Count products costing more than n1000.
#•  Display prices in descending order.

def price_report():
    print(prices)
    prices.sort(reverse=True)
    print(prices)
    print(prices[1])
    count=0
    for i in prices:
        if i>1000:
            count+=1
    print(count)
prices=[4000,7500,2000,5800,3400]
price_report()
#17. Product Prices
#Store product prices.
#bullet Display prices greater than n500.
#bullet Find the second highest price.

price=[500,600,100,800,1000]
for i in price:
    if i>500:
        print(i,end=" ")
price.sort()
print("\nSecond highest price is",price[-2])

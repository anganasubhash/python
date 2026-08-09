
#Input recharge amount.
#Display benefits: 199 → 1 GB/day | 299 → 1.5 GB/day 399 → 2 GB/day | Otherwise → Plan Not Available
recharge=int(input("Enter your recharge amount:"))
if recharge==199:
    print("1GB/day")
elif recharge==299:
    print("1.5GB/day")
elif recharge==399:
    print("2GB/day")
else:
    print("plan not available")
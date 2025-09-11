try:
    change=(float)(input("Please enter a dollar amount in cents and dollars\n"))
except ValueError:
    print("Please enter only an amount in cents and dollars.")
else:
    coin_count=0;
    change=(int)(change*100);
    quarters=(int)(change/25);
    coin_count+=quarters;
    change-=quarters*25;
    dimes=(int)(change/10);
    coin_count+=dimes;
    change-=dimes*10;
    nickels=(int)(change/5);
    coin_count+=nickels;
    change-=nickels*5;
    pennies=(int)(change/1);
    coin_count+=pennies;
    print("The minimum number of coins is", coin_count, "\n", quarters, "quarters\n", dimes, "dimes\n", nickels, "nickels\n", pennies, "pennies")
    if (coin_count<0):
        print("Are you trying to be silly or do you owe money")
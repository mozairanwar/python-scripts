# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts: list[list[int]]) -> int:
    mw = 0
    for i in accounts:
       w = sum(i)
       if w > mw:
           mw = w

    return mw

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(accounts))
-- https://leetcode.com/problems/bank-account-summary-ii/

SELECT name, SUM(All amount) AS balance
FROM Users
INNER JOIN Transactions
ON Users.account = Transactions.account
GROUP BY name
HAVING SUM(amount) > 10000
import time

def find_coins_greedy(coins, total):
	selection = {coin : 0 for coin in coins}

	current = 0
	while current < total:
		stale = True
		last = current
		for coin in coins:
			if current + coin <= total:
				selection[coin] += 1
				current += coin
				break
		if current == last: return None

	return {coin : count for coin, count in selection.items() if count > 0}

def find_min_coins(coins, total):
	selection = {coin : 0 for coin in coins}

	dp = [float('inf')] * (total + 1)
	dp[0] = 0
	coin_used = [0] * (total + 1)
	for i in range(1, total + 1):
		for coin in coins:
			if i >= coin and dp[i - coin] + 1 < dp[i]:
				dp[i] = dp[i - coin] + 1
				coin_used[i] = coin
	if dp[total] == float('inf'):
		return None

	amount = total
	while amount > 0:
		coin = coin_used[amount]
		selection[coin] += 1
		amount -= coin

	return {coin : count for coin, count in selection.items() if count > 0}

##############################

coins = [50, 25, 10, 5, 2, 1]

total = 113

res = find_coins_greedy(coins, total)
print(res)
res = find_min_coins(coins, total)
print(res)

start = time.time()
find_coins_greedy(coins, total)
find_coins_greedy_time = time.time() - start

start = time.time()
find_min_coins(coins, total)
find_min_coins_time = time.time() - start

find_coins_greedy_time *= 1000
find_min_coins_time *= 1000
print(f"Greedy calculation time: {find_coins_greedy_time} ms\nDynamic calculation time: {find_min_coins_time} ms")
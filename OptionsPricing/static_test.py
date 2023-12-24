from pricing import black_scholes

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

call_price = black_scholes(S, K, T, r, sigma, 'call')
put_price = black_scholes(S, K, T, r, sigma, 'put')

print("Call Option Price: ", call_price)
print("Put Option Price: ", put_price)
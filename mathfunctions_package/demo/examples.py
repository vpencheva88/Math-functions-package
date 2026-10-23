from mathfunctions_package import gcd, lcm, taylor_sin, birthday_prob, load_birthday_weights, simulate_birthdays_real

print(gcd(90, 18))          
print(lcm(2, 6))            
print(taylor_sin(0.89, 4))   
print(birthday_prob(18))  

weights = load_birthday_weights()
print(simulate_birthdays_real(39, weights))
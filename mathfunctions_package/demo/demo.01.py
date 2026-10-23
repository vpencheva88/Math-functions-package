import math
import matplotlib.pyplot as plt
import numpy as np


from mathfunctions_package import (gcd, lcm, primes, taylor_sin, birthday_prob,
                                   load_birthday_weights, simulate_birthdays_real,
                                   unique_birthdays_real)
print(gcd(48, 18))
print(lcm(4, 6))
print(primes(30)) #prints the prime numbers from 2 to 30

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

x = np.linspace(0, np.pi, 9)   # 9 points from 0 to pi
y = taylor_sin(x, 4)
print(y)

#to see how good the approximation is and show the error vs the exact number:
exact = np.sin(x)
error = np.abs(y - exact)

for xi, yi, ei in zip(x, y, error):
    print(f'x = {xi:.3f}   approx = {yi:.6f}   error = {ei:.2e}')




def plot_birthday_real() -> None:
    """Plot of chance of shared birthday for group of 1 to 80 people"""
    weights = load_birthday_weights()
    x = np.arange(1, 81)
    y1 = [birthday_prob(n) for n in x]                                   # exact formula
    y2 = [simulate_birthdays_real(n, weights, trials=2000) for n in x]   # real birth data

    fig, ax = plt.subplots(figsize=(8, 5))

    line = ax.plot(x, y1, label='exact')[0]
    line.set_linewidth(3)
    line.set_color('blue')

    dots = ax.plot(x, y2, label='Simulated with actual birth data')[0]
    dots.set_linestyle('none')      # no line joining the points
    dots.set_marker('o')        # draw a circle at each point
    dots.set_color('orange')
    dots.set_markersize(4)

    ax.set_title('The Birthday Problem with Real US births (2000-2014)')
    ax.set_xlabel('number of people')
    ax.set_ylabel('P(shared birthday)')
    ax.legend()
    ax.grid(True)
    plt.show()


def plot_taylor() -> None:
    """Taylor approximations of sin(x)"""
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    y1 = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 5))

    line = ax.plot(x, y1, label='sin(x)')[0]
    line.set_linewidth(3)
    line.set_color('black')

    for terms in range(1, 5):
        y = taylor_sin(x, terms)
        approx = ax.plot(x, y, label=f'{terms} terms')[0]
        approx.set_linestyle('--')

    ax.set_ylim(-2, 2)
    ax.set_title('Taylor Series for sin(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)
    plt.show()




#histogram for most popular birthday in the group
#Monte carlo simulation



#people with an unique birthday in a group of 100
def plot_unique_birthdays(group_size: int = 100) -> None:
    """Histogram of how many people have a birthday nobody else shares."""
    weights = load_birthday_weights()
    unique = unique_birthdays_real(group_size, weights, trials=10000)
    expected = group_size * np.sum(weights * (1 - weights) ** (group_size - 1))

    fig, ax = plt.subplots(figsize=(8, 5))

    bins = np.arange(unique.min() - 0.5, unique.max() + 1.5)
    ax.hist(unique, bins=bins, color='green', edgecolor='black',
            label='Monte Carlo simulation (real birth data)')

    mean_line = ax.axvline(np.mean(unique), label=f'simulated mean = {np.mean(unique):.2f}')
    mean_line.set_color('red')
    mean_line.set_linestyle('--')
    mean_line.set_linewidth(2)   #what actually happened in experiment

    theory_line = ax.axvline(expected, label=f'theory (all days equal) = {expected:.2f}')
    theory_line.set_color('black')
    theory_line.set_linestyle(':')
    theory_line.set_linewidth(2)  #prediction of what should happen

    ax.set_title(f'People With a Unique Birthday in a Group of {group_size}')
    ax.set_xlabel('number of people who share their birthday with nobody')
    ax.set_ylabel('number of trials')
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_birthday_real()
    plot_unique_birthdays()
    plot_taylor()
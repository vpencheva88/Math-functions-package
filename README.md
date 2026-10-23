## mathfunctions_package ##

'mathfunctions_package' is a small Python package of mathematical functions from my BSc Mathematics course. It covers three areas: 

-number theory: greatest common divisor, lowest common multiple and prime numbers
-calculus: a Taylor series approximation of sin(x)
-probability: the birthday problem

NumPy is used for fast calculations on arrays and for the Monte Carlo simulations. Matplotlib is used to plot the probabilities, the Taylor approximations and the histograms of simulated results.

The package includes a dataset of US births for every day from 2000 to 2014, published on Github. It is used to simulate the birthday problem with real birth rates instead of assuming every day is equally likely.




# Installation
From inside the 'mathkit' directory, install the package in editable mode:

```sh
python  pip install -e .
```

The required dependencies are specified in 'pyproject.toml' and will be installed automatically.

## Examples of use

The greatest common divisor and lowest common multiple of two whole numbers can be found using 'gcd' and 'lcm':

```python
from mathfunctions_package import gcd, lcm

print(gcd(90, 18))    # 18
print(lcm(2, 6))      # 6
```

The Taylor series approximation of sin(x) is calculated with 'taylor_sin', where the second argument is the number of terms used:

```python
from mathfunctions_package import taylor_sin

print(taylor_sin(0.89, 4))    # 0.77707...
```

'taylor_sin' also accepts a NumPy array, so many values can be approximated at once:

```python
import numpy as np

x = np.linspace(0, np.pi, 9)
print(taylor_sin(x, 4))
```

The exact probability that at least two people in a group share a birthday is given by 'birthday_prob':

```python
from mathfunctions_package import birthday_prob

print(birthday_prob(18))    # 0.3469...
print(birthday_prob(23))    # 0.5072...
```

The same probability can be estimated by simulation using the real birth data:

```python
from mathfunctions_package import load_birthday_weights, simulate_birthdays_real

weights = load_birthday_weights()
print(simulate_birthdays_real(23, weights))
```

## Error handling

The functions raise clear errors when they are given invalid input:

'TypeError' - 'gcd(5.7689,2)', lcm('12', 8), 'gcd' only accepts whole numbers and 'lcm' only accepts whole numbers, not text, respectively
| 'TypeError' | 'lcm(0, 2.5)' | the type check runs before the zero check, so decimals are always caught |
| 'ZeroDivisionError' | 'abs(0 * 0) // gcd(0, 0)' | gcd(0, 0) = 0, which is why 'lcm' returns 0 when either input is 0 |

The file also includes an example with the correct input, 'gcd(48, 18)' and 'lcm(4, 6)', showing that the 'except' block is skipped when no error occurs, while the 'finally' block always runs.


Examples of catching these errors with 'try', 'except' and 'finally' are in 'demo/errors_demo.py'.

## Demonstration

The complete demonstration, including all the graphs and histograms, can be run from the 'mathfunctions_package' directory using:

```sh
python demo/demo.01.py
```

The examples above can be run with:

```sh
python demo/examples.py       
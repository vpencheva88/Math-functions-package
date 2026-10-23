#Probability problem: birthday
#chance that everyone's birthday is different
import numpy as np
import math
from pathlib import Path

data_file = Path(__file__).parent / "data" / "dataset.csv"

def birthday_prob(n: int, days: int = 365) -> float:
    """Chance that at least 2 people share the same birthday."""
    if n > days:
        return 1.0
    p_all_diff = 1.0
    for k in range(n):
        p_all_diff *= (days - k) / days
    return 1 - p_all_diff




def load_birthday_weights() -> np.ndarray:
    """Probability of being born on each date of the year, from the real data.

    Returns 366 numbers (1 Jan ... 31 Dec, including 29 Feb) that add up to 1.
    """
    data = np.loadtxt(data_file, delimiter=',', skiprows=1, dtype=int)
    month = data[:, 1]
    day = data[:, 2]
    births = data[:, 4]

    totals = np.zeros((12, 31))   #grid: 12 months x 31 days
    for m, d, b in zip(month, day, births):
        totals[m - 1, d - 1] += b   #add that day's births to the right date

    totals = totals.flatten()       #12 x 31 grid -> one long list of 372
    totals = totals[totals > 0]     #remove dates that don't exist (e.g. 31 April) -> 366
    return totals / totals.sum()    #turn counts into probabilities that add up to 1

def load_births() -> np.ndarray:
    """Read the dataset into a NumPy array, one row per day.

    Columns: 0 = year, 1 = month, 2 = date_of_month, 3 = day_of_week, 4 = births
    """
    return np.loadtxt(data_file, delimiter=',', skiprows=1, dtype=int)


def simulate_birthdays_real(n: int, weights: np.ndarray, trials: int = 10000) -> float:
    """Chance of a shared birthday when birthdays follow the real data."""
    rng = np.random.default_rng()
    birthdays = rng.choice(len(weights), size=(trials, n), p=weights) #busy dates are picked more often
    sort_bdays = np.sort(birthdays, axis = 1)
    match_exists = np.any(sort_bdays[:, 1:] == sort_bdays[:, :-1], axis=1)
    return float(match_exists.mean())


def unique_birthdays_real(group_size: int, weights: np.ndarray,
                          trials: int = 10000) -> np.ndarray:
    """How many people have a birthday nobody else shares, using the real data."""
    rng = np.random.default_rng()
    results = []
    for _ in range(trials):
        birthdays = rng.choice(len(weights), size=group_size, p=weights)
        counts = np.bincount(birthdays, minlength=len(weights))
        results.append(np.sum(counts == 1))
    return np.array(results)


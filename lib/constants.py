import random
from scipy.stats import bernoulli, beta

DEFAULT_MEMORY = 50
DEFAULT_DISCOUNT_FACTOR = 0.99
DEFAULT_ALPHA = 30
DEFAULT_WARM_START_NUM_OBSERVATIONS = 5


RECORD_STATS_AT = [2000, 4000, 6000, 8000, 12000, 15000, 20000]

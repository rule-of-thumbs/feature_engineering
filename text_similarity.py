import fuzzywuzzy
from fuzzywuzzy import fuzz

# original repository: https://github.com/seatgeek/fuzzywuzzy
print(fuzzywuzzy.__version__)
print(fuzz.partial_ratio("this is a test", "this is a test!"))
print(fuzz.ratio("this is a test", "this is a test!"))
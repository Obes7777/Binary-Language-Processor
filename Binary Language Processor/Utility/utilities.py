#Justyn Veeck

#Add top-level folder to Python path to help handle file imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#Standard Imports
import math
import re
import sys
import os

#File Imports
from Data.stop_words import stop_words

#Blake verbally abuses me into doing things I dont like. Cuz he is Greedy and what I did first wasnt good enough
# FUNCTION DEFINITIONS

#Normalizes string
#Takes an input and filters out stop words from the current set
#Convert the list to a set for faster lookups
def remove_stop_words(text, stop_words=set(stop_words)):
  """
  Takes a string, removes the provided set of stop words, and returns a list
  of the remaining significant words.
  """
  # 1. Convert to lowercase and find all words (ignoring punctuation).
  # \b[a-zA-Z]+\b finds whole words consisting of only letters.
  words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

  # 2. Filter the list: include only words NOT in the stop_words set.
  significant_words = [word for word in words if word not in stop_words]

  return significant_words
#SYNTAX: 

#Sigmoid function for weighed sum outputs
#!!POSSIBLY WILL REQUIRE AN AVERAGE TO NORMALIZE OUTPUTS WITH MORE/LESS WORDS!!
def sigmoid(x):
  """
  Calculates the sigmoid of a given input x.
  The output is a value between 0 and 1.
  """
  try:
    return 1 / (1 + math.exp(-x))
  except OverflowError:
    # Handles extreme values
    return 1.0 if x < 0 else 0.0
#SYNTAX: 

#colored prints to enhance testing
#Currently supports red, green, and yellow
def print_colored(text, color, end='\n'):
  colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
  reset = '\x1b[0m'
  sys.stdout.write(colors.get(color, '') + text + reset + end)
#SYNTAX: 



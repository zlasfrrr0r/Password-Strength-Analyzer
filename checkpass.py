import numpy as np
import string
import os

def verdict_score(score):
  """
  verdict_score(): Returns a verdict string ('Strong.', 'Weak.', 'Medium.') given a score.
  """
  if score <= 2:
      return "Weak."
  elif score == 3:
      return "Medium."
  else:
      return "Strong."

def find_score(chars, length):
  """
  Determines the score (0-4) of a given password given char criteria
  Contains uppercase
  Contains lowercase
  Contains digits
  Length >= 8
  """
  has_upper = np.any(np.isin(chars, list(string.ascii_uppercase)))
  has_lower = np.any(np.isin(chars, list(string.ascii_lowercase)))
  has_digits = np.any(np.isin(chars, list(string.digits)))
  min_len = length >= 8
  return np.sum([has_upper, has_lower, has_digits, min_len]) # True => 1 and False => 0

def check_pass(password):
  """
  Determines password strength and returns its verdict 
  """
  password_length = len(password)
  password_chars = np.array(list(password))
  password_score = find_score(password_chars, password_length)
  return verdict_score(password_score)

# Load data from file containing most common passwords
filepath = os.path.join('data', 'common_passwords.csv')
passwords = np.genfromtxt(filepath, delimiter=',', dtype=str, skip_header=1)
passwords_subset = passwords[:1000,:1]
v_check_pass = np.vectorize(check_pass) # Vectorized Wrapper acts like func but takes array as input and apply pyfunc to each element
result = v_check_pass(passwords_subset)
print(result)

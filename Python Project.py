import re
#this program will take input of movie or tv show plots and scan them for certain words. If the words are found within the plot, the program will then print a trigger warning to the user. If none of these words are found, it will print that there are no trigger warnings.

#this function should ensure that the input is a valid string. If the input is not a string, it will throw an error and ask the user to input something valid
def plot(summary):
  if type(summary) != str:
    raise TypeError("Please input a plot summary")
  for element in plot:
    if 

#MadLib.py
#Name: Aaliyah
#Date: 08/31/2024
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  Noun1 = input("Enter a noun: Yogurt ")
  Noun2 = input ("Enter a noun: Jackie ")
  Noun3 = input ("Enter a noun: bike ")
  Noun4 = input ("Enter a noun: sarah")
  Noun5 = input ("Enter a noun: candy")
  Noun6 = input ("Enter a noun: store")
  #Print the story with the user supplied words.

  print ("I like to eat" + Noun1 + "with my mom" + Noun2 + "at the park")
  print ("I like to ride my" + Noun3 + "with my friend" + Noun4 + "all the time")
  print ("I love to eat" + Noun5 + "from the" + Noun6 + "each day")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

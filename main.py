
from platform import node
import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('data/US_Crime_Rates_1960_2014.csv')

crimerates_df = original_df.drop(columns=['Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft'])
crimerates_df.head()

# functions:

def showrawdata():
    print(original_df) 

def showcrimerates():
    print(crimerates_df)

def showgraph_yearandtotal():
      original_df.plot(
                    kind='line',
                    x='Year',
                    y='Total',
                    color='blue',
                    alpha=0.3,
                    title='Amount of crimes per year')
      plt.show()

def showgraph_popandtotal():
     crimerates_df.plot(
                    kind= 'line',
                    x='Population',
                    y='Total',
                    color='red',
                    alpha=0.3,
                    title='Amount of crime based on population')
     plt.show()

def user_options():
     global quit
     print("""
           Hi there, please choose an option from the following:

           1 - This will show the original dataset
           2 - This will show the updated Data Frame
           3 - This will show a graph of the year and the total amount of crime
           4 - This will show a graph of the population and the total amount of crime
           5 - Leave program

           """)
     try:
      choice = int(input('Please choose a number '))

      if choice == 1:
          showrawdata()
      elif choice == 2:
          showcrimerates()
      elif choice == 3:
          showgraph_yearandtotal()
      elif choice == 4:
          showgraph_popandtotal()
      elif choice == 5:
          quit = True
      else:
          print('Please try again ')
     except:
      print('Please enter a number ')     

while not quit:
    user_options()
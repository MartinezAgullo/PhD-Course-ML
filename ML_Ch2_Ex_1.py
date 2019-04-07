# Pablo Martinez Agullo
# ML Course - Exercise Chapter 2
# 07/04/2019


# Comparing the information of two different datasets

# We are comparing the databases of the OECD and IMF to check if there
# is a correlation. In the first case we are visualizing the "Better
# life index" while in the second the mean salary per year and person in
# each country.


import pandas as pd
import numpy as np
import matplotlib
import argparse


# Small parser to decide if we want to print the database
parser = argparse.ArgumentParser()
parser.add_argument("--prt", action="store_true", help="Prints the dabases")
parser.add_argument("--sts", action="store_true", help="Prints the stats")
parser.add_argument("--sort", action="store_true", help="Sort the countries of OECD list by GDP per capita")
args = parser.parse_args()


# Read the databases
#Gross domestic product per capita (IMF)
gdp_per_capita = pd.read_csv('IMF.txt', delimiter = ';', names = ['Country', 'GDP'])

#Better life index (OECD)
better_life_index = pd.read_csv('OECD.txt', delimiter = ';',names = ['Country', 'BLI'])


# Merge the two tables
#The function merge will keep only the countries that are in both tables (inner join)
merged_table = better_life_index.merge(gdp_per_capita) # merge() is a symetric function


# Subset division
# First division: Training dataset and Validation-Test dataset
index1 =np.random.choice(int(merged_table.Country.count()), int((merged_table.Country.count()+1)/2), False) 

#Create two new dataframes
Training_df = pd.DataFrame(columns = ['Country', 'BLI', 'GDP'])	#initialize
Aux_df = pd.DataFrame(columns = ['Country', 'BLI', 'GDP'])		#initialize
i = 0
while i < int(merged_table.Country.count()):
	if i in index1:
		Training_df = Training_df.append(merged_table.loc[i], ignore_index=True)
	else:
		Aux_df = Aux_df.append(merged_table.loc[i], ignore_index=True) # Aux_df creates Test_df and Validation_df
	i = i+1

# Second division: Validation dataset and Test dataset
#we repeat the previous procedure
index1 =np.random.choice(int(Aux_df.Country.count()), int(Aux_df.Country.count()/2), False) 
Validation_df = pd.DataFrame(columns = ['Country', 'BLI', 'GDP'])
Test_df = pd.DataFrame(columns = ['Country', 'BLI', 'GDP'])	
i = 0
while i < int(Aux_df.Country.count()):
	if i in index1:
		Validation_df = Validation_df.append(Aux_df.loc[i], ignore_index=True)
	else:
		Test_df = Test_df.append(Aux_df.loc[i], ignore_index=True)
	i = i+1



# Calculate the correlation
print("The correlation between the GDP and BLI has a correlation coefficient (r) = " + str(round(Training_df['BLI'].corr(Training_df['GDP']),5)))



#Extras
if args.prt or args.sts or args.sort:
	print("  -- Displaying aditional information --")
# Display the datasets
if args.prt:
	print("gdp_per_capita")
	print(gdp_per_capita)
	print("\n")
	print("better_life_index")
	print(better_life_index)
	print("\n")
	print("There are " + str(gdp_per_capita.Country.count())+" countries in the IMF list and "+str(better_life_index.Country.count())+" in the OECD list" + "\n")
	print("_________________")
	print(" - Training dataset - ")
	print(Training_df)
	print("\n"+" - Validation dataset - ")
	print(Validation_df)
	print("\n"+" - Test dataset - ")
	print(Test_df)
	print("_________________")
	

# Find mean, max, location
if args.sts:
	print("Average GDP per capita: " + str(round(gdp_per_capita.GDP.mean(),2)) + " USD")
	print("Average BLI: " + str(round(better_life_index.BLI.mean(), 3)))
	print("The country of IMF with higher GPD per capita is " +str(gdp_per_capita.loc[gdp_per_capita['GDP'].idxmax()]['Country'])+ ", with " +str(round(gdp_per_capita.GDP.max(),2))+ " USD")
	print("The country of OECD with higher BLI per capita is " +str(better_life_index.loc[better_life_index['BLI'].idxmax()]['Country'])+ ", with " +str(round(better_life_index.BLI.max(),2)))
	if merged_table.Country.count() == better_life_index.Country.count():
		print("The "+str(better_life_index.Country.count())+" countries in the OECD list are in the IMF list too")
	else:
		print("There are " + str(merged_table.Country.count()) + " countries that are in both lists.")

# Sort by GDP
if args.sort:
	merged_table = merged_table.sort_values(by = ['GDP'], ascending = False).reset_index(drop = True)
	print(merged_table)

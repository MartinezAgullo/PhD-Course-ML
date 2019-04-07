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
# The function merge will keep only the countries that are in both tables (inner join)
merged_table = better_life_index.merge(gdp_per_capita) # merge() is a symetric function





#Extras
# Display the datasets
if args.prt:
	print(gdp_per_capita)
	print("\n")
	print(better_life_index)
	print("\n")
	print("There are " + str(gdp_per_capita.Country.count())+" countries in the IMF list and "+str(better_life_index.Country.count())+" in the OECD list")

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

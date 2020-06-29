# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:59:59 2020

@author: Sayantan
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

from pylab import rcParams
# figure size in inches

import plotly.graph_objs as go
import plotly
plotly.offline.init_notebook_mode()


# Importing the dataset
dataset_obesity = pd.read_csv('obesity-cleaned.csv', index_col=0)
dataset_population = pd.read_csv('Country-population-data.csv')

dataset_population1 = dataset_population[["Country Name","2016"]]

countrymap = {'Afghanistan':'Afghanistan','Albania':'Albania','Algeria':'Algeria','Andorra':'Andorra','Angola':'Angola','Antigua and Barbuda':'Antigua and Barbuda','Argentina':'Argentina','Armenia':'Armenia','Australia':'Australia','Austria':'Austria','Azerbaijan':'Azerbaijan','Bahamas':'Bahamas','Bahrain':'Bahrain','Bangladesh':'Bangladesh','Barbados':'Barbados','Belarus':'Belarus','Belgium':'Belgium','Belize':'Belize','Benin':'Benin','Bhutan':'Bhutan','Bosnia and Herzegovina':'Bosnia and Herzegovina','Botswana':'Botswana','Brazil':'Brazil','Brunei Darussalam':'Brunei Darussalam','Bulgaria':'Bulgaria','Burkina Faso':'Burkina Faso','Burundi':'Burundi','Cabo Verde':'Cabo Verde','Cambodia':'Cambodia','Cameroon':'Cameroon','Canada':'Canada','Central African Republic':'Central African Republic','Chad':'Chad','Chile':'Chile','China':'China','Colombia':'Colombia','Comoros':'Comoros','Congo':'Congo','Congo, Dem. Rep.':'Democratic Republic of the Congo','Costa Rica':'Costa Rica','Croatia':'Croatia','Cuba':'Cuba','Cyprus':'Cyprus','Czech Republic':'Czechia','Denmark':'Denmark','Djibouti':'Djibouti','Dominica':'Dominica','Dominican Republic':'Dominican Republic','Ecuador':'Ecuador','Egypt':'Egypt','El Salvador':'El Salvador','Equatorial Guinea':'Equatorial Guinea','Eritrea':'Eritrea','Estonia':'Estonia','Eswatini':'Eswatini','Ethiopia':'Ethiopia','Fiji':'Fiji','Finland':'Finland','France':'France','Gabon':'Gabon','Gambia':'Gambia','Georgia':'Georgia','Germany':'Germany','Ghana':'Ghana','Greece':'Greece','Grenada':'Grenada','Guatemala':'Guatemala','Guinea':'Guinea','Guinea-Bissau':'Guinea-Bissau','Guyana':'Guyana','Haiti':'Haiti','Honduras':'Honduras','Hungary':'Hungary','Iceland':'Iceland','India':'India','Indonesia':'Indonesia','Iran, Islamic Rep.':'Iran (Islamic Republic of)','Iraq':'Iraq','Ireland':'Ireland','Israel':'Israel','Italy':'Italy','Jamaica':'Jamaica','Japan':'Japan','Jordan':'Jordan','Kazakhstan':'Kazakhstan','Kenya':'Kenya','Kiribati':'Kiribati','Korea, Dem. People’s Rep.':'Democratic Peoples Republic of Korea','Korea, Rep.':'Republic of Korea','Kuwait':'Kuwait','Lao PDR':'"Lao Peoples Democratic Republic"','Latvia':'Latvia','Lebanon':'Lebanon','Lesotho':'Lesotho','Liberia':'Liberia','Libya':'Libya','Lithuania':'Lithuania','Luxembourg':'Luxembourg','Madagascar':'Madagascar','Malawi':'Malawi','Malaysia':'Malaysia','Maldives':'Maldives','Mali':'Mali','Malta':'Malta','Marshall Islands':'Marshall Islands','Mauritania':'Mauritania','Mauritius':'Mauritius','Mexico':'Mexico','Micronesia, Fed. Sts.':'Micronesia (Federated States of)','Moldova':'Republic of Moldova','Monaco':'Monaco','Mongolia':'Mongolia','Montenegro':'Montenegro','Morocco':'Morocco','Mozambique':'Mozambique','Myanmar':'Myanmar','Namibia':'Namibia','Nauru':'Nauru','Nepal':'Nepal','Netherlands':'Netherlands','New Zealand':'New Zealand','Nicaragua':'Nicaragua','Niger':'Niger','Nigeria':'Nigeria','North Macedonia':'Republic of North Macedonia','Norway':'Norway','Oman':'Oman','Pakistan':'Pakistan','Palau':'Palau','Panama':'Panama','Papua New Guinea':'Papua New Guinea','Paraguay':'Paraguay','Peru':'Peru','Philippines':'Philippines','Poland':'Poland','Portugal':'Portugal','Qatar':'Qatar','Romania':'Romania','Russian Federation':'Russian Federation','Rwanda':'Rwanda','Samoa':'Samoa','San Marino':'San Marino','Sao Tome and Principe':'Sao Tome and Principe','Saudi Arabia':'Saudi Arabia','Senegal':'Senegal','Serbia':'Serbia','Seychelles':'Seychelles','Sierra Leone':'Sierra Leone','Singapore':'Singapore','Slovenia':'Slovenia','Solomon Islands':'Solomon Islands','Somalia':'Somalia','South Africa':'South Africa','South Sudan':'South Sudan','Spain':'Spain','Sri Lanka':'Sri Lanka','St. Kitts and Nevis':'Saint Kitts and Nevis','St. Lucia':'Saint Lucia','St. Vincent and the Grenadines':'Saint Vincent and the Grenadines','Sudan':'Sudan','Sudan':'Sudan (former)','Suriname':'Suriname','Sweden':'Sweden','Switzerland':'Switzerland','Syrian Arab Republic':'Syrian Arab Republic','Tajikistan':'Tajikistan','Tanzania':'United Republic of Tanzania','Thailand':'Thailand','Timor-Leste':'Timor-Leste','Togo':'Togo','Tonga':'Tonga','Trinidad and Tobago':'Trinidad and Tobago','Tunisia':'Tunisia','Turkey':'Turkey','Turkmenistan':'Turkmenistan','Tuvalu':'Tuvalu','Uganda':'Uganda','Ukraine':'Ukraine','United Arab Emirates':'United Arab Emirates','United Kingdom':'United Kingdom of Great Britain and Northern Ireland','United States':'United States of America','Uruguay':'Uruguay','Uzbekistan':'Uzbekistan','Vanuatu':'Vanuatu','Venezuela, RB':'Venezuela (Bolivarian Republic of)','Vietnam':'Viet Nam','Yemen':'Yemen','Zambia':'Zambia','Zimbabwe':'Zimbabwe'}
dataset_population2 = dataset_population1.copy()
dataset_population2['Country Name'] = dataset_population2['Country Name'].map(countrymap)
dataset_population3 = dataset_population2.rename(columns={"Country Name": "Country"})
dataset_population4 = dataset_population3.dropna()



X=dataset_obesity.Country.unique()
Y=dataset_obesity.Year.unique()
Z=dataset_obesity["Obesity (%)"].unique()

#Making the dataset usable 
dataset_obesity["Obesity"]= dataset_obesity["Obesity (%)"].apply(lambda x: (x.split(" ")[0]))
dataset_obesity2 = dataset_obesity[dataset_obesity["Obesity"] != "No"]
Z2=dataset_obesity2["Obesity"].unique()
dataset_obesity2["Obesity"] = dataset_obesity2["Obesity"].apply(lambda x: float(x))
Z3=dataset_obesity2["Obesity"].unique()
dataset_obesity3 = dataset_obesity2.drop("Obesity (%)",axis="columns")




# Plotting meaan obesity by year for all countries
rcParams['figure.figsize'] = 20,10
all_sexes = dataset_obesity3[dataset_obesity3["Sex"]=="Both sexes"].groupby("Year").Obesity.mean()
male = dataset_obesity3[dataset_obesity3["Sex"]=="Male"].groupby("Year").Obesity.mean()
female = dataset_obesity3[dataset_obesity3["Sex"]=="Female"].groupby("Year").Obesity.mean()
plt.plot(all_sexes,linestyle='solid',marker='o',label="Obesity% of both Sexes",  color = 'green')
plt.plot(male,linestyle='solid',marker='o',label="Obesity% of male", color = 'blue')
plt.plot(female,linestyle='solid',marker='o',label="Obesity% female", color = 'red')
plt.xlabel('Year', fontsize=20)
plt.ylabel('Obesity%', fontsize=20)
plt.title('Mean Obesity by Year', fontsize=20)
plt.style.use('fivethirtyeight')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('Obesity% of all countries.png', dpi=108)




# Potting graph of Obesity% of all countries in 2016 - Sorted by Obesity%

# Fitting the data
countries_both_o = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Both sexes")].groupby("Country").Obesity.sum().sort_values(ascending=False)
countries_male_o = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Male")].groupby("Country").Obesity.sum().sort_values(ascending=False)
countries_female_o = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Female")].groupby("Country").Obesity.sum().sort_values(ascending=False)

x = np.arange(len(countries_female_o))
width = 4
countries_o = countries_both_o.reset_index()
countries_o = countries_o.drop(columns="Obesity")
countries_o = countries_o.transpose()
countries_o.columns = countries_o.iloc[0]

fig, ax = plt.subplots()
rcParams['figure.figsize'] = 20,10
ax.bar((20*x),countries_both_o, width, label='Both')
ax.bar(((20*x)+4),countries_male_o, width, label='Male')
ax.bar(((20*x)+8),countries_female_o, width, label='Female')

# Add some text for labels, title and custom x-axis  tick labels, etc.
ax.set_ylabel('Obesity %')
ax.set_xlabel('Country')
ax.set_title('Obesity% of all countries in 2016 - Sorted by Obesity%')
ax.set_xticks((20*x)+1)
ax.set_xticklabels(countries_o)
plt.xticks(fontsize=3,rotation=90)
ax.legend()
plt.savefig('Obesity% of all countries in 2016 - Sorted by Obesity%.png', dpi=1080)




# Potting graph of Obesity% of all countries in 2016 - Sorted by Country Name

# Fitting the data
countries_both_n = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Both sexes")].groupby("Country").Obesity.sum()
countries_male_n = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Male")].groupby("Country").Obesity.sum()
countries_female_n = dataset_obesity3[(dataset_obesity3["Year"]==2016) & (dataset_obesity3["Sex"]=="Female")].groupby("Country").Obesity.sum()

x = np.arange(len(countries_female_n))
width = 4
countries = dataset_obesity3["Country"].unique()

fig, ax = plt.subplots()
rcParams['figure.figsize'] = 20,10
ax.bar((20*x),countries_both_n, width, label='Both')
ax.bar(((20*x)+4),countries_male_n, width, label='Male')
ax.bar(((20*x)+8),countries_female_n, width, label='Female')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Obesity %')
ax.set_xlabel('Country')
ax.set_title('Obesity% of all countries in 2016 - Sorted by Country Name')
ax.set_xticks((20*x)+1)
ax.set_xticklabels(countries)
plt.xticks(fontsize=3,rotation=90)
ax.legend()
plt.savefig('Obesity% of all countries in 2016 - Sorted by Country Name.png', dpi=1080)










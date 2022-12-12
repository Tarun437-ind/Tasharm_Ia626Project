# Tasharm_IA626Project

# Project Title: Classfication of Counties of state New York By Bio Diversity and Farmland 

# Reading CSV Files

We used total 2 csv files one for biodiversity and one for Farmland_Class  wehere County is the Common column
# Reading bio diversity data

import pandas as pd

import numpy as np

df= pd.read_csv(r"C:\Users\Admin\Downloads\Biodiversity_by_County_-_Distribution_of_Animals__Plants_and_Natural_Communities.csv")

df

output:
![This Is an Image](https://github.com/Tarun437-ind/Tasharm_Ia626Project/blob/main/df_bio.png)

# Description of columns 
 

County : Name of New York State County. In addition to New York’s 62 Counties, the dataset also includes separate entries for offshore open waters that are part of New York State but that are not within the jurisdiction of any county: Lake Ontario, Lake Erie, and Atlantic Ocean/Long Island Sound

Category : Category of the species or community: Animal, Plant, or Natural Community.

Taxonomic Group: For animals and plants, the taxonomic phylum, class, or order to which the species belongs.Groups are not always equivalent to a single taxonomic group, and they are given English names.For natural communities, group is the system to which the natural community belongs. Natural communities are grouped into seven systems:marine, tidal wetlands (estuarine), rivers and streams (riverine), lakes and ponds (lacustrine),freshwater nontidal wetlands (palustrine),uplands (terrestrial), and  subterranean (caves). 

Taxonomic Subgroup : For animals and plants, a lower level of taxonomic
group than the Taxonomic Group (above). The
subgroup is the taxonomic phylum, class, order,
or family to which the species belong. Subgroups
are not always equivalent to a single taxonomic
group, and they are given English names.For natural communities, subgroup is the
subsystem to which the natural community
belongs. Marine and tidal wetland systems are
divided into subtidal and intertidal subsystems.
The freshwater nontidal wetlands system is
divided into open mineral soil wetlands, forested
mineral soil wetlands, open peatlands, and
forested peatlands. The uplands system is divided
into open uplands, barrens and woodlands, and
forested uplands. The rivers and streams, lakes
and ponds, and subterranean systems each have
one subsystem

Scientific Name : For plants and animals, the scientific name used
in the database of the New York Natural Heritage
Program. Names are based on generally accepted
references, augmented by recent scientific
literature and expert opinion.

Common Name : For plants and animals, the common name is its
“plain English” name, as used in the database of
the New York Natural Heritage Program. Names
are based on generally accepted references,
augmented by recent scientific literature and
expert opinion.

Year Last Documented : The most recent year the species or community
type was observed in the given county, as
documented in the dataset’s source databases.A value of “2000 – 2005” indicates that the
species was most recently documented during
the second NYS Breeding Bird Atlas Project,
conducted from 2000 to 2005.
A value of “1990-1999” indicates that the species
was most recently documented during the NY
Amphibian and Reptile Atlas Project, conducted
from 1990 to 1999.
A value of “not available” indicates that the
species or community type has been recorded in
the given county, but no date is available.

NY Listing Status:For animals and plants, the legal protected status
under New York State Environmental
Conservation Law (ECL) and under New York State
regulations. The highest level of protection is
given to species listed by New York State as
Endangered or Threatened. Regulations regarding
animals are administered by NYS DEC’s Division of
Fish, Wildlife, and Marine Resources. Regulations
regarding plants are administered by NYS DEC’s
Division of Lands and Forests.


# selecting Particular columns by using df.loc Method
bio=df.loc[:,["County","Category","Taxonomic Group","Distribution Status"]]

bio

Output:

![This Is an Image](https://github.com/Tarun437-ind/Tasharm_Ia626Project/blob/main/bio.png)

# Removing the unecessary County rows for further analysis 

Out of 66 counties we will be using only 57 countie for merging our datasets for our Farmland class 

we will use .drop() method to remove rows 

bio.drop(bio.loc[bio['County']=='Bronx'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Atlantic Ocean and Long Island Sound'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Counties Unknown'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Lake Erie Open Waters'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Lake Ontario Open Waters'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='New York'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Queens'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Richmond'].index, inplace=True)
bio.drop(bio.loc[bio['County']=='Kings'].index, inplace=True)

# Reading  Farmland Class data

df2= pd.read_csv(r"C:\Users\Admin\Downloads\farmclass.csv")

df2

output:
![df2](https://user-images.githubusercontent.com/93997961/207168435-f4993a89-7d24-40f7-8b9b-34ac3f227369.png)

# Description Of Columns : 

	Area_symbol	: Contains the Area code with State symbol
 
 County : Names of the New York State counties available in tbis datasets 
 
 Map_unit_symbol	: It is an Varchar dtypes which contains the unit symbol of map address 
 
 Map_unit_Name : They are total 4725 types of unit names where it gives how the land is for a particular map address such as slopes with percent or water or landfills etc
 
 Farmland_Class: They are total 4 types of different Farmland class such as 'All areas are prime farmland', 'Not prime farmland','Farmland of statewide importance', 'Prime farmland if drained'
 
 # Renaming the rows of county by setting and resetting Index
 df2.set_index('County', inplace=True)
 
 We are changing the row values to merge with bio data frame so that we will be not facing any issue while merging the datsets as our county is the common among both datasets.
 
 df2.rename(index = {"Albany County, New York":"Albany", "Allegany County Area, New York":"Allegany",
       "Broome County, New York":"Broome", "Cattaraugus County, New York":"Cattaraugus",
       "Cayuga County, New York":"Cayuga", "Chautauqua County, New York":"Chautauqua",
       "Chemung County, New York":"Chemung", "Chenango County, New York":"Chenango",
       "Clinton County, New York":"Clinton", "Columbia County, New York":"Columbia",
       "Cortland County, New York":"Cortland", "Delaware County, New York":"Delaware",
       "Dutchess County, New York":"Dutchess", "Erie County, New York":"Erie",
       "Essex County, New York":"Essex",
       "Franklin County, New York, Northern Part":"Franklin",
       "Fulton County, New York":"Fulton", "Genesee County, New York":"Genesee",
       "Greene County, New York":"Greene", "Hamilton County, New York":"Hamilton",
       "Herkimer County, New York, Southern Part":"Herkmier",
       "Jefferson County, New York":"Jefferson",
       "Lewis County, New York, Middle Part":"Lewis",
       "Livingston County, New York":"Livingston", "Madison County, New York":"Madison",
        "Monroe County, New York":"Monroe",
       "Montgomery County, New York":"Montgomery", "Nassau County, New York":"Nassau",
       "Niagara County Area, New York":"Niagara", "Oneida County, New York":"Oneida",
       "Onondaga County, New York":"Onondaga", "Ontario County, New York":"Ontario",
       "Orange County, New York":"Orange", "Orleans County, New York":"Orleans",
       "Oswego County, New York":"Oswego", "Otsego County, New York":"Ostego",
       "Putnam County, New York":"Putnam", "Rensselaer County, New York":"Rensselaer",
       "Rockland County, New York":"Rockland", "Saratoga County, New York":"Saratoga",
       "Schenectady County, New York":"Schenectady", "Schoharie County, New York":"Schoharie",
       "Schuyler County, New York":"Schuyler", "Seneca County, New York":"Seneca",
       "St. Lawrence County, New York":"St. Lawrence", "Steuben County, New York":"Steuben",
       "Suffolk County, New York":"suffolk", "Sullivan County, New York":"Sullivan",
       "Tioga County, New York":"Tioga", "Tompkins County, New York":"Tompkins",
       "Ulster County, New York":"Ulster", "Warren County, New York":"Warren",
       "Washington County, New York":"Washington", "Wayne County, New York":"Wayne",
       "Westchester County, New York":"Westchester", "Wyoming County, New York":"Wyoming",
       "Yates County, New York":"Yates"},inplace = True)


df2
 
 Output:
 
 ![index](https://user-images.githubusercontent.com/93997961/207170720-a5894ff2-7bba-4022-a1d9-75bbb654968c.png)
 
 After Indexing and renaming the row values we will be dropping the counties which are to be removed and match with the bio dataframe 
 
 df2.reset_index('County',inplace=True)
 
 df2.drop(df2.loc[df2['County']=='Akwesasne Territory: St. Regis Mohawk Reservation'].index, inplace=True)
df2.drop(df2.loc[df2['County']=='Area Name'].index, inplace=True)
df2.drop(df2.loc[df2['County']=='Seneca Nation of Indians, New York'].index, inplace=True)

# Merging the Datsets by using pd.merge method 
final=pd.merge(bio,df2,how='inner',on='County')

final

Output:

![final](https://user-images.githubusercontent.com/93997961/207171252-8bcad7bd-52f8-409b-965d-5906a2ee76e2.png)

After merging the dataframes we get 2.4M rows of 54 counties and we get to know Essex has the vast farmland_class by doing some visualization on power BI 

# Data Visualization



Using Power BI as a visulaization tools we will doing some clustering visulaization of county,category,farmland_class,unit_acres by using coloumn graph,area graph,tree map,line anf plot graph,table with sum of unit acres with different farmland classs types

# Count of Farmland_Class by County and Category By using cluster coloumn chart
we can see here essex has the more values compared to other 53 counties

![BI1](https://user-images.githubusercontent.com/93997961/207174779-c3049e92-164a-43dd-8f25-1ff82fbfc028.png)


# Count of Farmland_Class by County and Category By using Area graph 

![BI2](https://user-images.githubusercontent.com/93997961/207175952-20c280aa-e129-4fe8-85e0-9bc47d8c4957.png)

# Count  of Farm_Class and sum of unit_Acres by counties By using line graph

![BI3](https://user-images.githubusercontent.com/93997961/207176621-ec20aa3c-ddb0-4aeb-ba2f-e7b416cc8c07.png)

# County of category by Farmland_Class and County
![BI4](https://user-images.githubusercontent.com/93997961/207179674-834a6c31-9a2a-40b1-a221-916a610f28a6.png)

# Count of county by Farmland_Class and unit_Acres
![BI5](https://user-images.githubusercontent.com/93997961/207180484-ace79cdf-74f4-4ff4-9624-e492737b4fda.png)

# Creating Table of county covering 4 types of farmland and calculating sum of unit_Acres 
This is not an entire table but it gives glance how data looks and sum of unit_Acres is about 9 billons covering 4 types of farmlands and 54 counties

![BI6](https://user-images.githubusercontent.com/93997961/207180807-8ac6bcb8-1d60-40fb-bd94-c3a12e3e5670.png)

# sum of unit acres and count of farmland_class by county using line chart
![BI7](https://user-images.githubusercontent.com/93997961/207181685-cf87b843-4dcf-4ca2-937c-e65de8a26e04.png)

# Count of farmland class by diving total of farmland class using tree map 
By using all the 2.43M we see how the value is spreaded amoung 4 different types of farmland

![BI8](https://user-images.githubusercontent.com/93997961/207182432-6a448118-f3b3-4590-a231-7c06146496b0.png)

# Conclusion
After doing data analysis by using Power BI we can see that there is a difference between Farmland_class and unit_Acres among counties when we are counting the values for farmland_class of particular county ESSEX has the highest value and St.Lawerence has second but when we are counting the unit_Acres St.lawerence has the highest acres covered with category same goes for Broome and schenactady for the least value between Farmland_class and unit_Acres.













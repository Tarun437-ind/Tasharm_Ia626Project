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
![This Is an Image]()



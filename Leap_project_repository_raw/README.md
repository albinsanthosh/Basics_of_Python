# Leap-Project

Getting the contributors  (Commits also similar)
1. Authentication : Personal tokens in the url itself.
2. Limited Access (only 30 items per fetch): a) Using a loop b) Page number c) per_page items 
3. Condition: Until all the data is read until the final page is fetched.
4. Printing the length to see the number of items - Contributors.
5. Converting to Dataframe.
6. Concatinating the dataframe with a global empty dataframe till all the data is stored.
7. Exporting the dataframe to contributors.xlsx 

Getting the Contibutor's companies
0. Creating a dictionary to store the companies.
1. Importing the contributors.xlsx to dataframe.
2. Getting the organization_url column out of dataframe and looping.
3. Going through each contributor's organization_url and requesting the api.
4. Some contributor's organization is empty so adding them to Misc element.
5. Other's whose organization is there, are also added as organization as new element or if it exists in the dictionary then its inceamented.



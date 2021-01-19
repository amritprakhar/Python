#pip install covid
from covid import Covid
covid = Covid()
name = input("Enter the name of the country : ")
cases = covid.get_status_by_country_name(name.upper())
for x in cases:
    print(x , ":", cases[x])

# Script to extract ASX Codes from ASX website 
#   How:  Download csv from ASX website 
#         Remove columns not required and rename required columns
#         Write finalised data to a new csv file (ASXCompanyInformation.csv)


#Imports
import requests as r
import pandas as pd


# Get stock data from ASX website
url="https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?"
response = r.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the response to a local CSV file
    with open(r"C:\WorkingASX\TickersFromWebsite\tickers.csv", "wb") as f:
       f.write(response.content)
    print("CSV file downloaded successfully")
else:
    print("Failed to download CSV file. Status code:", response.status_code)

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\WorkingASX\TickersFromWebsite\tickers.csv")

# Drop columns that are not required, rename kept columns
df.drop(['Market Cap'],axis=1,inplace=True)
df.columns = ['ASXCode','CompanyName','Industry','ListingDate']

# Write output to csv
df.to_csv(r'C:\WorkingASX\Tickers\ASXCompanyInformation.csv',index=False)
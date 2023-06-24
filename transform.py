import json
import mysql.connector
import re

def extract_decimal(string):
    pattern = r'\d+\.\d+'  # Match the pattern of a decimal number
    match = re.search(pattern, string)
    
    if match:
        return str(match.group())  # Convert the matched decimal to a float
    else:
        return ""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="costofliving"
)
mycursor = mydb.cursor()

with open("results.json", "r") as file:
    jsonData = json.load(file, strict=False)

countries = ['Cambodia', 'Paraguay', 'Kazakhstan', 'Portugal', 'Syria', 'Bahamas', 'Greece', 'Latvia', 'Mongolia', 'Iran', 'Morocco', 'Panama', 'Guatemala', 'Iraq', 'Chile', 'Nepal', 'Argentina', 'Seychelles', 'Tanzania', 'Ukraine', 'Belize', 'Ghana', 'Zambia', 'Bahrain', 'India', 'Canada', 'Maldives', 'Turkey', 'Belgium', 'Finland', 'Taiwan', 'North Macedonia', 'South Africa', 'Bermuda', 'Georgia', 'Jamaica', 'Peru', 'Germany', 'Yemen', 'Puerto Rico', 'Fiji', 'Hong Kong', 'United States', 'Somalia', 'Ivory Coast', 'Thailand', 'Libya', 'Costa Rica', 'Sweden', 'Vietnam', 'Poland', 'Jordan', 'Kuwait', 'Bulgaria', 'Nigeria', 'Tunisia', 'Croatia', 'Uruguay', 'Sri Lanka', 'United Kingdom', 'United Arab Emirates', 'Kenya', 'Switzerland', 'Palestine', 'Spain', 'Lebanon', 'Cuba', 'Venezuela', 'Azerbaijan', 'Czech Republic', 'Guernsey', 'Israel', 'Australia', 'Estonia', 'Myanmar', 'Cameroon', 'Cyprus', 'Malaysia', 'Iceland', 'Oman', 'Bosnia And Herzegovina', 'Armenia', 'South Korea', 'Austria', 'El Salvador', 'Luxembourg', 'Brazil', 'Algeria', 'Jersey', 'Slovenia', 'Ecuador', 'Kosovo (Disputed Territory)', 'Colombia', 'Hungary', 'Japan', 'Moldova', 'Belarus', 'Mauritius', 'Trinidad And Tobago', 'Albania', 'New Zealand', 'Senegal', 'Italy', 'Honduras', 'Ethiopia', 'Afghanistan', 'Singapore', 'Egypt', 'Bolivia', 'Malta', 'Russia', 'Saudi Arabia', 'Netherlands', 'Pakistan', 'Ireland', 'Qatar', 'China', 'Slovakia', 'France', 'Lithuania', 'Serbia', 'Romania', 'Philippines', 'Rwanda', 'Uzbekistan', 'Bangladesh', 'Barbados', 'Nicaragua', 'Norway', 'Botswana', 'Macao', 'Denmark', 'Dominican Republic', 'Zimbabwe', 'Mexico', 'Uganda', 'Suriname', 'Montenegro', 'Indonesia']

countriesId = 1
citiesId = 1
for country in countries:
    if False == (country in jsonData and jsonData[country] is not None and 'child' in jsonData[country] and jsonData[country]['child'] is not None):
        continue
    restaurantsAVG = []
    restaurantsRange = []
    for elem in (jsonData[country]['\n\nRestaurants']):
        if elem == None:
                continue
        if(elem[1] == ' ?' or elem[1] == ''):
            restaurantsAVG.append('NULL')
        else:
            restaurantsAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            restaurantsRange.append('NULL')
        else:
            restaurantsRange.append(elem[2].replace(",", "").strip())
    marketsAVG = []
    marketsRange = []
    for elem in (jsonData[country]['\n\nMarkets']):
        if(elem[1] == ' ?' or elem[1] == ''):
            marketsAVG.append('NULL')
        else:
            marketsAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            marketsRange.append('NULL')
        else:
            marketsRange.append(elem[2].replace(",", "").strip())
    transportationAVG = []
    transportationRange = []
    for elem in (jsonData[country]['\n\nTransportation']):
        if(elem[1] == ' ?' or elem[1] == ''):
            transportationAVG.append('NULL')
        else:
            transportationAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            transportationRange.append('NULL')
        else:
            transportationRange.append(elem[2].replace(",", "").strip())
    
    utilitiesAVG = []
    utilitiesRange = []
    for elem in (jsonData[country]['\n\nUtilities (Monthly)']):
        if(elem[1] == ' ?' or elem[1] == ''):
            utilitiesAVG.append('NULL')
        else:
            utilitiesAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            utilitiesRange.append('NULL')
        else:
            utilitiesRange.append(elem[2].replace(",", "").strip())
   
    leisureAVG = []
    leisureRange = []
    for elem in (jsonData[country]['\n\nSports And Leisure']):
        if(elem[1] == ' ?' or elem[1] == ''):
            leisureAVG.append('NULL')
        else:
            leisureAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
           leisureRange.append('NULL')
        else:
            leisureRange.append(elem[2].replace(",", "").strip())
   
    childcareAVG = []
    childcareRange = []
    for elem in (jsonData[country]['\n\nChildcare']):
        if(elem[1] == ' ?' or elem[1] == ''):
            childcareAVG.append('NULL')
        else:
            childcareAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            childcareRange.append('NULL')
        else:
            childcareRange.append(elem[2].replace(",", "").strip())

    clothingAVG = []
    clothingRange = []
    for elem in (jsonData[country]['\n\nClothing And Shoes']):
        if(elem[1] == ' ?' or elem[1] == ''):
            clothingAVG.append('NULL')
        else:
            clothingAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            clothingRange.append('NULL')
        else:
            clothingRange.append(elem[2].replace(",", "").strip())

    rentAVG = []
    rentRange = []
    for elem in (jsonData[country]['\n\nRent Per Month']):
        if(elem[1] == ' ?' or elem[1] == ''):
            rentAVG.append('NULL')
        else:
            rentAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            rentRange.append('NULL')
        else:
            rentRange.append(elem[2].replace(",", "").strip())

    buyHouseAVG = []
    buyHouseRange = []
    for elem in (jsonData[country]['\n\nBuy Apartment Price']):
        if(elem[1] == ' ?' or elem[1] == ''):
            buyHouseAVG.append('NULL')
        else:
            buyHouseAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            buyHouseRange.append('NULL')
        else:
            buyHouseRange.append(elem[2].replace(",", "").strip())

    financingAVG = []
    financingRange = []
    for elem in (jsonData[country]['\n\nSalaries And Financing']):
        if(elem[1] == ' ?' or elem[1] == ''):
            financingAVG.append('NULL')
        else:
            financingAVG.append(extract_decimal(elem[1]))
        if(elem[2] == ' ?' or elem[2] == ''):
            financingRange.append('NULL')
        else:
            financingRange.append(elem[2].replace(",", "").strip())
    
    ''' 
    if((country == "Indonesia" and city == "Yogyakarta") or True): 
        print(restaurantsAVG[0])
        print(restaurantsRange[0])
        print(marketsAVG[0])
        print(marketsRange[0])
        print(transportationAVG[0])
        print(transportationRange[0])
        print(utilitiesAVG[0])
        print(utilitiesRange[0])
        print(leisureAVG[0])
        print(leisureRange[0])
        print(childcareAVG[0])
        print(childcareRange[0])
        print(clothingAVG[0])
        print(clothingRange[0])
        print(rentAVG[0])
        print(rentRange[0])
        print(buyHouseAVG[0])
        print(buyHouseRange[0])
        print(financingAVG[0])
        print(financingRange[0])
    '''

    sql = "INSERT INTO CostOfLivingCountries VALUES (" + str(countriesId) + ", \"" + country + "\", " + restaurantsAVG[0] + ", \"" + restaurantsRange[0] + "\", " + restaurantsAVG[1] + ", \"" + restaurantsRange[1] + "\", " + restaurantsAVG[2] + ", \"" + restaurantsRange[2] + "\", " + restaurantsAVG[3] + ", \"" + restaurantsRange[3] + "\", " + restaurantsAVG[4] + ", \"" + restaurantsRange[4] + "\", " + restaurantsAVG[5] + ", \"" + restaurantsRange[5] + "\", " + restaurantsAVG[6] + ", \"" + restaurantsRange[6] + "\", " + restaurantsAVG[7] + ", \"" + restaurantsRange[7] + "\", " + marketsAVG[0] + ", \"" + marketsRange[0] + "\", " + marketsAVG[1] + ", \"" + marketsRange[1] + "\", " + marketsAVG[2] + ", \"" + marketsRange[2] + "\", " + marketsAVG[3] + ", \"" + marketsRange[3] + "\", " + marketsAVG[4] + ", \"" + marketsRange[4] + "\", " + marketsAVG[5] + ", \"" + marketsRange[5] + "\", " + marketsAVG[6] + ", \"" + marketsRange[6] + "\", " + marketsAVG[7] + ", \"" + marketsRange[7] + "\", " + marketsAVG[8] + ", \"" + marketsRange[8] + "\", " + marketsAVG[9] + ", \"" + marketsRange[9] + "\", " + marketsAVG[10] + ", \"" + marketsRange[10] + "\", " + marketsAVG[11] + ", \"" + marketsRange[11] + "\", " + marketsAVG[12] + ", \"" + marketsRange[12] + "\", " + marketsAVG[13] + ", \"" + marketsRange[13] + "\", " + marketsAVG[14] + ", \"" + marketsRange[14] + "\", " + marketsAVG[15] + ", \"" + marketsRange[15] + "\", " + marketsAVG[16] + ", \"" + marketsRange[16] + "\", " + marketsAVG[17] + ", \"" + marketsRange[17] + "\", " + marketsAVG[18] + ", \"" + marketsRange[18] + "\", " + transportationAVG[0] + ", \"" + transportationRange[0] + "\", " + transportationAVG[1] + ", \"" + transportationRange[1] + "\", " + transportationAVG[2] + ", \"" + transportationRange[2] + "\", " + transportationAVG[3] + ", \"" + transportationRange[3] + "\", " + transportationAVG[4] + ", \"" + transportationRange[4] + "\", " + transportationAVG[5] + ", \"" + transportationRange[5] + "\", " + transportationAVG[6] + ", \"" + transportationRange[6] + "\", " + transportationAVG[7] + ", \"" + transportationRange[7] + "\", " + utilitiesAVG[0] + ", \"" + utilitiesRange[0] + "\", " + utilitiesAVG[1] + ", \"" + utilitiesRange[1] + "\", " + utilitiesAVG[2] + ", \"" + utilitiesRange[2] + "\", " + leisureAVG[0] + ", \"" + leisureRange[0] + "\", "  + leisureAVG[1] + ", \"" + leisureRange[1] + "\", " + leisureAVG[2] + ", \"" + leisureRange[2] + "\", " + childcareAVG[0] + ", \"" + childcareRange[0] + "\", " + childcareAVG[1] + ", \"" + childcareRange[1] + "\", " + clothingAVG[0] + ", \"" + clothingRange[0] + "\", " + clothingAVG[1] + ", \"" + clothingRange[1] + "\", " + clothingAVG[2] + ", \"" + clothingRange[2] + "\", " + clothingAVG[3] + ", \"" + clothingRange[3] + "\", " + rentAVG[0] + ", \"" + rentRange[0] + "\", " + rentAVG[1] + ", \"" + rentRange[1] + "\", " + rentAVG[2] + ", \"" + rentRange[2] + "\", " + rentAVG[3] + ", \"" + rentRange[3] + "\", "  + buyHouseAVG[0] + ", \"" + buyHouseRange[0] + "\", " + buyHouseAVG[1] + ", \"" + buyHouseRange[1] + "\", " + financingAVG[0] + ", \"" + financingRange[0] + "\", " + financingAVG[1] + ", \"" + financingRange[1] + "\");"
    countriesId += 1
    '''
    text_file = open("sample.txt", "w")
    n = text_file.write(sql)
    text_file.close()
    '''
    mycursor.execute(sql)

    cities = []
    for city in jsonData[country]['child']:
        if False == (city in jsonData[country]['child'] and jsonData[country]['child'][city] is not None):
            continue
        elif(city == '' or city == 'none'):
            continue
        cities.append(city)
        restaurantsAVG = []
        restaurantsRange = []
        for elem in (jsonData[country]['child'][city]['\n\nRestaurants']):
            if elem == None:
                continue
            if(elem[1] == ' ?' or elem[1] == ''):
                restaurantsAVG.append('NULL')
            else:
                restaurantsAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                restaurantsRange.append('NULL')
            else:
                restaurantsRange.append(elem[2].replace(",", "").strip())
        marketsAVG = []
        marketsRange = []
        for elem in (jsonData[country]['child'][city]['\n\nMarkets']):
            if(elem[1] == ' ?' or elem[1] == ''):
                marketsAVG.append('NULL')
            else:
                marketsAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                marketsRange.append('NULL')
            else:
                marketsRange.append(elem[2].replace(",", "").strip())
        transportationAVG = []
        transportationRange = []
        for elem in (jsonData[country]['child'][city]['\n\nTransportation']):
            if(elem[1] == ' ?' or elem[1] == ''):
                transportationAVG.append('NULL')
            else:
                transportationAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                transportationRange.append('NULL')
            else:
                transportationRange.append(elem[2].replace(",", "").strip())
        
        utilitiesAVG = []
        utilitiesRange = []
        for elem in (jsonData[country]['child'][city]['\n\nUtilities (Monthly)']):
            if(elem[1] == ' ?' or elem[1] == ''):
                utilitiesAVG.append('NULL')
            else:
                utilitiesAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                utilitiesRange.append('NULL')
            else:
                utilitiesRange.append(elem[2].replace(",", "").strip())
       
        leisureAVG = []
        leisureRange = []
        for elem in (jsonData[country]['child'][city]['\n\nSports And Leisure']):
            if(elem[1] == ' ?' or elem[1] == ''):
                leisureAVG.append('NULL')
            else:
                leisureAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
               leisureRange.append('NULL')
            else:
                leisureRange.append(elem[2].replace(",", "").strip())
       
        childcareAVG = []
        childcareRange = []
        for elem in (jsonData[country]['child'][city]['\n\nChildcare']):
            if(elem[1] == ' ?' or elem[1] == ''):
                childcareAVG.append('NULL')
            else:
                childcareAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                childcareRange.append('NULL')
            else:
                childcareRange.append(elem[2].replace(",", "").strip())

        clothingAVG = []
        clothingRange = []
        for elem in (jsonData[country]['child'][city]['\n\nClothing And Shoes']):
            if(elem[1] == ' ?' or elem[1] == ''):
                clothingAVG.append('NULL')
            else:
                clothingAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                clothingRange.append('NULL')
            else:
                clothingRange.append(elem[2].replace(",", "").strip())

        rentAVG = []
        rentRange = []
        for elem in (jsonData[country]['child'][city]['\n\nRent Per Month']):
            if(elem[1] == ' ?' or elem[1] == ''):
                rentAVG.append('NULL')
            else:
                rentAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                rentRange.append('NULL')
            else:
                rentRange.append(elem[2].replace(",", "").strip())

        buyHouseAVG = []
        buyHouseRange = []
        for elem in (jsonData[country]['child'][city]['\n\nBuy Apartment Price']):
            if(elem[1] == ' ?' or elem[1] == ''):
                buyHouseAVG.append('NULL')
            else:
                buyHouseAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                buyHouseRange.append('NULL')
            else:
                buyHouseRange.append(elem[2].replace(",", "").strip())

        financingAVG = []
        financingRange = []
        for elem in (jsonData[country]['child'][city]['\n\nSalaries And Financing']):
            if(elem[1] == ' ?' or elem[1] == ''):
                financingAVG.append('NULL')
            else:
                financingAVG.append(extract_decimal(elem[1]))
            if(elem[2] == ' ?' or elem[2] == ''):
                financingRange.append('NULL')
            else:
                financingRange.append(elem[2].replace(",", "").strip())
        
        ''' 
        if((country == "Indonesia" and city == "Yogyakarta") or True): 
            print(restaurantsAVG[0])
            print(restaurantsRange[0])
            print(marketsAVG[0])
            print(marketsRange[0])
            print(transportationAVG[0])
            print(transportationRange[0])
            print(utilitiesAVG[0])
            print(utilitiesRange[0])
            print(leisureAVG[0])
            print(leisureRange[0])
            print(childcareAVG[0])
            print(childcareRange[0])
            print(clothingAVG[0])
            print(clothingRange[0])
            print(rentAVG[0])
            print(rentRange[0])
            print(buyHouseAVG[0])
            print(buyHouseRange[0])
            print(financingAVG[0])
            print(financingRange[0])
        '''
        sql = "INSERT INTO CostOfLivingCities VALUES (" + str(citiesId) + ", \"" + country + "\", \"" + city + "\", " + restaurantsAVG[0] + ", \"" + restaurantsRange[0] + "\", " + restaurantsAVG[1] + ", \"" + restaurantsRange[1] + "\", " + restaurantsAVG[2] + ", \"" + restaurantsRange[2] + "\", " + restaurantsAVG[3] + ", \"" + restaurantsRange[3] + "\", " + restaurantsAVG[4] + ", \"" + restaurantsRange[4] + "\", " + restaurantsAVG[5] + ", \"" + restaurantsRange[5] + "\", " + restaurantsAVG[6] + ", \"" + restaurantsRange[6] + "\", " + restaurantsAVG[7] + ", \"" + restaurantsRange[7] + "\", " + marketsAVG[0] + ", \"" + marketsRange[0] + "\", " + marketsAVG[1] + ", \"" + marketsRange[1] + "\", " + marketsAVG[2] + ", \"" + marketsRange[2] + "\", " + marketsAVG[3] + ", \"" + marketsRange[3] + "\", " + marketsAVG[4] + ", \"" + marketsRange[4] + "\", " + marketsAVG[5] + ", \"" + marketsRange[5] + "\", " + marketsAVG[6] + ", \"" + marketsRange[6] + "\", " + marketsAVG[7] + ", \"" + marketsRange[7] + "\", " + marketsAVG[8] + ", \"" + marketsRange[8] + "\", " + marketsAVG[9] + ", \"" + marketsRange[9] + "\", " + marketsAVG[10] + ", \"" + marketsRange[10] + "\", " + marketsAVG[11] + ", \"" + marketsRange[11] + "\", " + marketsAVG[12] + ", \"" + marketsRange[12] + "\", " + marketsAVG[13] + ", \"" + marketsRange[13] + "\", " + marketsAVG[14] + ", \"" + marketsRange[14] + "\", " + marketsAVG[15] + ", \"" + marketsRange[15] + "\", " + marketsAVG[16] + ", \"" + marketsRange[16] + "\", " + marketsAVG[17] + ", \"" + marketsRange[17] + "\", " + marketsAVG[18] + ", \"" + marketsRange[18] + "\", " + transportationAVG[0] + ", \"" + transportationRange[0] + "\", " + transportationAVG[1] + ", \"" + transportationRange[1] + "\", " + transportationAVG[2] + ", \"" + transportationRange[2] + "\", " + transportationAVG[3] + ", \"" + transportationRange[3] + "\", " + transportationAVG[4] + ", \"" + transportationRange[4] + "\", " + transportationAVG[5] + ", \"" + transportationRange[5] + "\", " + transportationAVG[6] + ", \"" + transportationRange[6] + "\", " + transportationAVG[7] + ", \"" + transportationRange[7] + "\", " + utilitiesAVG[0] + ", \"" + utilitiesRange[0] + "\", " + utilitiesAVG[1] + ", \"" + utilitiesRange[1] + "\", " + utilitiesAVG[2] + ", \"" + utilitiesRange[2] + "\", " + leisureAVG[0] + ", \"" + leisureRange[0] + "\", "  + leisureAVG[1] + ", \"" + leisureRange[1] + "\", " + leisureAVG[2] + ", \"" + leisureRange[2] + "\", " + childcareAVG[0] + ", \"" + childcareRange[0] + "\", " + childcareAVG[1] + ", \"" + childcareRange[1] + "\", " + clothingAVG[0] + ", \"" + clothingRange[0] + "\", " + clothingAVG[1] + ", \"" + clothingRange[1] + "\", " + clothingAVG[2] + ", \"" + clothingRange[2] + "\", " + clothingAVG[3] + ", \"" + clothingRange[3] + "\", " + rentAVG[0] + ", \"" + rentRange[0] + "\", " + rentAVG[1] + ", \"" + rentRange[1] + "\", " + rentAVG[2] + ", \"" + rentRange[2] + "\", " + rentAVG[3] + ", \"" + rentRange[3] + "\", "  + buyHouseAVG[0] + ", \"" + buyHouseRange[0] + "\", " + buyHouseAVG[1] + ", \"" + buyHouseRange[1] + "\", " + financingAVG[0] + ", \"" + financingRange[0] + "\", " + financingAVG[1] + ", \"" + financingRange[1] + "\");"
        #print("INSERT INTO CostOfLivingCities VALUES (" + str(citiesId) + ", \"" + country + "\", \"" + city + "\", " + restaurantsAVG[0] + ", \"" + restaurantsRange[0] + "\", " + restaurantsAVG[1] + ", \"" + restaurantsRange[1] + "\", " + restaurantsAVG[2] + ", \"" + restaurantsRange[2] + "\", " + restaurantsAVG[3] + ", \"" + restaurantsRange[3] + "\", " + restaurantsAVG[4] + ", \"" + restaurantsRange[4] + "\", " + restaurantsAVG[5] + ", \"" + restaurantsRange[5] + "\", " + restaurantsAVG[6] + ", \"" + restaurantsRange[6] + "\", " + restaurantsAVG[7] + ", \"" + restaurantsRange[7] + "\", " + marketsAVG[0] + ", \"" + marketsRange[0] + "\", " + marketsAVG[1] + ", \"" + marketsRange[1] + "\", " + marketsAVG[2] + ", \"" + marketsRange[2] + "\", " + marketsAVG[3] + ", \"" + marketsRange[3] + "\", " + marketsAVG[4] + ", \"" + marketsRange[4] + "\", " + marketsAVG[5] + ", \"" + marketsRange[5] + "\", " + marketsAVG[6] + ", \"" + marketsRange[6] + "\", " + marketsAVG[7] + ", \"" + marketsRange[7] + "\", " + marketsAVG[8] + ", \"" + marketsRange[8] + "\", " + marketsAVG[9] + ", \"" + marketsRange[9] + "\", " + marketsAVG[10] + ", \"" + marketsRange[10] + "\", " + marketsAVG[11] + ", \"" + marketsRange[11] + "\", " + marketsAVG[12] + ", \"" + marketsRange[12] + "\", " + marketsAVG[13] + ", \"" + marketsRange[13] + "\", " + marketsAVG[14] + ", \"" + marketsRange[14] + "\", " + marketsAVG[15] + ", \"" + marketsRange[15] + "\", " + marketsAVG[16] + ", \"" + marketsRange[16] + "\", " + marketsAVG[17] + ", \"" + marketsRange[17] + "\", " + marketsAVG[18] + ", \"" + marketsRange[18] + "\", " + transportationAVG[0] + ", \"" + transportationRange[0] + "\", " + transportationAVG[1] + ", \"" + transportationRange[1] + "\", " + transportationAVG[2] + ", \"" + transportationRange[2] + "\", " + transportationAVG[3] + ", \"" + transportationRange[3] + "\", " + transportationAVG[4] + ", \"" + transportationRange[4] + "\", " + transportationAVG[5] + ", \"" + transportationRange[5] + "\", " + transportationAVG[6] + ", \"" + transportationRange[6] + "\", " + transportationAVG[7] + ", \"" + transportationRange[7] + "\", " + utilitiesAVG[0] + ", \"" + utilitiesRange[0] + "\", " + utilitiesAVG[1] + ", \"" + utilitiesRange[1] + "\", " + utilitiesAVG[2] + ", \"" + utilitiesRange[2] + "\", " + leisureAVG[0] + ", \"" + leisureRange[0] + "\", "  + leisureAVG[1] + ", \"" + leisureRange[1] + "\", " + leisureAVG[2] + ", \"" + leisureRange[2] + "\", " + childcareAVG[0] + ", \"" + childcareRange[0] + "\", " + childcareAVG[1] + ", \"" + childcareRange[1] + "\", " + clothingAVG[0] + ", \"" + clothingRange[0] + "\", " + clothingAVG[1] + ", \"" + clothingRange[1] + "\", " + clothingAVG[2] + ", \"" + clothingRange[2] + "\", " + clothingAVG[3] + ", \"" + clothingRange[3] + "\", " + rentAVG[0] + ", \"" + rentRange[0] + "\", " + rentAVG[1] + ", \"" + rentRange[1] + "\", " + rentAVG[2] + ", \"" + rentRange[2] + "\", " + rentAVG[3] + ", \"" + rentRange[3] + "\", "  + buyHouseAVG[0] + ", \"" + buyHouseRange[0] + "\", " + buyHouseAVG[1] + ", \"" + buyHouseRange[1] + "\", " + financingAVG[0] + ", \"" + financingRange[0] + "\", " + financingAVG[1] + ", \"" + financingRange[1] + "\");")    
        citiesId += 1
        '''
        text_file = open("sample.txt", "w")
        n = text_file.write(sql)
        text_file.close()
        '''
        mycursor.execute(sql)
mydb.commit()
print("records inserted.")



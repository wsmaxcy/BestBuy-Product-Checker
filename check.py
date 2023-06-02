from urllib.request import urlopen
from urllib.error import HTTPError
import simplejson
from time import sleep
from datetime import datetime
import webbrowser
from playsound import playsound
import sys

period = .5
sku = [6521430,6521518,6524435,6524436,6522679,6522334,6521517,6522371] # Product SKU's go here
names = []
apiKey = 'xxxxxxxxxxxxxxxx' # API Key goes here
global count 
count = 0
num = len(sku)

# Checks if product is in stock
def check(apiKey,sku):
    
    # Checks if product is in stock
    try:
        response = urlopen('https://api.bestbuy.com/v1/products/'+str(sku)+'.json?show=onlineAvailability&apiKey='+str(apiKey))
    
    # Makes sure we don't put in too many requests too fast
    except HTTPError as err:
        if err.code == 403:
            print("⚠️ We're overloading the servers, gonna wait "+ str(period) +" seconds on this one literally from " + datetime.now().strftime("%H:%M:%S"))
            sleep(period)
            return False
            
    return(simplejson.loads(response.read())['onlineAvailability'])

# Main function
def main():

    count = 0
    
    # Gets product names
    for card in sku:
        response = urlopen('https://api.bestbuy.com/v1/products/'+str(card)+'.json?show=name&apiKey='+apiKey)
        name = simplejson.loads(response.read())['name']
        print(name + " added to list of cards checking")
        names.append(name)
        sleep(period+2)
    
    # Checks if product is in stock    
    status = check(apiKey,sku[count])
    
    # If product is not in stock, wait and check again
    while status == False:
        sleep(period)
        print("❌ "+str(count)+" checks complete. Product not found. Time complete: " + datetime.now().strftime("%H:%M:%S")+ " | Card # "+ str((count%num)+1) + " - " + str(names[(count%num)]))
        count = count + 1
        status = check(apiKey,sku[count%num])
    
    print("✅ PRODUCT FOUND IN STOCK")
    webbrowser.open("https://www.bestbuy.com/site/searchpage.jsp?st=" + names[(count%num)] + "&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys")
    playsound(sys.path[0]+"\\alarm.wav")
		
main()

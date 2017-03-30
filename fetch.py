import urllib.request
from bs4 import BeautifulSoup
from itertools import cycle

resp = urllib.request.urlopen('https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India')
html = resp.read()
soup = BeautifulSoup(html, 'html.parser')
result = {}
states = {'AP':  'Andhra Pradesh',
          'AS':  'Assam',
          'BR':  'Bihar',
          'CH':  'Chennai',
          'DL':  'Delhi',
          'GJ':  'Gujarat',
          'HP':  'Himachal Pradesh',
          'HR':  'Haryana',
          'JK':  'Jammu and Kashmir',
          'KL':  'Kerala',
          'KA':  'Karnataka',
          'KO':  'Kolkata',
          'MH':  'Maharashtra & Goa',
          'MP':  'Madhya Pradesh',
          'MU':  'Mumbai',
          'NE':  'North East',
          'OR':  'Orissa',
          'PB':  'Punjab',
          'RJ':  'Rajasthan',
          'TN':  'Tamil Nadu',
          'UE':  'UP (East)',
          'UW':  'UP (West)',
          'WB':  'West Bengal'}

def main():
    tables = soup.findAll('table', attrs={'class':'wikitable'})
    for table in tables:
        res = str(table.find('caption'))
        if 'Mobile Telephone' in res:
            for row in table.findAll('tr'):
                col = row.findAll('td')
                data = [ele.text.strip() for ele in col]
                if data:
                    make_dict(data)

    print (result)
    #number = int(input('Enter phone number: '))
    #phone_check(number)


def make_dict(data):
    i = 0
    prev = False
    while i <  len(data):
        try:
            number = int(data[i])
            prev = True
        except ValueError:
            if len(data[i]) == 0:
                i = i + 1
                continue
            else:
                if prev == False:
                    result[number] = data[i]

                else:
                    try:
                        if i+1 < len(data) and int(data[i+1]):
                            result[number] = data[i]
                    except ValueError:
                        prev = False

        i = i + 1

def phone_check(number):
    prefix = int(str(number)[0:-6])

    code = result[prefix]
    print (states[code])

if __name__ == '__main__':
    main()

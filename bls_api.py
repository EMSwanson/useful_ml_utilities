import requests
import json
import prettytable
headers = {'Content-type': 'application/json'}
#LNS14000000 is the national unemployment rate - really simple monthly grab from public API
#'IPUHN44_45_L000000000' is retail trade labor productivity
#Have to look at the top picks to find series IDs to use.

#List of series for unemployment
data = json.dumps({"seriesid": ['LNS14000000','SUUR0000SA0','IPUHN44_45_L000000000'],"startyear":"2015", "endyear":"2020"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
        x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
        seriesId = series['seriesID']
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = item['value']
            footnotes=""
            for footnote in item['footnotes']:
                if footnote:
                    footnotes = footnotes + footnote['text'] + ','
                if 'M01' <= period <= 'M12':
                    x.add_row([seriesId,year,period,value,footnotes[0:-1]])
        output = open(seriesId + '.txt','w')
        output.write (x.get_string())
        output.close()
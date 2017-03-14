#!/usr/bin/env python
from betfair import Betfair
import sys

print "HugeHard Test Script"
client = Betfair('fxmlhjiDhNghfmLP', 'C:/Users/Cong/Desktop/betfair/keys/shang.pem')
client.login('shang1982@gmail.com', 'wabjtam@123')
print 'login successful'

sys.exit 

from betfair.models import MarketFilter
event_types = client.list_event_types(
    MarketFilter(text_query='basketball')
)

#print (len(event_types))
#print (event_types[0].event_type.name)
football_event_type = event_types[0]

competitions = client.list_competitions()
for comp in competitions:
    a = comp['competition']
    if a.name == u'NBA Matches':
        id_NBA = a.id
    


events = client.list_events(MarketFilter(competition_ids=[id_NBA]))
f  = open('C:/Users/Cong/Desktop/betfair/log_basketball.txt', 'w')
for eventResult in events:
    e = eventResult.event
    c = eventResult.market_count
#    print "id:" + e.id + ", name=" + e.name + ", market_count:" + str(c)
    markets = client.list_market_catalogue(MarketFilter(event_ids=[e.id]))
    for m in markets:
        f.write( m.market_id + ' ' + m.market_name + ' '+ ' ' + str(e['id'])+ ' ' + str(e['name']) + '\n')
        f.write( '***' + str(e['country_code']) + '...\n')

f.close()
client.logout()
#print 'logout successful'
#
#for comp in competitions:
#    a = comp['competition']
#    b = comp['market_count']
#    c = comp['competition_region']
##    f.write(str(a.name) + ' '+  str(a.id)  + '  '+ str(b) +  ' ' + str(c))
##    print a.name, a.id ,b, c
#    
#    f.close()
    



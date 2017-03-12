#!/usr/bin/env python
from betfair import Betfair

print "HugeHard Test Script"
client = Betfair('fxmlhjiDhNghfmLP', 'certs/betfair.pem')
client.login('shang1982@gmail.com', 'wabjtam@123')
print 'login successful'


from betfair.models import MarketFilter
event_types = client.list_event_types(
    MarketFilter(text_query='soccer')
)

print (len(event_types))
print (event_types[0].event_type.name)
football_event_type = event_types[0]

events = client.list_events(MarketFilter(event_type_ids=[football_event_type.event_type.id]))

for eventResult in events:
    e = eventResult.event
    c = eventResult.market_count
    print "id:" + e.id + ", name=" + e.name + ", market_count:" + str(c)
    markets = client.list_market_catalogue(MarketFilter(event_ids=[e.id]))
    for m in markets:
        print "    - market: ", m.market_id, m.market_name

#markets = client.list_market_catalogue(
#    MarketFilter(event_type_ids=[football_event_type.event_type.id])
#)
#for m in markets:
#    print m.market_name

client.logout()
print 'logout successful'

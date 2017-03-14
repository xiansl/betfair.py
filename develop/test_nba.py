#!/usr/bin/env python
from betfair import Betfair
import sys

print "HugeHard Test Script"
client = Betfair('fxmlhjiDhNghfmLP', '/home/shang/git/betfair.py/certs/betfair.pem')
client.login('shang1982@gmail.com', 'wabjtam@123')
print 'login successful'

from betfair.models import MarketFilter, PriceProjection
event_types = client.list_event_types(
    MarketFilter(text_query='basketball')
    #MarketFilter(text_query='soccer')
)

competition_types = client.list_competitions(
    MarketFilter(text_query='NBA matches')
    #MarketFilter(text_query='English Premier League')
)

#print (len(event_types))
#print (event_types[0].event_type.name)
basketball_event_type = event_types[0]

#print (len(competition_types))
#print (competition_types[0].competition.name)
basketball_competition = competition_types[0].competition

events = client.list_events(MarketFilter(event_type_ids=[basketball_event_type.event_type.id], competition_ids=[basketball_competition.id]))

from betfair.constants import OrderProjection, MatchProjection, PriceData

for eventResult in events:
    e = eventResult.event
    c = eventResult.market_count
    print "id:" + e.id + ", name=" + e.name + ", market_count:" + str(c)
    markets = client.list_market_catalogue(MarketFilter(event_ids=[e.id]))
    for m in markets:
        print "    - market: id=" + m.market_id + ", name=" + m.market_name
        marketbooks = client.list_market_book(market_ids=[m.market_id], price_projection=PriceProjection(price_data=PriceData.EX_BEST_OFFERS), order_projection=OrderProjection.EXECUTABLE, match_projection=MatchProjection.ROLLED_UP_BY_PRICE)
        for mb in marketbooks:
            print "    - - marketbook: id=" + mb.market_id + ", status=" + mb.status + ", delay=" + str(mb.is_market_data_delayed) + ", bet_delay=" + str(mb.bet_delay) + ", total_matched=" + str(mb.total_matched) + ", total_available=" + str(mb.total_available)
            for r in mb.runners:
                print "    - - - runner: id=" + str(r.selection_id) + ", handicap=" + str(r.handicap) + ", status=" + str(r.status) + ", lastprice=" + str(r.last_price_traded) + ", total_matched=" + str(r.total_matched)
                sp = r.sp
                ex = r.ex
                orders = r.orders
                matches = r.matches
                if sp:
                    print "    - - - - startprice(near=" + str(sp.near_price) + ", far=" + str(sp.far_price) + ", actual=" + str(sp.actual_SP) + ")"
                if ex:
                    for back in ex.available_to_back: 
                        print "    - - - - exchangeprice(back): price=" + str(back.price) + ", size=" + str(back.size)
                    for lay in ex.available_to_lay: 
                        print "    - - - - exchangeprice(lay): price=" + str(lay.price) + ", size=" + str(lay.size)
                    for vol in ex.traded_volume: 
                        print "    - - - - exchangeprice(traded volumn): price=" + str(vol.price) + ", size=" + str(vol.size)
                if orders:
                    for o in r.orders:
                        print "    - - - - order: betid=" + o.bet_id + ", ordertype=" + str(o.order_type)
                if matches:
                    for match in r.matches:
                        print"    - - - - match: matchid=" + match.match_id
                
    #break 

#markets = client.list_market_catalogue(
#    MarketFilter(event_type_ids=[football_event_type.event_type.id])
#)
#for m in markets:
#    print m.market_name

client.logout()
print 'logout successful'


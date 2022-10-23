# wig20_ann_modeling
Modeling of changes of the WIG20 stock market index using artificial neural networks.

### Description of Dependent Variables and Trading Strategy
Two dependent variables are considered:
1. Log-return of the close value of the WIG20 index between trading day *D+1* and *D+2*
2. Binary variable indicating whether the close value of the WIG20 index on trading
day *D+2* is higher than the close value of the index on trading day *D+1*

The reason why the dependent variables are defined this way is that in case of 
finding a good model the following trading strategy can be implemented:
* generate model prediction on trading day *D*
* if the close value of the index is expected to go up (respectively: down) from 
trading day *D+1* to trading day *D+2*, then buy (resp.: sell) a futures contract 
during the [post-closing session phase (pl: *dogrywka*)](https://www.infor.pl/prawo/encyklopedia-prawa/f/290674,Fixing-i-dogrywka-w-sesji-gieldowej.html)
on trading day *D+1* and close the position during the post-closing session phase on trading day *D+2*.

Also, cf. [description of phases of trading session](https://www.elearnmarkets.com/school/units/stock-market-terminologies/types-of-market-sessions-and-market-timings).

### Shortcomings of the Trading Strategy Considered
It is assumed that there is always enough liquidity during the post closing 
session phase to open/close the position. This does not have to be the case in real life! 

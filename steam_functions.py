import json
import os
import pickle
import time
from time import sleep

import requests

from helpfiles.filemanagment import getaccountfilespath, getprojectdirectorypath
from helpfiles.crypto import decryptfile, encryptfile
from helpfiles.logger import log
from myapifiles.item import Item
from mysteampymodified.client import SteamClient
from mysteampymodified.utils import GameOptions

coefdrop48h168h=1.05
coefdrop24h72h=1.04
coefdrop12h36h=1.03
coefboost48h72h=1.03
coefboost48h168h=1.04
coefboost24h48h=1.02
coefboost3h24h=1.01
sellhistcountcoefforgraphicdrop=None
sellhistcountcoefforgraphicboost=None
sellhistcountbadcoef=None
sellhistcountgoodcoef=None
steamclientfilenameforrelogin=None
steamclient=None


def loginsteam(steamclientfilename='steamclient.pkl',accountfilename='account.json',steamguardfilename='steamguard.json'):
    log('steamf: loginsteam')
    projectdirectorypath=getprojectdirectorypath()
    accountfilespath=projectdirectorypath+getaccountfilespath()
    global steamclientfilenameforrelogin
    steamclientfilenameforrelogin=steamclientfilename
    steamclientfilename=accountfilespath+steamclientfilename
    accountfilename=accountfilespath+accountfilename
    steamguardfilename=accountfilespath+steamguardfilename
    global steamclient
    if os.path.isfile(steamclientfilename):
        steamclient=decryptfile(steamclientfilename)
    if steamclient.issessionalive():
        return
    account=decryptfile(accountfilename)
    steamguard=decryptfile(steamguardfilename)
    steamclient=SteamClient(account['apikey'])
    steamclient.login(account['steamlogin'],account['steampassword'],steamguard)
    with open(steamclientfilename,'wb') as f:
        pickle.dump(steamclient,f)
        encryptfile(steamclientfilename)


def reloginsteam(accountfilename='account.json',steamguardfilename='steamguard.json'):
    log('steamf: reloginsteam')
    while True:
        try:
            loginsteam(steamclientfilenameforrelogin,accountfilename,steamguardfilename)
            break
        except Exception as err:
            log('steamf: проблема в функции reloginsteam')
            log(err)
        sleep(5)


def initializecoefsforgetitemsactualprice():
    global sellhistcountcoefforgraphicdrop
    global sellhistcountcoefforgraphicboost
    global sellhistcountbadcoef
    global sellhistcountgoodcoef
    curtime=time.gmtime()
    if curtime.tm_wday==1:
        sellhistcountcoefforgraphicdrop=0.02
        sellhistcountcoefforgraphicboost=0.02
        sellhistcountbadcoef=0.04
        sellhistcountgoodcoef=0.06
        return
    if curtime.tm_wday==2:
        sellhistcountcoefforgraphicdrop=0.01
        sellhistcountcoefforgraphicboost=0.01
        sellhistcountbadcoef=0.03
        sellhistcountgoodcoef=0.05
        return
    if curtime.tm_wday==3:
        if curtime.tm_hour<8:
            sellhistcountcoefforgraphicdrop=0.01
            sellhistcountcoefforgraphicboost=0.01
            sellhistcountbadcoef=0.03
            sellhistcountgoodcoef=0.05
            return
    sellhistcountcoefforgraphicdrop=0.03
    sellhistcountcoefforgraphicboost=0.03
    sellhistcountbadcoef=0.05
    sellhistcountgoodcoef=0.07


def getsteampriceforeveryiteminlist(itemslistforsteam,coef):
    log('steamf: getsteampriceforeveryiteminlist')
    initializecoefsforgetitemsactualprice()
    for item in itemslistforsteam:
        while True:
            try:
                itemprice=getitemactualprice(item)
                break
            except Exception as err:
                log('проблема в функции getsteampriceforeveryiteminlist')
                log(err)
        item.steamprice=itemprice
        item.tmprice=round(itemprice*0.87/coef*10)
        log(f'{item.getname()}: {item.steamprice} : {item.tmprice}\n')


def getitemactualprice(item):
    log('steamf: getitemactualprice')
    history=getpricehistory(item.getname())
    histogram=getitemhistogram(item)
    pricegraphic=round(getitempricegraphic(history),2)
    pricehistogram=round(getitempricehistogram(history,histogram),2)
    maxbuyorder=float(histogram['highest_buy_order'])/100
    minsellorder=float(histogram['lowest_sell_order'])/100
    if pricegraphic==pricehistogram:
        return int(round(pricegraphic*100))
    count24_12histogram,count12_6histogram,count6_3histogram,count3_0histogram=getcountofpriceorhigherinhistory24_12_6_3(history,pricehistogram-0.005)
    if count24_12histogram==0 and count12_6histogram==0 and count6_3histogram==0 and count3_0histogram==0:
        return int(round(max(pricegraphic,minsellorder)*100))
    if checkgraphicdrop(history) or checkgraphicboost(history):
        if pricegraphic<pricehistogram:
            return int(round(max(pricegraphic,minsellorder)*100))
        return int(round(pricehistogram*100))
    else:
        if pricegraphic>pricehistogram and pricehistogram<=maxbuyorder:
            return int(round(max(pricegraphic,minsellorder)*100))

        if pricehistogram>pricegraphic and pricegraphic<=maxbuyorder:
            return int(round(pricehistogram*100))
    if pricegraphic/pricehistogram>=1.07 or pricehistogram/pricegraphic>=1.07:
        return int(round(min(pricehistogram,max(pricegraphic,minsellorder))*100))
    else:
        if pricegraphic>pricehistogram:
            return int(round(max(pricegraphic,minsellorder)*100))
        return int(round(pricehistogram*100))


def getpricehistory(itemname,gameoption=GameOptions.CS):
    log('steamf: getpricehistory')
    while True:
        try:
            tmp=steamclient.market.fetch_price_history(itemname,game=gameoption)
            if tmp["success"]:
                return tmp["prices"]
        except Exception as err:
            log('steamf: проблема в функции getpricehistory')
            log(err)
            if not steamclient.is_session_alive():
                reloginsteam()

            sleep(1)


def getitemhistogram(item):
    log('steamf: getitemhistogram')
    while True:
        try:
            histogram=steamclient.market.get_item_histogram(item)
            if histogram['success']:
                return histogram
        except Exception as err:
            log('steamf: проблема в функции getitemhistogram')
            log(err)
            if not steamclient.is_session_alive():
                reloginsteam()
            sleep(2)


def getitempricegraphic(prices):
    log('steamf: getitempricegraphic')
    if checkgraphicdrop(prices):
        price2h=calculateavgpriceandmore(prices,2)
        return price2h
    price7days=calculateavgpriceandmore(prices,168,72)
    price3days=calculateavgpriceandmore(prices,72,48)
    price2days=calculateavgpriceandmore(prices,48)
    if price2days/price3days>=coefboost48h72h and price2days/price7days>=coefboost48h168h:
        price1day=calculateavgpriceandmore(prices,24)
        if price1day/price2days>=coefboost24h48h:
            price3hrs=calculateavgpriceandmore(prices,3)
            if price3hrs/price1day>=coefboost3h24h:
                return price3hrs
            else:
                price2hrs=calculateavgpriceandmore(prices,2)
                return price2hrs
        else:
            price12h=calculateavgpriceandmore(prices,12)
            return price12h
    return price2days


def calculateavgpriceandmore(prices,time2,time1=0):
    log('steamf: calculateavgpriceandmore')
    res=0
    count=0
    for i in range(time1,time2):
        res+=prices[-1-i][1]*int(prices[-1-i][2])
        count+=int(prices[-1-i][2])
    priceaverage=res/count
    res=0
    count=0
    highestpricecoef=1.2
    for i in range(time1,time2):
        if priceaverage<=prices[-1-i][1]<=priceaverage*highestpricecoef:
            res+=prices[-1-i][1]*int(prices[-1-i][2])
            count+=int(prices[-1-i][2])
    if count>0:
        return res/count
    return priceaverage


def checkgraphicdrop(prices):
    log('steamf: checkgraphicdrop')
    price1=calculateavgpriceandmore(prices,168,48)
    price2=calculateavgpriceandmore(prices,48)
    if price1/price2>=coefdrop48h168h:
        return True
    price1=calculateavgpriceandmore(prices,72,24)
    price2=calculateavgpriceandmore(prices,24)
    if price1/price2>=coefdrop24h72h:
        return True
    price1=calculateavgpriceandmore(prices,36,12)
    price2=calculateavgpriceandmore(prices,12)
    if price1/price2>=coefdrop12h36h:
        return True
    return False


def checkgraphicboost(prices):
    log('steamf: checkgraphicboost')
    price7days=calculateavgpriceandmore(prices,168,72)
    price3days=calculateavgpriceandmore(prices,72,48)
    price2days=calculateavgpriceandmore(prices,48)
    if price2days/price3days>=coefboost48h72h and price2days/price7days>=coefboost48h168h:
        return True
    return False


def getitempricehistogram(prices,histogram):
    log('steamf: getitempricehistogram')
    sellorderslist=getitemsellorderslist(histogram)
    itemsellcountforweek=calculateitemsellcount(prices,168)
    itemsellcountforday=int(itemsellcountforweek/7)
    if checkgraphicdrop(prices):
        sellcountfordropcoef=int(sellhistcountcoefforgraphicdrop*itemsellcountforday)
        counter=0
        for i in range(len(sellorderslist)):
            curcounter=sellorderslist[i]['count']
            counter+=curcounter
            if counter>=sellcountfordropcoef:
                if i==0:
                    if counter>sellcountfordropcoef:
                        return sellorderslist[i]['price']-0.01
                    else:
                        return sellorderslist[i]['price']
                else:
                    return sellorderslist[i-1]['price']
    if checkgraphicboost(prices):
        sellcountforboostcoef=int(sellhistcountcoefforgraphicboost*itemsellcountforday)
        counter=0
        for i in range(len(sellorderslist)):
            curcounter=sellorderslist[i]['count']
            counter+=curcounter
            if counter>=sellcountforboostcoef:
                if i==0:
                    if counter>sellcountforboostcoef:
                        return sellorderslist[i]['price']-0.01
                    else:
                        return sellorderslist[i]['price']
                else:
                    return sellorderslist[i-1]['price']
    maxbuyorder=int(histogram['highest_buy_order'])/100
    sellpricebad=0
    sellpricegood=0
    sellcountbad=int(sellhistcountbadcoef*itemsellcountforday)
    sellcountgood=int(sellhistcountgoodcoef*itemsellcountforday)
    counter=0
    for i in range(len(sellorderslist)):
        curcounter=sellorderslist[i]['count']
        counter+=curcounter
        if counter>=sellcountbad:
            if i==0:
                if counter>sellcountbad:
                    sellpricebad=sellorderslist[i]['price']-0.01
                    break
                else:
                    sellpricebad=sellorderslist[i]['price']
                    break
            else:
                sellpricebad=sellorderslist[i-1]['price']
                break
    counter=0
    for i in range(len(sellorderslist)):
        curcounter=sellorderslist[i]['count']
        counter+=curcounter
        if counter>=sellcountgood:
            if i==0:
                if counter>sellcountgood:
                    sellpricegood=sellorderslist[i]['price']-0.01
                    break
                else:
                    sellpricegood=sellorderslist[i]['price']
                    break
            else:
                sellpricegood=sellorderslist[i-1]['price']
                break
    if sellpricebad/maxbuyorder<1.04 and sellpricegood/maxbuyorder<1.06:
        return sellpricegood
    else:
        return sellpricebad


def getitemsellorderslist(histogram):
    log('steamf: getitemsellorderslist')
    sellorders=histogram['sellordergraph']
    reslist=list()
    precount=0
    for itemsellorders in sellorders:
        count=itemsellorders[1]
        rescount=count-precount
        precount=count
        resobject={'price':itemsellorders[0],'count':rescount}
        reslist.append(resobject)
    return reslist


def calculateitemsellcount(prices,time2,time1=0):
    log('steamf: calculateitemsellcount')
    count=0
    for i in range(time1,time2):
        count+=int(prices[-1-i][2])
    return count


def getcountofpriceorhigherinhistory24_12_6_3(prices,price):
    log('steamf: getcountofpriceorhigherinhistory24_12_6_3')
    count12h24h=parsecountofpriceorhigherinhistory(prices,price,24,12)
    count6h12h=parsecountofpriceorhigherinhistory(prices,price,12,6)
    count3h6h=parsecountofpriceorhigherinhistory(prices,price,6,3)
    count3h=parsecountofpriceorhigherinhistory(prices,price,3)
    return count12h24h,count6h12h,count3h6h,count3h


def parsecountofpriceorhigherinhistory(prices,price,time2,time1=0):
    log('steamf: parsecountofpriceorhigherinhistory')
    count=0
    for i in range(time1, time2):
        if prices[-1-i][1]>=price:
            count+=int(prices[-1-i][2])
    return count
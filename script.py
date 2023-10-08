
import requests
from bs4 import BeautifulSoup 
import json
import yfinance as yf
import time
from collections import defaultdict

f = open("./data.json")
data = json.load(f)
f.close()
print("have " + str(len(data)) + " tickers")

def wr():
    f = open("./data.json", "w")
    f.write(json.dumps(data))
    print("wrote " + str(len(data)) + " tickers")
    f.close()

# Get all tickers


# f1 = open("./nasdaq.json")
# f2 = open("./nyse.json")
# tickers1 = json.load(f1)
# tickers2 = json.load(f2)
# f.close()
# c = 0
# for t in tickers1 + tickers2:
#     if t["symbol"] not in data:
#         data[t["symbol"]] = {"name": t["name"]}
#         print(t, t["name"])
#     else:
#         info = data[t["symbol"]]
#         info["sector"] = t["sector"] or "Other"
#         info["name"] = t["name"] or info["name"]
# print(c)
# wr()

# REMOVE WEIRD TICKERS
# n = 0
# for ticker, info in list(data.items()):
#     if len(ticker) >= 6: 
#         del data[ticker]
#         print("REMOVED: ", ticker)
#         n += 1
#         continue
#     for char in "-./:,;^&*()%$#@!+=`~?\\[\{\}]":
#         if char in ticker:
#             del data[ticker]
#             print("REMOVED: ", ticker)
#             n += 1
#             break

# wr()



# GET ESG Scores

# headers = {
#     'Host': 'finance.yahoo.com',
#     'User-Agent': 'Mozilla/5.0'
# }
# c = 10
# for ticker, info in data.items():
#     if "total" in data[ticker] or "-" in ticker: continue

#     c -= 1
#     n -= 1
#     if not c: 
#         c = 100
#         print("REMAINING: ", n)
#         wr()

#     try:
#         url = f"https://finance.yahoo.com/quote/{ticker}/sustainability?p={ticker}"
#         # time.sleep(1)
#         res = requests.get(url, headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')

#         esg = soup.find_all('div', class_='D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)') 
#         if len(esg) == 3:
#             info["environmental"] = float(esg[0].text)
#             info["social"] = float(esg[1].text)
#             info["governance"] = float(esg[2].text)
#             info["total"] = info["governance"]+ info["social"]+ info["environmental"]
#         else:
#             info["total"] = -1

#     except Exception as e:
#         print(e)

#     finally:
#         print(info)

# wr()


# #Add sector info
# r = 0
# c = 10
# for t, d in data.items():
#     r+=1
#     print(r)
#     if "sector" in d: continue
#     d["sector"] = "Other"
#     c -= 1
#     if not c: 
#         c = 100
#         wr()

#     try:
#         info = yf.Ticker(t).info
#         if "sector" in info:
#             d["sector"] = info["sector"]
#             print(d)        
#     except Exception as e:
#         print("ERROR: ", e, t, d)
# wr()




# n = 0
# for ticker, info in data.items():
#     if "sector" not in info:
#         print("No sector: ", ticker)
#         info["sector"] = "Other"
#         n += 1
#     if "total" not in info:
#         print("No esg: ", ticker)
#         info["total"] = -1
#         n += 1
# print(n)






# # Map containing list of tickers that belong to the sector
# sectors = defaultdict(list)
# for t, d in data.items():
#     sectors[d["sector"]].append(t)

# print(sorted(sectors.keys()))

# # Calculate the average ESG score for the sector
# averageBySector = defaultdict(float)
# for sector, tickers in sectors.items():
#     esgScores = [(data[ticker]["environmental"],data[ticker]["social"],data[ticker]["governance"],data[ticker]["total"]) for ticker in tickers if data[ticker]["total"] != -1]
#     eSum = sum([score[0] for score in esgScores])
#     sSum = sum([score[1] for score in esgScores])
#     gSum = sum([score[2] for score in esgScores])
#     tSum = sum([score[3] for score in esgScores])
#     l = len(esgScores)
#     if esgScores:
#         averageBySector[sector] = (eSum/l, sSum/l, gSum/l, tSum/l)
#     else: 
#         averageBySector[sector] = None
#     print(sector, averageBySector[sector])

# f = open("data_final.json", "w")
# f.write(json.dumps(
#     {"averageBySector": averageBySector, "sectors": sectors, "tickers": data}
# ))
# f.close()
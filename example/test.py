# package import statement
from SmartApi import SmartConnect #or from smartapi.smartConnect import SmartConnect

#import smartapi.smartExceptions(for smartExceptions)

#create object of call
obj=SmartConnect(api_key="luqqitFE")

#login api call

data = obj.generateSession("A59123614","8126","IJYRLZE56Y4ZKDHRJHBYRWVDCA")

refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)
#place order
#gtt rule creation
#gtt rule list
#Historic api
try:
    historicParam={
    "exchange": "NSE",
    "symboltoken": "26000",
    "interval": "ONE_MINUTE",
    "fromdate": "2021-02-08 09:00", 
    "todate": "2021-02-08 09:16"
    }
    obj.getCandleData(historicParam)
except Exception as e:
    print("Historic Api failed: {}".format(e.message))
#logout
try:
    logout=obj.terminateSession('A59123614')
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))

##Estimate Charges
# params = {
#     "orders": [
#         {
#             "product_type": "DELIVERY",
#             "transaction_type": "BUY",
#             "quantity": "10",
#             "price": "800",
#             "exchange": "NSE",
#             "symbol_name": "745AS33",
#             "token": "17117"
#         },
#         # {
#         #     "product_type": "DELIVERY",
#         #     "transaction_type": "BUY",
#         #     "quantity": "10",
#         #     "price": "800",
#         #     "exchange": "BSE",
#         #     "symbol_name": "PIICL151223",
#         #     "token": "726131"
#         # }
#     ]
# }
# estimateCharges = obj.estimateCharges(params)
# print(estimateCharges);

# params = {
#     "isin":"INE528G01035",
#     "quantity":"1"
# }
# verifyDis = obj.verifyDis(params)
# print(verifyDis);

# params = {
#     "dpId":"33200",
#     "ReqId":"2351614738654050",
#     "boid":"1203320018563571",
#     "pan":"JZTPS2255C"
# }
# generateTPIN = obj.generateTPIN(params)
# print(generateTPIN);

# params = {
#     "ReqId":"2351614738654050"
# }
# getTranStatus = obj.getTranStatus(params)
# print(getTranStatus);

# params = {
#     "name":"TCS",
#     "expirydate":"25JAN2024"
# }
# optionGreek = obj.optionGreek(params)
# print(optionGreek);

# params = {
#     "datatype":"PercOIGainers",
#     "expirytype":"NEAR" 
# }
# gainersLosers = obj.gainersLosers(params)
# print(gainersLosers);

# putCallRatio = obj.putCallRatio()
# print(putCallRatio);

# params = {
#     "expirytype":"NEAR",
#     "datatype":"Long Built Up"
# }
# OIBuildup = obj.oIBuildup(params)
# print(OIBuildup);

## WebSocket

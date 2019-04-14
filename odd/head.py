def getHeaders(head):
    headers = {}
    for h in head.splitlines():
        headers[h.split(': ')[0]] = h.split(': ')[1]
    return headers


all_cookies = {
    "通众易加专卖店": 'cna=Oab5EqW3/UsCAXkgxqJMT3MA; isg=BKmpgfbr0Uf00O0iYx83aKuNu1PD3pTe2E1xx0ueIRDPEsgkk8ePeSUE1H6BkTXg; enc=8CeHMXLtq6D7gs3SCRg58vHKwQNHMISpXUBJaAWgtbYP9icg1nhAEjZkKkiKtwviNQQys3mVYe43pH%2FRjjibDA%3D%3D; um=GB262B925F3854B1027EEBD3E34219C97A66F0A; t=8a90b96cf4366182c79789846a731a95; _cc_=W5iHLLyFfA%3D%3D; tg=0; ali_ab=113.73.29.71.1533941862115.2; l=bBT67WGRvzf1BcvjBOCwNuIRCE79IIObYuPRw5Dvi_5Cw1L_GKbOl9DLZep6V15PONTB4i5WivpTde288P9f.; thw=cn; mt=ci=0_0; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=1692f5de0d9518-0e701e9c1c1ada8-4a576a-fa000-1692f5de0da26; _bl_uid=nwjm7tCs02j4t4x5Xyt22pO4UyzX; uc3=id2=&nk2=&lg2=; tracknick=; cookie2=1753c824f1ef35b27d91001bd516ea26; _tb_token_=bee556658509; x=1584616501; uc1=cookie14=UoTZ50Ce%2FTnB3A%3D%3D&lng=zh_CN; skt=b0d10dc786b1b58a; sn=%E9%80%9A%E4%BC%97%E6%98%93%E5%8A%A0%E4%B8%93%E5%8D%96%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4103200120; csg=f662907f; v=0; apush02e1ebbc3a50ec1e1f85f932e6f9a217=%7B%22ts%22%3A1553957834036%2C%22parentId%22%3A1553957834030%7D',
    "亿维通众专卖店": "cna=Oab5EqW3/UsCAXkgxqJMT3MA; isg=BI-P3JqsDzVIrQs0SZ25hmHvHSVZHOqgoi9XMaGeJv4QcKJyr4DGJi0mcmjrE7tO; enc=8CeHMXLtq6D7gs3SCRg58vHKwQNHMISpXUBJaAWgtbYP9icg1nhAEjZkKkiKtwviNQQys3mVYe43pH%2FRjjibDA%3D%3D; um=GB262B925F3854B1027EEBD3E34219C97A66F0A; t=8a90b96cf4366182c79789846a731a95; _cc_=W5iHLLyFfA%3D%3D; tg=0; ali_ab=113.73.29.71.1533941862115.2; l=bBT67WGRvzf1BdqfBOfwquIRCE7OiQA2CkPzw4NGPICP_H1DhST1BZ_cUALkC31Na6MHS3SVNIDpB588ayUih; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=1692f5de0d9518-0e701e9c1c1ada8-4a576a-fa000-1692f5de0da26; _store_token=; cookie2=10c2ecdec0b7e814bde3880b0ca1ff71; _tb_token_=f93de65e6669f; x=925025092; mt=ci=0_0; uc3=id2=&nk2=&lg2=; uc1=cookie14=UoTZ4Sf5berRdA%3D%3D&lng=zh_CN; skt=ea2f66841aba4469; sn=%E4%BA%BF%E7%BB%B4%E9%80%9A%E4%BC%97%E4%B8%93%E5%8D%96%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4102709064; tracknick=; csg=ea3fbc8b; apushc4158f1603065ab927acf1cf680bb4e5=%7B%22ts%22%3A1555244436535%2C%22parentId%22%3A1555168895963%7D; v=0",
    "通众旗舰店": "cna=Oab5EqW3/UsCAXkgxqJMT3MA; isg=BA8PUdOuj7Xf94u0yR05BuFvnaXZnGogIq_XsSEcmH6E8C7yKQBZpqvm8uhrkzvO; enc=8CeHMXLtq6D7gs3SCRg58vHKwQNHMISpXUBJaAWgtbYP9icg1nhAEjZkKkiKtwviNQQys3mVYe43pH%2FRjjibDA%3D%3D; um=GB262B925F3854B1027EEBD3E34219C97A66F0A; t=8a90b96cf4366182c79789846a731a95; _cc_=W5iHLLyFfA%3D%3D; tg=0; ali_ab=113.73.29.71.1533941862115.2; l=bBT67WGRvzf1BDd8BOCwmuIRCE79vIObYuPRw5Dvi_5Np68sCY6OlZfXgFJ6V15POi8B4i5WivpTFUFYJPvf.; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=1692f5de0d9518-0e701e9c1c1ada8-4a576a-fa000-1692f5de0da26; _store_token=; cookie2=10c2ecdec0b7e814bde3880b0ca1ff71; _tb_token_=f93de65e6669f; x=3079394145; mt=ci=0_0; uc3=id2=&nk2=&lg2=; uc1=cookie14=UoTZ4Sf5aQkpFQ%3D%3D&lng=zh_CN; skt=a435e487b50be8a5; sn=%E9%80%9A%E4%BC%97%E6%97%97%E8%88%B0%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4094468737; tracknick=; csg=24ae55eb; v=0",
    "亿维办公旗舰店": "t=146b8a759ca793b0781e09bb6d7658ea; cna=IfuQFBJMQD4CAXFKKOIRLopa; ali_ab=113.74.41.76.1547430640066.5; mt=ci=0_0; l=aBqaMaNxysN-0foKkMa_pSG5g707yP5Puz8F1MwHiTEhNPG2YfLcEGrx-zzINaAQtIbfu02V505j0; _m_h5_tk=63f705bc2e3037b7bb458165b89ef0a8_1548071381668; _m_h5_tk_enc=8fb7bb5838ee77b1166446dd1291c36a; enc=ZfIo7EggHanDUx0JfOqUCzTJfnyrqGu2CmZY5VBhgp%2F61%2BtgfQ%2BCetLb6qpxtysKDNQZyOhBwxkwYfZ5%2BymXLw%3D%3D; cookie2=12e645262ea73470788e1fead159cfe7; _tb_token_=e731e8eee3b3b; x=2933051711; uc3=id2=&nk2=&lg2=; skt=0f4f392a9418681d; sn=%E4%BA%BF%E7%BB%B4%E5%8A%9E%E5%85%AC%E6%97%97%E8%88%B0%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4094724875; tracknick=; csg=c8181ec7; v=0; uc1=cookie14=UoTYPmCpR2CW%2BQ%3D%3D&lng=zh_CN; apushbe9bcadb4aabcb1dd3eb19aa72693de8=%7B%22ts%22%3A1548142072139%2C%22parentId%22%3A1548142060000%7D; isg=BL-_RIlM37DY0NvgTKI_QGsNTpOJDBMpb-oML1GNPG61YNjiWHWnl48ypnA7OOu-",
    "众泰": "t=146b8a759ca793b0781e09bb6d7658ea; cna=IfuQFBJMQD4CAXFKKOIRLopa; ali_ab=113.74.41.76.1547430640066.5; mt=ci=0_0; l=aBqaMaNxysN-0foKkMa_pSG5g707yP5Puz8F1MwHiTEhNPG2YfLcEGrx-zzINaAQtIbfu02V505j0; _m_h5_tk=63f705bc2e3037b7bb458165b89ef0a8_1548071381668; _m_h5_tk_enc=8fb7bb5838ee77b1166446dd1291c36a; enc=ZfIo7EggHanDUx0JfOqUCzTJfnyrqGu2CmZY5VBhgp%2F61%2BtgfQ%2BCetLb6qpxtysKDNQZyOhBwxkwYfZ5%2BymXLw%3D%3D; cookie2=12e645262ea73470788e1fead159cfe7; _tb_token_=e731e8eee3b3b; x=2829884134; uc3=id2=&nk2=&lg2=; skt=926601fee5e58904; sn=%E4%BC%97%E6%B3%B0%E5%8A%9E%E5%85%AC%E4%B8%93%E8%90%A5%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4102789044; tracknick=; csg=d8354810; v=0; uc1=cookie14=UoTYPmCpRqku5w%3D%3D&lng=zh_CN; apush6fe09dcfe234ff394df6dc3e87b88877=%7B%22ts%22%3A1548143616761%2C%22parentId%22%3A1548143610749%7D; isg=BLy8zin_zAleSPgZSzMMSfTMjVquHWCwoEtvtpY8yaeKYV_rv8Q7boaTRcm8KZg3"
}

def gc(c):
    cc = {}
    for i in c.split('; '):
        cc[i.split('=')[0]] = i.split('=')[1]
    return cc

shop = '通众易加专卖店'
all_cookies[shop] = 'cna=Oab5EqW3/UsCAXkgxqJMT3MA; isg=BKmpgfbr0Uf00O0iYx83aKuNu1PD3pTe2E1xx0ueIRDPEsgkk8ePeSUE1H6BkTXg; enc=8CeHMXLtq6D7gs3SCRg58vHKwQNHMISpXUBJaAWgtbYP9icg1nhAEjZkKkiKtwviNQQys3mVYe43pH%2FRjjibDA%3D%3D; um=GB262B925F3854B1027EEBD3E34219C97A66F0A; t=8a90b96cf4366182c79789846a731a95; _cc_=W5iHLLyFfA%3D%3D; tg=0; ali_ab=113.73.29.71.1533941862115.2; l=bBT67WGRvzf1BcvjBOCwNuIRCE79IIObYuPRw5Dvi_5Cw1L_GKbOl9DLZep6V15PONTB4i5WivpTde288P9f.; thw=cn; mt=ci=0_0; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=1692f5de0d9518-0e701e9c1c1ada8-4a576a-fa000-1692f5de0da26; _bl_uid=nwjm7tCs02j4t4x5Xyt22pO4UyzX; uc3=id2=&nk2=&lg2=; tracknick=; cookie2=1753c824f1ef35b27d91001bd516ea26; _tb_token_=bee556658509; x=1584616501; uc1=cookie14=UoTZ50Ce%2FTnB3A%3D%3D&lng=zh_CN; skt=b0d10dc786b1b58a; sn=%E9%80%9A%E4%BC%97%E6%98%93%E5%8A%A0%E4%B8%93%E5%8D%96%E5%BA%97%3A%E8%8F%9C%E9%B8%9F; unb=4103200120; csg=f662907f; v=0; apush02e1ebbc3a50ec1e1f85f932e6f9a217=%7B%22ts%22%3A1553957834036%2C%22parentId%22%3A1553957834030%7D'

cookies = gc(all_cookies[shop])

param = """auctionType: 0
close: 0
pageNum: 1
pageSize: 15
queryMore: true
rxAuditFlag: 0
rxElectronicAllFlag: 0
rxElectronicAuditFlag: 0
rxHasSendFlag: 0
rxOldFlag: 0
rxSendFlag: 0
rxSuccessflag: 0
rxWaitSendflag: 0
tradeTag: 0
useCheckcode: false
useOrderInfo: false
errorCheckcode: false
action: itemlist/SoldQueryAction
prePageNo: 1
buyerNick: 
dateBegin: 1551369600111
dateEnd: 1554048000858
logisticsService: 
orderStatus: 
queryOrder: desc
rateStatus: 
refund: 
sellerNick: 
tabCode: latest3Months"""

params = getHeaders(param)
# shop = str(cookie.split('; x=')[1].split('; ')[0])
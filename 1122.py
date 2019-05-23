{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from pyquery import PyQuery as pq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "cookies = {\"over18\":\"1\"}\n",
    "res = requests.get(\"https://www.ptt.cc/bbs/Gossiping/index.html\",\\\n",
    "                  cookies = cookies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "mainDoc = pq(res.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Re: [新聞] 吳祥輝：柯P有15萬票我一生閉嘴 hgt\n",
      "Re: [ＦＢ] 柯文哲選情 非常危險 we27\n",
      "[問卦] 想賣小吃擺攤該賣什麼 MEVIUS\n",
      "[新聞] 淪選票毒藥？吳敦義六都「互踢」 ak904\n",
      "[問卦] 1個月100多塊零用錢有啥用? brian751204\n",
      "[新聞] 台灣能源政策何去何從？陳立誠：燃煤、核 toastdown\n",
      "[問卦] 有沒有虛擬貨幣暴跌的八卦 peter610297\n",
      "[新聞] 台大醫院人體實驗出包　女助理竟偽造衛福 losel\n",
      "[新聞] 盧秀燕稱選舉不簽承諾書 網友翻舊文2次 jason31831\n",
      "[問卦] 誰跟我一樣已經把選舉公報跟辯論會看了個 bearboss\n",
      "Re: [新聞] 完工90%！環狀線拚明年通車 最新進度曝光 nocesst\n",
      "Re: [爆卦] 盧秀燕有感人大絕招! marvinwu\n",
      "Re: [新聞] 《17》直播創辦人贈未婚妻黑卡「盡量刷」 gofigure\n",
      "Re: [ＦＢ] 林洲民 - 「白色改革」都發局的政績 asynchronous\n",
      "[新聞] 嚇呆！人妻路邊吃宵夜 被奶襲哥當眾扯爆 badbadook\n",
      "[問卦] 金城武在八卦板被桶會發生什麼事？ sheep531531\n",
      "[問卦] 刀劍神域是不是影響台灣文學很深? glthe1\n",
      "Re: [爆卦] 吳子嘉：柯文哲100%落選 miyarou\n",
      "[問卦] 被告白該如何應對 cefywo\n",
      "Re: [爆卦] 嘉義市議員候選人背景介紹指南 sevenzgod\n",
      "Re: [ＦＢ] 柯文哲選情 非常危險 digitalman\n",
      "Re: [新聞] 中華奧會若被停權 楊忠和：可用獨立運動 smd1201\n",
      "[問卦] 往又老又窮邁進的台北 whkuo\n",
      "[新聞] 護唇膏害韓國瑜?學者嗨解:膏字帶月是當選 udo\n",
      "Re: [爆卦] 韓國瑜三民區掃街 ck5\n",
      "Re: [問卦] 怎麼到現在還有人相信國民黨、民進黨？ Benetnasch\n",
      "[問卦] 為什麼感覺今天八卦板士氣有點低落? vovzz\n",
      "Re: [爆卦] 趙少康精準預測大選結果 strlen\n",
      "[新聞] 蔡壁如LINE截圖外流 操作棄保被抓包 earning\n",
      "[問卦] 有沒有某陣營很奇怪的八卦 RogerStark\n",
      "[問卦] 三環三線蓋一半了 cloud72426\n",
      "Re: [爆卦] 韓國瑜三民區掃街 seabox\n",
      "Re: [爆卦] 趙少康精準預測大選結果 tetsu2008\n",
      "[問卦] 泡麵打不開的八卦？ LeisureBan\n",
      "[新聞] 柯文哲車隊掃街 支持者排隊等候合影 thnlkj0665\n",
      "[新聞] 選前展現武力 博科聖地攻擊造成53死 haijin\n",
      "[問卦] 明天夜市要賣啥會發財 shinnim\n",
      "Re: [問卦] 法律系畢業卻考不上律師執照的八卦 kilof\n",
      "Re: [新聞] 永春都更居民登報感謝 柯P：遇到困難不是擺爛一定要解決 tai728\n",
      "[問卦] 金城武還在八卦板嗎? douCai\n",
      "[新聞] 遭韓粉霸凌後...再替蘇貞昌唱　詹雅雯激 WeiKitten\n",
      "Re: [爆卦] 吳子嘉：柯文哲100%落選 luckysmallsu\n",
      "Re: [問卦] 學店生能做什麼工作 yoyodiy\n",
      "Re: [爆卦] 吳子嘉：柯文哲100%落選 CPer\n",
      "Re: [ＦＢ] 柯文哲選情 非常危險 iamlaw\n",
      "[問卦] 體力對男人的重要性 pierre0916\n",
      "Re: [爆卦] 韓國瑜三民區掃街 EDFR\n",
      "Re: [爆卦] 韓國瑜三民區掃街 potabaw\n",
      "Re: [爆卦] 吳子嘉：柯文哲100%落選 hsuans\n",
      "[新聞] 新聞圈傳喜事 愛國主播徐展元娶了谷懷萱 train60125\n",
      "[新聞] 罕見！高雄議員涉賄選　投票前夕遭拘提 Powerplayer\n",
      "Re: [爆卦] 韓國瑜三民區掃街 sjm0626\n",
      "Re: [問卦] 關羽不北伐 蜀漢可以進行啥策略 qk123\n",
      "[新聞] 吳祥輝：柯P有15萬票我一生閉嘴 threee\n",
      "[問卦] 在八卦酸同學被同學發現該怎麼辦？ trylin\n",
      "[新聞] 怒！飆仔伴隨韓國瑜車隊「合法飆車」　쐠 kiemets\n",
      "[問卦] 信義區晚上怎麼這麼亮的八卦？ y22710616\n",
      "Re: [新聞] 「要求副總統不出席世大運閉幕式」 姚文 lovetweet\n"
     ]
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    for each in mainDoc(\"#main-container > div.r-list-container.action-bar-margin.bbs-screen > div > div.title >a \").items():\n",
    "        print(each.text(),each.parent().siblings(\".meta>.author\").text())\n",
    "    mainDoc.make_links_absolute(base_url=res.url)\n",
    "    res = requests.get(mainDoc(\"#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)\").attr(\"href\"),\\\n",
    "                                          cookies = cookies)\n",
    "    mainDoc = pq(res.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "看板 Gossiping 文章列表 - 批踢踢實業坊\n",
      "批踢踢實業坊 › 看板 Gossiping 關於我們 聯絡資訊\n",
      "看板 精華區\n",
      "最舊 ‹ 上頁 下頁 › 最新\n",
      "2\n",
      "Re: [問卦] 住高雄澄清湖附近是啥感覺的卦\n",
      "tai0916\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 tai0916 的文章\n",
      "11/22\n",
      "Re: [新聞] 蔡壁如LINE截圖外流 操作棄保被抓包\n",
      "Fant1408\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 Fant1408 的文章\n",
      "11/22\n",
      "35\n",
      "Re: [爆卦] 韓國瑜三民區掃街\n",
      "Cetuximab\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 Cetuximab 的文章\n",
      "11/22\n",
      "[問卦] 同性戀合法化的滑坡效應被低估?\n",
      "TouchAgain\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 TouchAgain 的文章\n",
      "11/22\n",
      "Re: [新聞] 中華奧會若被停權 楊忠和：可用獨立運動\n",
      "wattswatts\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 wattswatts 的文章\n",
      "11/22\n",
      "10\n",
      "Re: [問卦] 住高雄澄清湖附近是啥感覺的卦\n",
      "Mews\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 Mews 的文章\n",
      "11/22\n",
      "(本文已被刪除) [PANG920]\n",
      "-\n",
      "11/22\n",
      "5\n",
      "[問卦] 天氣冷的時候在床上拿IPAD是不是很爽?\n",
      "than09138\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 than09138 的文章\n",
      "11/22\n",
      "18\n",
      "Re: [爆卦] 韓國瑜三民區掃街\n",
      "kobest\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 kobest 的文章\n",
      "11/22\n",
      "5\n",
      "Re: [爆卦] 韓國瑜三民區掃街\n",
      "mitsui0309\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 mitsui0309 的文章\n",
      "11/22\n",
      "9\n",
      "[新聞] 直播推泰語教學　男女報名比例懸殊\n",
      "eric830204\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 eric830204 的文章\n",
      "11/22\n",
      "4\n",
      "[問卦] 有哪些厲害的人出生在中華民國？\n",
      "toro556613\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 toro556613 的文章\n",
      "11/22\n",
      "4\n",
      "Re: [爆卦] 韓國瑜三民區掃街\n",
      "processior\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 processior 的文章\n",
      "11/22\n",
      "3\n",
      "[問卦] 公館水源市場前排什麼？\n",
      "rs23234\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 rs23234 的文章\n",
      "11/22\n",
      "29\n",
      "[爆卦] 鬼島夢想家(29) 厚友誼片尾曲-新北地獄去\n",
      "rhino0314\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 rhino0314 的文章\n",
      "11/22\n",
      "7\n",
      "Re: [新聞] 傳小英官邸談選情！台北只要「丁贏不了」\n",
      "orze04\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 orze04 的文章\n",
      "11/22\n",
      "36\n",
      "Re: [爆卦] 韓國瑜三民區掃街\n",
      "antiyahoo\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 antiyahoo 的文章\n",
      "11/22\n",
      "1\n",
      "[爆卦] 游良福這次有選!!\n",
      "u2721\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 u2721 的文章\n",
      "11/22\n",
      "2\n",
      "Re: [問卦] 被告白該如何應對\n",
      "balahaha\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 balahaha 的文章\n",
      "11/22\n",
      "[問卦] 847是否有可能其實是資深柯粉？\n",
      "plusonezero\n",
      "⋯\n",
      "搜尋同標題文章\n",
      "搜尋看板內 plusonezero 的文章\n",
      "11/22\n",
      "本網站已依台灣網站內容分級規定處理。此區域為限制級，未滿十八歲者不得瀏覽。\n",
      "(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','https://www.google-analytics.com/analytics.js','ga'); ga('create', 'UA-32365737-1', { cookieDomain: 'ptt.cc', legacyCookieDomain: 'ptt.cc' }); ga('send', 'pageview');\n"
     ]
    }
   ],
   "source": [
    "print(mainDoc.text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
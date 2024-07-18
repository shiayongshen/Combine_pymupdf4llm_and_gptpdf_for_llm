# 基於Pymupdf與gptpdf之LLM PDF parser

2024-07-17 16:36:22,271 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

這是一張東京都的氣候圖表，顯示了每月的平均最高和最低溫度以及降雨量。圖表分為兩部分，分別以攝氏（°C）和華氏（°F）表示溫度，降雨量則分別以毫米（mm）和英寸（in）表示。
![image](https://github.com/shiayongshen/Combine_pymupdf4llm_and_gptpdf_for_llm/blob/main/pic/3_2.png)
### 攝氏（°C）和毫米（mm）：
- **溫度**：
  - 1月：最高10°C，最低1°C
  - 2月：最高10°C，最低2°C
  - 3月：最高14°C，最低4°C
  - 4月：最高19°C，最低9°C
  - 5月：最高23°C，最低14°C
  - 6月：最高26°C，最低18°C
  - 7月：最高29°C，最低22°C
  - 8月：最高31°C，最低23°C
  - 9月：最高27°C，最低20°C
  - 10月：最高22°C，最低14°C
  - 11月：最高16°C，最低8°C
  - 12月：最高12°C，最低4°C

- **降雨量**：
  - 1月：52 mm
  - 2月：56 mm
  - 3月：118 mm
  - 4月：125 mm
  - 5月：138 mm
  - 6月：168 mm
  - 7月：154 mm
  - 8月：168 mm
  - 9月：210 mm
  - 10月：198 mm
  - 11月：93 mm
  - 12月：51 mm

### 華氏（°F）和英寸（in）：
- **溫度**：
  - 1月：最高49°F，最低34°F
  - 2月：最高51°F，最低35°F
  - 3月：最高56°F，最低40°F
  - 4月：最高66°F，最低49°F
  - 5月：最高73°F，最低57°F
  - 6月：最高78°F，最低64°F
  - 7月：最高85°F，最低71°F
  - 8月：最高87°F，最低73°F
  - 9月：最高80°F，最低67°F
  - 10月：最高71°F，最低58°F
  - 11月：最高61°F，最低47°F
  - 12月：最高53°F，最低38°F

- **降雨量**：
  - 1月：2.1 in
  - 2月：2.2 in
  - 3月：4.6 in
  - 4月：4.9 in
  - 5月：5.4 in
  - 6月：6.6 in
  - 7月：6 in
  - 8月：6.6 in
  - 9月：8.3 in
  - 10月：7.8 in
  - 11月：3.6 in
  - 12月：2 in

資料來源：[28]

2024-07-17 16:36:34,824 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
![image](https://github.com/shiayongshen/Combine_pymupdf4llm_and_gptpdf_for_llm/blob/main/pic/4_0.png)
以下是根據圖片中的表格架構以及提供的Markdown文字內容所製作的HTML表格：


<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <table>
        <thead>
            <tr>
                <th rowspan="2">月份</th>
                <th colspan="12">東京</th>
                <th rowspan="2">全年</th>
            </tr>
            <tr>
                <th>1月</th>
                <th>2月</th>
                <th>3月</th>
                <th>4月</th>
                <th>5月</th>
                <th>6月</th>
                <th>7月</th>
                <th>8月</th>
                <th>9月</th>
                <th>10月</th>
                <th>11月</th>
                <th>12月</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>历史最高温 °C（°F）</td>
                <td>22.6 (72.7)</td>
                <td>24.9 (76.8)</td>
                <td>28.1 (82.6)</td>
                <td>29.2 (84.6)</td>
                <td>32.6 (90.7)</td>
                <td>36.4 (97.5)</td>
                <td>39.5 (103.1)</td>
                <td>39.1 (102.4)</td>
                <td>38.1 (100.6)</td>
                <td>32.6 (90.7)</td>
                <td>27.3 (81.1)</td>
                <td>24.8 (76.6)</td>
                <td>39.5 (103.1)</td>
            </tr>
            <tr>
                <td>平均高温 °C （°F）</td>
                <td>9.8 (49.6)</td>
                <td>10.9 (51.6)</td>
                <td>14.2 (57.6)</td>
                <td>19.4 (66.9)</td>
                <td>23.6 (74.5)</td>
                <td>26.1 (79.0)</td>
                <td>29.9 (85.8)</td>
                <td>31.3 (88.3)</td>
                <td>27.5 (81.5)</td>
                <td>22.0 (71.6)</td>
                <td>16.7 (62.1)</td>
                <td>12.0 (53.6)</td>
                <td>20.3 (68.5)</td>
            </tr>
            <tr>
                <td>日均气温 °C （°F）</td>
                <td>5.4 (41.7)</td>
                <td>6.1 (43.0)</td>
                <td>9.4 (48.9)</td>
                <td>14.3 (57.7)</td>
                <td>18.8 (65.8)</td>
                <td>21.9 (71.4)</td>
                <td>25.7 (78.3)</td>
                <td>26.9 (80.4)</td>
                <td>23.3 (73.9)</td>
                <td>18.0 (64.4)</td>
                <td>12.5 (54.5)</td>
                <td>7.7 (45.9)</td>
                <td>15.8 (60.4)</td>
            </tr>
            <tr>
                <td>平均低温 °C （°F）</td>
                <td>1.2 (34.2)</td>
                <td>2.1 (35.8)</td>
                <td>5.0 (41.0)</td>
                <td>9.8 (49.6)</td>
                <td>14.6 (58.3)</td>
                <td>18.5 (65.3)</td>
                <td>22.4 (72.3)</td>
                <td>23.5 (74.3)</td>
                <td>20.3 (68.5)</td>
                <td>14.8 (58.6)</td>
                <td>8.8 (47.8)</td>
                <td>3.8 (38.8)</td>
                <td>12.1 (53.8)</td>
            </tr>
            <tr>
                <td>历史最低温 °C（°F）</td>
                <td>−9.2 (15.4)</td>
                <td>−7.9 (17.8)</td>
                <td>−5.6 (21.9)</td>
                <td>−3.1 (26.4)</td>
                <td>2.2 (36.0)</td>
                <td>8.5 (47.3)</td>
                <td>13.0 (55.4)</td>
                <td>15.4 (59.7)</td>
                <td>10.5 (50.9)</td>
                <td>−0.5 (31.1)</td>
                <td>−3.1 (26.4)</td>
                <td>−6.8 (19.8)</td>
                <td>−9.2 (15.4)</td>
            </tr>
            <tr>
                <td>平均降水量 mm（英寸）</td>
                <td>59.7 (2.35)</td>
                <td>56.5 (2.22)</td>
                <td>116.0 (4.57)</td>
                <td>133.7 (5.26)</td>
                <td>139.7 (5.50)</td>
                <td>167.8 (6.61)</td>
                <td>156.2 (6.15)</td>
                <td>154.7 (6.09)</td>
                <td>224.9 (8.85)</td>
                <td>234.8 (9.24)</td>
                <td>96.3 (3.79)</td>
                <td>57.9 (2.28)</td>
                <td>1,598.2 (62.91)</td>
            </tr>
            <tr>
                <td>平均降雪量 cm（英寸）</td>
                <td>4 (1.6)</td>
                <td>4 (1.6)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>0 (0)</td>
                <td>8 (3.1)</td>
            </tr>
            <tr>
                <td>平均降水天数（≥ 0.5 mm）</td>
                <td>5.3</td>
                <td>6.1</td>
                <td>10.3</td>
                <td>10.9</td>
                <td>11.1</td>
                <td>12.8</td>
                <td>12.0</td>
                <td>9.4</td>
                <td>12.3</td>
                <td>11.8</td>
                <td>8.2</td>
                <td>5.8</td>
                <td>116</td>
            </tr>
            <tr>
                <td>平均降雪天数（≥ 1 cm）</td>
                <td>0.7</td>
                <td>0.8</td>
                <td>0.2</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.0</td>
                <td>0.1</td>
                <td>1.8</td>
            </tr>
            <tr>
                <td>平均相對濕度（％）</td>
                <td>51</td>
                <td>52</td>
                <td>57</td>
                <td>62</td>
                <td>68</td>
                <td>75</td>
                <td>76</td>
                <td>74</td>
                <td>75</td>
                <td>71</td>
                <td>64</td>
                <td>56</td>
                <td>65</td>
            </tr>
            <tr>
                <td>月均日照時數</td>
                <td>192.6</td>
                <td>170.4</td>
                <td>175.3</td>
                <td>178.8</td>
                <td>179.6</td>
                <td>124.2</td>
                <td>151.4</td>
                <td>174.2</td>
                <td>126.7</td>
                <td>129.4</td>
                <td>149.8</td>
                <td>174.4</td>
                <td>1,926.8</td>
            </tr>
            <tr>
                <td colspan="14">数据来源1：[28]</td>
            </tr>
            <tr>
                <td colspan="14">数据来源2：[37]</td>
            </tr>
        </tbody>
    </table>
</body>



2024-07-17 16:37:42,430 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
![image](https://github.com/shiayongshen/Combine_pymupdf4llm_and_gptpdf_for_llm/blob/main/pic/10_0.png)
這張圖表顯示了自1920年以來東京的人口變化趨勢。圖表中的數據點和標註顯示了幾個重要的里程碑：

- 1956年，東京人口超過800萬。
- 1963年，東京人口超過1000萬。
- 2001年，東京人口超過1200萬。

從圖表中可以看出，東京的人口在1920年為370萬，之後逐漸增長，並在1945年出現下降，隨後又迅速回升並持續增長。到2013年，東京的人口達到約1329萬。

2024-07-17 16:37:55,717 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
![image](https://github.com/shiayongshen/Combine_pymupdf4llm_and_gptpdf_for_llm/blob/main/pic/11_0.png)
以下是根據圖片中的表格結構和Markdown中的文字內容製作的HTML表格：

<table border="1">
  <tr>
    <td rowspan="2">東京都區部</td>
    <td colspan="2">足立區、荒川區、板橋區、江戶川區、大田區、葛飾區、北區、江東區、品川區、澀谷區、新宿區、杉並區、墨田區、世田谷區、台東區、中央區、千代田區、豐島
區、中野區、練馬區、文京區、港區、目黑區</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="3">多摩地域</td>
    <td>市</td>
    <td>昭島市、秋留野市、稻城市、青梅市、清瀨市、國立市、小金井市、國分寺市、小平市、狛江市、立川市、多摩市、調布市、西東京市、八王子市、羽村市、東久留米市、東村山
市、東大和市、日野市、府中市、福生市、町田市、三鷹市、武藏野市、武藏村山市</td>
  </tr>
  <tr>
    <td>西多摩郡</td>
    <td>奥多摩町、日之出町、瑞穗町、檜原村</td>
  </tr>
  <tr></tr>
  <tr>
    <td rowspan="4">東京都島嶼部</td>
    <td>大島支廳</td>
    <td>大島町、利島村、新島村、神津島村</td>
  </tr>
  <tr>
    <td>三宅支廳</td>
    <td>三宅村、御藏島村</td>
  </tr>
  <tr>
    <td>八丈支廳</td>
    <td>八丈町、青島村</td>
  </tr>
  <tr>
    <td>小笠原支廳</td>
    <td>小笠原村</td>
  </tr>
</table>




2024-07-17 16:39:47,572 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
以下是根據圖片中的表格架構以及提供的Markdown文字內容所製作的HTML表格：

![image](https://github.com/shiayongshen/Combine_pymupdf4llm_and_gptpdf_for_llm/blob/main/pic/22_0.png)
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<body>
    <table>
        <thead>
            <tr>
                <th>城市</th>
                <th>國家</th>
                <th>締結日期</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>紐約</td>
                <td>美国</td>
                <td>1960年 2月29日</td>
            </tr>
            <tr>
                <td>北京</td>
                <td>中华人民共和国</td>
                <td>1979年 3月14日</td>
            </tr>
            <tr>
                <td>巴黎</td>
                <td>法國</td>
                <td>1982年 7月14日</td>
            </tr>
            <tr>
                <td>新南威爾士州</td>
                <td>澳大利亞</td>
                <td>1984年 5月 9日</td>
            </tr>
            <tr>
                <td>首爾</td>
                <td>韩国</td>
                <td>1988年 9月 3日</td>
            </tr>
            <tr>
                <td>雅加達</td>
                <td>印度尼西亞</td>
                <td>1989年10月23日</td>
            </tr>
            <tr>
                <td>聖保羅州</td>
                <td>巴西</td>
                <td>1990年 6月13日</td>
            </tr>
            <tr>
                <td>開羅省</td>
                <td>埃及</td>
                <td>1990年10月23日</td>
            </tr>
            <tr>
                <td>莫斯科</td>
                <td>俄羅斯</td>
                <td>1991年 7月16日</td>
            </tr>
            <tr>
                <td>柏林</td>
                <td>德国</td>
                <td>1994年 5月14日</td>
            </tr>
            <tr>
                <td>羅馬</td>
                <td>義大利</td>
                <td>1996年 7月 5日</td>
            </tr>
            <tr>
                <td>大倫敦</td>
                <td>英国</td>
                <td>2015年10月14日</td>
            </tr>
        </tbody>
    </table>
</body>
</html>

這段HTML代碼將會生成一個表格，表格的結構和圖片中的表格一致，並且填入了提供的Markdown文字內容。

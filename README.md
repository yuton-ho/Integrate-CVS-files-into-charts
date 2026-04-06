In Intergrate.py, place the files that need to be analyzed.
Filtering_Attribute.py extracts important attributes from the files, after which the user selects which attributes to use.
Read_data.py stores the corresponding data into record.csv based on the user’s selected attributes. This step is intended to reduce the time required for data retrieval.
Check_data.py is used to verify whether there are any issues with the user’s data.
Finally, Graph.py uses matplotlib to generate visualizations.

---

Filtering_Attribute.py:
The method for extracting attributes is as follows: if there are more than two attributes with the same name, they will not be included in useful_columns. Attribute names are case-sensitive. The output is useful_columns.

Check_data.py:
The criteria for data validation are:

1. Whether there is missing data
2. Whether there are extreme values that could affect the charts

---

在Intergrate.py檔案中將需要分析的檔案放入，從Filtering_Attribute.py:提取檔案中重要的屬性，隨後使使用者選擇使用哪些屬性。Read_data.py根據使用者選擇的屬性，將對應資料儲存至record.csv，這一步是為了降低提取資料時，所需讀取的時間。使用Check_data.py檢查使用者資料是否有問題。最後Graph.py使用 matplotlib繪製圖表。

---
Filtering_Attribute.py:提取檔案的方式是如果存在相同名字超過2個的屬性名稱，則不加入useful_columns。大小寫有差異。輸出useful_columns。
Check_data.py檢查資料的標準是:1.資料有無缺失2.是否存在影響圖表的極端值

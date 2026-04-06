import pandas as pd

def load_data(filename, nrows=None):
    df = pd.read_csv(filename, nrows=1)

    # 取得所有欄位的名稱列表
    all_columns = df.columns.tolist()

    # 統計每個欄位名稱出現次數
    column_counts = {col: all_columns.count(col) for col in all_columns}

    # 過濾：排除名稱出現超過兩次、以及不需要的影像標記欄位
    useful_columns = [
        col
        for col in all_columns
        if column_counts[col] <= 2 and 'Hencky' not in col and 'mm]' not in col
    ]

def main():
    """主程式：讀取資料並顯示篩選結果。"""
    useful_columns = load_data('U90Al6XXX-T81_BatchB5R02T2.686W12.68.csv', nrows=None)
    print("--- 篩選出的關鍵機台數據屬性 ---")
    # 只針對我們篩選出來的欄位檢視型態
    print(useful_columns)
def select_attributes(attributes):
    """
    從屬性清單中讓使用者選擇需要的屬性。

    使用者輸入格式：資料編號、1號座標、2號座標
    例如：1,2,3

    Args:
        attributes (list): 屬性名稱列表

    Returns:
        list: 使用者選擇的屬性（資料編號、1號座標、2號座標）
    """
    print("可選屬性：")
    for i, attr in enumerate(attributes, start=1):
        print(f"  {i}. {attr}")

    selected = input(
        "請輸入要選取的屬性編號（格式：資料編號、1號座標、2號座標，enter=預設前三個屬性）："
    ).strip()

    if not selected:
        default = attributes[:3]
        print(f"已預設選擇：{default}")
        return default

    try:
        indices = [int(x.strip()) for x in selected.split(',') if x.strip()]
        chosen = [attributes[i-1] for i in indices if 1 <= i <= len(attributes)]
        if len(chosen) != 3:
            print("請輸入三個屬性編號，已預設選擇前三個屬性。")
            return attributes[:3]
        return chosen
    except ValueError:
        print("輸入格式錯誤，已預設選擇前三個屬性。")
        return attributes[:3]

if __name__ == '__main__':
    main()


'''
得到結果:Count                  int64
Time_1               float64
Time_0               float64
Dev2/ai0             float64
Dev2/ai1             float64
Dev2/ai2             float64
Dev2/ai3             float64
Displacement_(mm)    float64
Force_(kN)           float64
Extensometer         float64
unused               float64
dtype: object
'''

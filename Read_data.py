import pandas as pd


def load_to_record(file_path, usecols, output_filename='record.csv'):
    """
    讀取 CSV 檔案並只讀取指定欄位，然後保存到 record.csv。

    Args:
        file_path (str): CSV 檔案路徑
        usecols (list): 要讀取的欄位列表
        output_filename (str): 輸出檔案名稱，預設為 record.csv

    Returns:
        pd.DataFrame: 讀取的資料框
    """
    df = pd.read_csv(file_path, usecols=usecols)
    df.to_csv(output_filename, index=False)
    print(f"資料已保存到 {output_filename}")
    return df


def main():
    """主程式：讀取資料並保存。"""
    # 指定要讀取的欄位：時間 (Time_1)、位移 (Displacement_(mm))、力量 (Force_(kN))
    usecols = ['Time_1', 'Displacement_(mm)', 'Force_(kN)']
    
    # 讀取原始資料並保存到 record.csv
    load_to_record('c:/Project_Pratice/U90Al6XXX-T81_BatchB5R02T2.686W12.68.csv', usecols)


if __name__ == '__main__':
    main()

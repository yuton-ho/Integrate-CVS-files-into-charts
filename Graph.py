import pandas as pd
import matplotlib.pyplot as plt


def process_and_plot(input_filename, output_filename, usecols):
    """
    讀取資料、保存到新檔案、並繪製力量 vs 位移的圖形。
    
    Args:
        input_filename (str): 原始 CSV 檔案路徑
        output_filename (str): 輸出檔案名稱
        usecols (list): 要讀取的欄位列表
    """
    # 讀取原始資料
    df = pd.read_csv(input_filename, usecols=usecols)
    
    # 將結果保存到新檔案
    df.to_csv(output_filename, index=False)
    print(f"資料已保存到 {output_filename}")
    
    # 從輸出檔案重新讀取數據
    df = pd.read_csv(output_filename)
    
    # 繪製力量 vs 位移的圖形
    plt.figure(figsize=(10, 6))
    plt.plot(df['Displacement_(mm)'], df['Force_(kN)'], linewidth=2)
    plt.xlabel('Displacement_(mm)', fontsize=12)
    plt.ylabel('Force_(kN)', fontsize=12)
    plt.title('Force vs Displacement', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == '__main__':
    # 指定要讀取的欄位：時間 (Time_1)、位移 (Displacement_(mm))、力量 (Force_(kN))
    usecols = ['Time_1', 'Displacement_(mm)', 'Force_(kN)']
    
    # 執行完整流程：讀取、保存、繪製
    process_and_plot(
        'c:/Project_Pratice/U90Al6XXX-T81_BatchB5R02T2.686W12.68.csv',
        'record.csv',
        usecols
    )

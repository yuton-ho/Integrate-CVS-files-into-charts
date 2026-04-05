import pandas as pd

def check_data(filename, select_attributes):
    """
    讀取 CSV 並進行資料完整性檢查和統計摘要。

    Args:
        filename (str): CSV 檔案名稱
        select_attributes (list): 要讀取的欄位列表

    Returns:
        dict: 包含檢查結果和問題回報的字典
    """
    df = pd.read_csv(filename, usecols=select_attributes)
    
    issues = []  # 記錄發現的問題

    # 1. 檢查缺失值
    print("===== 第一步：檢查有沒有空白遺失的資料 =====")
    missing_data = df.isnull().sum()
    print(missing_data)
    
    has_missing = (missing_data > 0).any()
    if has_missing:
        issues.append(f"❌ 發現缺失值：{dict(missing_data[missing_data > 0])}")
        print("⚠️  警告：存在缺失值！")
    else:
        print("✓ 資料完整，無缺失值。")
    print("-" * 40)

    # 2. 統計摘要（只對數值列進行）
    print("\n===== 第二步：用統計摘要看極端值 =====")
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    summary = None
    
    if numeric_columns:
        summary = df[numeric_columns].describe()
        print(summary)
        print("\n極端值檢查：")
        for col in numeric_columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
            if len(outliers) > 0:
                issues.append(f"⚠️  {col} 中有 {len(outliers)} 個異常值")
                print(f"  ⚠️  {col}：檢測到 {len(outliers)} 個異常值")
            else:
                print(f"  ✓ {col}：無異常值")
    else:
        print("無數值列，跳過統計摘要。")
        issues.append("⚠️  無數值列可進行統計分析")
    print("-" * 40)

    # 3. 問題回報
    print("\n===== 資料檢查問題回報 =====")
    if issues:
        print("🔴 發現問題：")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("🟢 資料檢查通過，無發現問題！")
    print("-" * 40)

    return {
        'missing_data': missing_data,
        'summary': summary,
        'issues': issues,
        'dataframe': df,
        'has_issues': len(issues) > 0,
    }


def main():
    """主程式：執行所有資料檢查步驟。"""
    select_attributes = ['Count', 'Time_1', 'Displacement_(mm)', 'Force_(kN)']
    result = check_data('U90Al6XXX-T81_BatchB5R02T2.686W12.68.csv', select_attributes)

    # 如果需要，可在這裡使用返回值
    # print(result['logical_checks'])


if __name__ == '__main__':
    main()
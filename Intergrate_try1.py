import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
#import寫好的資料處理模組
import Filtering_Attribute
import Check_data
import Read_data
import Graph

def process_data(file_path, thickness, width, usecols):
    # ==========================================
    # 這裡放你之前寫的 Pandas 邏輯
    # 1. 讀取與過濾欄位
    # 2. 數據歸零
    # 3. 計算截面積 A0 = thickness * width
    # 4. 計算應力與應變
    # 5. 產出圖表與 PDF
    # ==========================================
    try:
        # 1. 讀取與過濾欄位
        df = Read_data.load_and_select_columns(file_path, usecols=usecols)
        
        # 2. 保存處理後的資料
        Read_data.save_to_csv(df, 'record.csv')
        
        # 3. 重新讀取並檢查資料
        df = pd.read_csv('record.csv')
        Check_data.check_missing_data(df)
        
        summary_cols = [c for c in ['Displacement_(mm)', 'Force_(kN)'] if c in usecols]
        if summary_cols:
            Check_data.show_summary(df, summary_cols)

        if 'Time_1' in usecols and 'Force_(kN)' in usecols:
            Check_data.check_physical_logic(df)
        else:
            print("⚠️ 物理邏輯檢查：需要 Time_1 與 Force_(kN) 才能完整檢查。")

        # 4. 產出圖表（只有当 Displacement 和 Force 都存在）
        if 'Displacement_(mm)' in usecols and 'Force_(kN)' in usecols:
            Graph.process_and_plot(file_path, 'record.csv', usecols=usecols)
        else:
            print("⚠️ 跳過圖表繪製：需要 Displacement_(mm) 與 Force_(kN) 欄位。")

        print(f"✅ 正在處理：{file_path}，厚度：{thickness} mm，寬度：{width} mm")
        return True

    except Exception as e:
        print(f"❌ 處理過程中發生錯誤：{e}")
        return False

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        lbl_file_path.config(text=filepath)


def get_selected_usecols():
    cols = []
    if var_time.get():
        cols.append('Time_1')
    if var_disp.get():
        cols.append('Displacement_(mm)')
    if var_force.get():
        cols.append('Force_(kN)')
    return cols


def start_execution():
    filepath = lbl_file_path.cget("text")
    try:
        # 取得使用者輸入的試片尺寸
        t = float(entry_thickness.get())
        w = float(entry_width.get())
        
        if filepath == "尚未選擇檔案":
            messagebox.showwarning("警告", "請先選擇 CSV 檔案！")
            return
            
        # 檢查欄位選擇
        selected_usecols = get_selected_usecols()
        if not selected_usecols:
            messagebox.showwarning("警告", "請至少選一個欄位！")
            return

        # 呼叫處理函數
        lbl_status.config(text="處理中，請稍候...", fg="blue")
        window.update() # 刷新介面
        
        success = process_data(filepath, t, w, selected_usecols)
        
        if success:
            lbl_status.config(text="✅ 報告生成成功！", fg="green")
            messagebox.showinfo("完成", "PDF 報告已成功產出！")
            
    except ValueError:
        messagebox.showerror("錯誤", "厚度與寬度請輸入正確的數字格式！")
    except Exception as e:
        messagebox.showerror("執行失敗", f"發生錯誤：{e}")

# === 建立主視窗 ===
window = tk.Tk()
window.title("機械測試數據自動化處理工具 v1.0")
window.geometry("400x350")

# --- 區塊 1：檔案選擇 ---
tk.Label(window, text="1. 選擇機台匯出的 CSV 檔", font=("Arial", 12, "bold")).pack(pady=10)
btn_browse = tk.Button(window, text="瀏覽檔案", command=select_file)
btn_browse.pack()
lbl_file_path = tk.Label(window, text="尚未選擇檔案", fg="gray")
lbl_file_path.pack(pady=5)

# --- 區塊 2：輸入試片參數 ---
tk.Label(window, text="2. 輸入試片原始尺寸", font=("Arial", 12, "bold")).pack(pady=10)

frame_inputs = tk.Frame(window)
frame_inputs.pack()

tk.Label(frame_inputs, text="厚度 (mm):").grid(row=0, column=0, padx=5, pady=5)
entry_thickness = tk.Entry(frame_inputs, width=10)
entry_thickness.grid(row=0, column=1, padx=5, pady=5)
entry_thickness.insert(0, "1.2") # 給個預設值，例如常見的 1.2mm

tk.Label(frame_inputs, text="寬度 (mm):").grid(row=1, column=0, padx=5, pady=5)
entry_width = tk.Entry(frame_inputs, width=10)
entry_width.grid(row=1, column=1, padx=5, pady=5)
entry_width.insert(0, "12.5") # 給個預設值

# --- 區塊 3：執行與狀態 ---
# --- 區塊 3：欄位選擇 ---
tk.Label(window, text="3. 選擇要保留的欄位", font=("Arial", 12, "bold")).pack(pady=10)

var_time = tk.BooleanVar(value=True)
var_disp = tk.BooleanVar(value=True)
var_force = tk.BooleanVar(value=True)

chk_time = tk.Checkbutton(window, text="Time_1", variable=var_time)
chk_time.pack(anchor='w', padx=20)
chk_disp = tk.Checkbutton(window, text="Displacement_(mm)", variable=var_disp)
chk_disp.pack(anchor='w', padx=20)
chk_force = tk.Checkbutton(window, text="Force_(kN)", variable=var_force)
chk_force.pack(anchor='w', padx=20)

# --- 區塊 4：執行與狀態 ---
btn_run = tk.Button(window, text="🚀 開始生成報告", bg="lightblue", font=("Arial", 12), command=start_execution)
btn_run.pack(pady=20)

lbl_status = tk.Label(window, text="", font=("Arial", 10))
lbl_status.pack()

window.mainloop()
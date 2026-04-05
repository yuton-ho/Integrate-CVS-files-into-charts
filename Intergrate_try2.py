import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
#import寫好的資料處理模組
import Filtering_Attribute
import Check_data
import Read_data
import Graph



def process_data(file_path):
    attributes = Filtering_Attribute.load_data(file_path, nrows=None)
    if not attributes:
        print("無可用屬性，請檢查資料來源。")
        return []

    selected_attributes = Filtering_Attribute.select_attributes(attributes)
    print(f"已選擇的屬性：{selected_attributes}")
    Read_data.load_to_record(file_path, selected_attributes)
    Check_data.check_data("record.csv", selected_attributes)
    Graph.process_and_plot("record.csv", "record.csv", selected_attributes)
    


def main():
    selected = process_data('U90Al6XXX-T81_BatchB5R02T2.686W12.68.csv')
    

if __name__ == '__main__':
    main()
    
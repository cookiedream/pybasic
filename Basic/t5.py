while True:  # 進入無限迴圈
    try:  # 嘗試讀取使用者輸入的整數
        num = int(input())  # 將使用者輸入的值轉換為整數並儲存在變數 num 中
        if num < 0:  # 如果輸入值小於 0，則將其轉換為正數
            num = 256 + num  # 轉換為正數
        a = bin(num)  # 將轉換後的整數轉換為二進位制的數字，並將結果儲存在變數 x 中
        b = a[2:]  # 從二進位制數字中去除前面的 '0b'，並將結果儲存在變數 y 中
        print(b.zfill(8))  # 在 y 的前面填充 0，直到 o 的長度為 8 位元，並輸出結果
    except:  # 如果出現錯誤，則跳出迴圈
        break

# 第一階段讀取ExcelX,Y軸資料
# 閱讀文章https://openhome.cc/Gossip/CodeData/PythonTutorial/NumericStringPy3.html
# 閱讀文章https://pandas.pydata.org/docs/reference/frame.html
# 閱讀文章https://zhuanlan.zhihu.com/p/259583430
# 閱讀文章https://wreadit.com/@wwwlearncodewithmikecom/post/222271
# 閱讀文章https://www.heywhale.com/mw/notebook/5a59bd9146c4ba639c6f260d
import pandas as pd


def do_someing(df) -> list:
    # df.dropna(0)
    df = df.fillna(0)  # 將空值變為零
    Xnumber = float  # 縱軸數值
    EVnumber = float  # 縱軸數值
    EHnumber = float  # 橫軸數值
    # NewcoorDinate = [] #新座標
    NewcoorDinate = float
    Frequency = float
    MaxH = float
    Frequency = 0.0  # 須移動次數(定義變數)
    EHnumber = 0  # excel第一行
    EVnumber = 8  # excel 孔位X軸座標
    Xnumber = 9  # excel 孔位Y軸座標
    nrows = df.shape[0]  # 計算所有行數
    MaxH = (nrows - 1)  # 若行數=極限會跳出錯誤
    totalfloors = int  # 總層數(手動輸入)
    BX = 0.0  # 舊X軸
    BY = 0.0  # 舊Y軸
    totalNamber = 0
    Xaxis = float
    Yaxis = float
    # Xaxis = 0.0
    # Yaxis = 0.0
    # Xaxis = []
    # Yaxis = []
    moveX_list = []
    moveY_list = []
    while True:
        if Frequency <= MaxH:  # 讀取行數<=最大行數
            Xaxis = df.iat[EHnumber, EVnumber]  # X軸座標=Excel第X行第8排
            Yaxis = df.iat[EHnumber, Xnumber]  # Y軸座標=Excel第X行第9排
            # Newcoordinate = [Xaxis,Yaxis]#現實座標軸(X,Y)
            Xaxis = float(Xaxis)
            Yaxis = float(Yaxis)
            moveX = float(Xaxis) - BX  # X軸位移量=目標位置-當前位置
            moveY = float(Yaxis) - BY  # Y軸位移量=目標位置-當前位置
            moveX_list.append(moveX)
            moveY_list.append(moveY)
            bottom = (moveX**2 + moveY**2)**0.5  # 計算斜邊長 e板-b板
            BX = Xaxis  # 將目標位置更新為當前位置
            BY = Yaxis
            # print(bottom)
            # print("本次X軸位移", moveX)
            # print("本次Y軸位移", moveY)
            # print(type(BX))
            # print(Newcoordinate)
            # print('執行次數為',EHnumber)
            # moveX = Xaxis - BX #X軸位移量=目標位置-當前位置
            # moveY = Yaxis - BY #Y軸位移量=目標位置-當前位置
            # bottom=(moveX**2+moveY**2)**0.5 #計算斜邊長
            # print(bottom)
            EHnumber = EHnumber + 1  # Excel每行讀取
            Frequency = Frequency + 1  # 行數+1
        else:
            break
    return moveX_list, moveY_list


if __name__ == '__main__':
    df = pd.read_excel(r'./352topb.xls')
    moveX_list, moveY_list = do_someing(df)

#

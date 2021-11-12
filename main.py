import pandas as pd
from library import read_excel


if __name__ == '__main__':
    df = pd.read_excel(r'./data/352topb.xls')
    moveX_list, moveY_list = read_excel.do_someing(df)
    print(moveX_list,moveY_list)

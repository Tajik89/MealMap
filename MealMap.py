import numpy as np
import plot as plt
import sheet as sht

full_table = []

print('\n<---------Welcome + to + MealMap-------->\n')
while True :
    user = input(' TAKING@MealMap $ ')

    if 'first' in user or 'get' in user :
        for i in range(1, 51) :
            if i in full_table :
                continue
            print(f' -sudo : First Empty Table is : [{i}]\n')
            break
    
    elif 'full' in user :
        user = int(input(' -TAKING@MealMap : Full/Table $ '))
        if user > 50 :
            print(' --sudo : This Food-court only has 50 table\n')
        else :
            full_table.append(user)
            print()

    elif 'empty' in user :
        user = int(input(' -TAKING@Resturant : Empty/Num $ '))
        andis = 0
        if user > 50 :
            print(' --sudo : This Food-court only has 50 table\n')
        else :
            for k in full_table :
                if k == user :
                    full_table.pop(andis)
                elif andis == (len(full_table) - 1) :
                    print(" -sudo : This table is empty! U can't Use this command :(")
                andis += 1
        print()
    
    elif 'list' in user :
        try :
            data_arr = np.array(full_table)
            sh = len(full_table)
            axis_0 = 0
            for i in range(3, sh + 1) :
                if sh % i == 0 :
                    axis_0 = i
                    break
            axis_1 = int(sh / axis_0)
            data_arr_rsh = data_arr.reshape(axis_0, axis_1)
            print(data_arr_rsh)
        except :
            print(' -sudo : List of full table is less')
        print()
    
    elif 'plot' in user :
        try :
            plt.main()
        except :
            print(' -sudo : The plot  can not show now! Please try leter')
        print()

    elif 'sheet' in user :
        try :
            sht.data_sheet()
        except :
            print(' -sudo : The sheet can not show now! Please trye leter')
        print()

    else :
        print(" -sudo : I dont underestand about Ur command :(\n --Please Use a keyword\n")
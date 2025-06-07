# 時薪  :hourly_salary
# 年薪  :annual_Salary
# 月支出:monthly_fee
# 年支出:annual_fee
# 年儲存:annual_savings

hourly_salary = 150                             #設定時薪
annual_salary = hourly_salary*8*300             #設定年薪
monthly_fee = 9000                              #設定每月花費
annual_fee = monthly_fee*12                     #計算每年花費
annual_savinges = annual_salary - annual_fee    #計算每年儲存金額
print(annual_savinges)                          #顯示出來

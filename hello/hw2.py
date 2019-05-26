#1.	迴圏的練習-expression
#利用for迴圏計算12-22+32-42+…+492-502的值。

#2.	迴圏的練習-factor
#輸入一正整數，求其所有的因數。
#說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。

#3.	迴圏的練習-perfect_number
#一個數字若等於其所有因數的總和，則此數為perfect number。
#出100以內所有的完美數。
#說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。

#4.	迴圏的練習-amstrong
#Amstrong數是指一個三位數的整，其各位數之立方和等於該數本身。
#找出所有的Amstrong數。
#說明：153=13+53+33，故153為Amstrong數。

#5.	迴圈的練習-prime
#輸入一正整數，找出所有小於或等於的質數。


#6.	迴圏的練習-rope
#若有一條繩子長3000公尺，每天剪去一半的長度，需多少天繩子的長度會短於5公尺。
n= 0
a =3000
while a>5:
    a =a/2
    n+=1
print(n)
#7.	迴圏的練習-rabbit
#老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。
n=1
while(n%3!=1or n%5!=3or n%7!=2):
     n+=1
print(n)

#8.	迴圏的練習-password
#出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
#若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
#若輸入不正確，再次出現”請輸入密碼”的提示。
#若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。
num=0
while True:
    ps=eval(input(":::"))
    if  ps==666666:
        print("登入成功！")
        break
    else:
        num+=1
        if num==3:
            print("GG")
            break

#9.	迴圈敘述的練習-stars
#   畫出下列三種排列的星星圖形。
'''
(1)	         *         (2)  * * * * *    (3)     *
        	* *              * * * *           *  *
          	* * *              * * *          *  *  *
          	* * * *              * *         *  *  *  *
          	* * * * *              *        *  *  *  *  *
          	
          	

10.	迴圈敘述的練習-nine_nine
   印出下列九九乘法表：
   		|	1	2	3	4	5	6	7	8	9
    -----------------------------------------------------------------
     9	|	9	18	27	36	45	54	63	72	81
     8	|	8	16	24	32	40	48	56	64
     7	|	7	14	21	28	35	42	49
     6	|	6	12	18	24	30	36
     5	|	5	10	15	20	25
     4	|	4	8	12	16
     3	|	3	6	9
     2	|	2	4
     1	| 	1

     print('----------------------------------------------------------------------')
for i in range(9,0,-1):
    for j in range (1,i+1):
        print("  {} ".format(i*j),end = '\t')
    print()

11.	迴圈敘述的練習-interest
錢精打以10%單利投資100000元，郝細算則以5%複利投資100000元。計算多少年後郝細算的投資可以超過錢精打，並將此時兩人錢數印出。(27年後)
提示：單利公式：P(1+r*n)    複利公式：P(1+r)n
P：本金，r：利率，n：多少年

12.	迴圈敘述的練習-loan
錢不精以100000元分別向銀行、當鋪和地下錢莊借貸。若銀行的年利率為20%，當鋪月利率為10%和地下錢莊日利率為1%。以月為單位，計算一個月後至一年後每個月該歸還多少錢。
'''

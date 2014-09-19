ntusbleague
===========

Format of record:
-----------
(以下所有代號皆不分大小寫)

每場比賽有兩個 team record，每個 team record 由 N 個 row 組成，有幾個先發打者就有幾個 row

row 的組成為: **背號　守位　PA　PA　PA ...**
守位至少要有一個人是投手(P)，其他人的守位目前可以隨便寫


PA 的記法為: **(換投/代打/)方位/記錄/註解**
  
```
    換投:
        p + 背號
    代打: 
        r + 背號
    方位: 
        可以是守備代號(1~10)或L(左外野)、R(右外野)、C(中外野)
    記錄: 
        1B  一壘安打
        2B  二壘安打
        3B  三壘安打
        HR  全壘打
        SF  高飛犧牲打
        BB  保送
        K   三振
        G   滾地球出局
        F   飛球出局
        DP  雙殺打
        FC  野手選擇
        E   失誤
        IB  違規擊球(Illegal Batted)
        CB  投手強襲球(combacker)
        IF  內野高飛必死球(Infield Fly)
        FO  界外飛球接殺(foul out)
    註解: 
        1~4 打點
        r   得分
        x   出局數(目前這個打席造成的出局數，而非球員出局。詳見注意事項3)
        #   換局
        !   比賽結束
        *   補充說明
```        

注意事項:

1. PA 的寫法可以為 
    - **記錄**
    - **方位/記錄**
    - **記錄/註解**
    - **方位/記錄/註解**
  
  Example: 

  左外野二壘安打可以寫成
    - 2B
    - L/2B
    - 7/2B
  
  右外野滿貫全壘打可以寫成
    - HR/4r
    - R/HR/4r
  
2. 滾地球出局(G)、飛球出局(F)、三振(K)、雙殺(DP)、高飛犧牲打(SF)、違規擊球(IB)、投手強襲球(CB)、內野高飛必死球(IF)和界外飛球接殺(FO)可以不用寫出局數(x)。但是野手選擇(FC)不一定有人出局，所以一定要寫有幾個x。若有失誤或助殺出局者一定要寫x。

  Example:
  
  游擊方向滾地球出局帶有一分打點:
    - 6/G/1x
    - G/1
    
  二壘野手選擇造成一壘往二壘跑者出局:
    - 4/FC/x
    - FC/x
    
  游擊手野手選擇傳二壘但沒人出局(非失誤情形):
    - 6/FC
    - FC

  左外野一壘安打帶有一分打點，但二壘跑者在本壘前出局:
    - 7/1B/1x*
    - L/1B/1x*
  
  加註星號(*)是為了方便在PTT上面寫註解
  
3. 若同一打席同時有換投和換代打，可寫 **換投/代打/PA** 或 **代打/換投/PA**

4. **一定要記得加換局(#)以及比賽結束(!)**

Input Example
----------
Away Record:
```
n   1   R/1B/r   8/2B/r   8/F         8/2B/r  8/2B/2r
7   2   8/1B/r   9/3B/2r  6/1B/1      5/E/r   BB/r
23  3   L/1B/1r  7/2B/1r  8/1B/1x*#   7/2B/2r HR/4r
6   P   7/2B/2   7/HR/2r  6/G         7/2B/2  7/2B/r
26  5   6/F/xx*  7/2B/r   r31/6/1B    K       rOB/8/1b/1r
24  6   5/E/r    6/1B/r   7/2B        6/G/#   8/E/r
17  7   7/1B/1   8/HR/3r  K           8/1B/r  6/1B
21  8   7/2B/x#* 7/1B/r   6/F/x#      6/1B/r  1/1B/1
25  9   8/1B     6/E/r    8/1B/r      5/F     6/DP/!
3   10  5/FC/xr  6/1B     rob/k       1/1b/r
```

Home Record:
```
74  1   BB      6/F     7/F
36  2   DP      8/F     BB/r
7   3   1/F/#   9/3B    8/2B/r
71  4   6/E/r   1/G/#   8/2B/2
20  5   6/E     p99/8/F 6/G/!
24  P   K       6/G
35  7   BB      BB
29  8   K       1/1B
21  9   1/E     6/FC/x#
77  10  K/#     1/G
```

Output Example
-------------
* PTT format:

![ScreenShot](https://raw.github.com/phoenix104104/Baseball_Record_Parser/ver2.0/image/ptt_example.jpg)

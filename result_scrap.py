import  pandas as pd
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()

df_cse = pd.DataFrame()
df_it = pd.DataFrame()
df_ece = pd.DataFrame()
df_bt = pd.DataFrame()
df_aeie = pd.DataFrame()
df_che = pd.DataFrame()
df_me = pd.DataFrame()
df_ce = pd.DataFrame()
df_ee = pd.DataFrame()

tit_data=[]

semester = 3
roll_num = 12619001012

for i in range (0,9):

   if (i == 7):
      roll_num = roll_num+5000
   
   elif (i == 8):
      roll_num = roll_num+2000

   df = pd.DataFrame(columns= [" Roll No. "])
   df['Name'] = ""
   # site = driver.get("http://136.232.2.202:8084/stud21o13.aspx")
   site = driver.get("http://136.232.2.202:8084/stud21i.aspx")
   
   roll = driver.find_element_by_css_selector("#form1 > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > input")
   roll.send_keys(roll_num)

   sem = driver.find_element_by_css_selector(f"#form1 > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > select > option:nth-child({semester})")
   sem.click()

   show_result = driver.find_element_by_css_selector("#Button1")
   show_result.click()
   title =[]

   l = driver.find_elements_by_xpath('//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr')
   l = len(l)-1

   for i in range(2,2+l):
      t = driver.find_element_by_xpath(f"//*[@id='form1']/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[{i}]/td[2]").text
      title.append(t)

   df[title] = ""
   df['Odd_SGPA'] = ""
   df['Even_SGPA'] = ""
   df['YGPA'] = ""
   tit_data.append(df)
   roll_num = roll_num+1000
   

df = df.T
for i in range(0,9):
   tit_data[i] = tit_data[i].T
   if i==0 :
      df_cse = tit_data[i]
   elif i==1:
      df_it  = tit_data[i]
   elif i==2:
      df_ece  = tit_data[i]
   elif i==3:
      df_bt  = tit_data[i]
   elif i==4:
      df_aeie  = tit_data[i]
   elif i==5:
      df_che  = tit_data[i]
   elif i==6:
      df_me  = tit_data[i]
   elif i==7:
      df_ce = tit_data[i]
   elif i==8:
      df_ee = tit_data[i]


# CSE:
# 12619001001 ---> 12619001210
# 12620001182 ---> 12620001210

#12620002061 ---> 12620002067
#12620003186 ---> 12620003208
#12620005062 ---> 12620005070
#12620006054 ---> 12620006060
#12620007106 ---> 12620007132
#12620013105 ---> 12620013134

roll_num = 12619001000
count = count1 = count2 = count3 = count4 = 0
count5 = count6 = count7 = count8 = count9 = 0

while(roll_num < 12620014017):
   
   # site = driver.get("http://136.232.2.202:8084/stud21o13.aspx")
   site = driver.get("http://136.232.2.202:8084/stud21i.aspx")

# Finding and inserting Roll No. and Semester  then submiting the data
   roll = driver.find_element_by_css_selector("#form1 > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > input")
   roll.send_keys(roll_num)

   sem = driver.find_element_by_css_selector(f"#form1 > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > select > option:nth-child({semester})")
   sem.click()

   show_result = driver.find_element_by_css_selector("#Button1")
   show_result.click()

# Result page data
   try:  
      
      j=4
      marks = [] 
      stream = driver.find_element_by_xpath('//*[@id="lbltop"]')

      l = driver.find_elements_by_xpath('//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr')
      l = len(l)-1
      
      ROLL_NO = driver.find_element_by_xpath("//*[@id='lblroll']").text[-11:]
      NAME = driver.find_element_by_xpath('//*[@id="lblname"]').text[5:]
      Odd_SGPA = driver.find_element_by_xpath('//*[@id="lblbottom1"]').text[25:]
      Even_SGPA = driver.find_element_by_xpath('//*[@id="lblbottom2"]').text[26:]
      YGPA = driver.find_element_by_xpath('//*[@id="lblbottom3"]').text[16:]

      for i in range(2,2+l):
         mark = driver.find_element_by_xpath(f"//*[@id='form1']/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[{i}]/td[{j}]").text
         marks.append(mark)

      if 'CSE' in stream.text:
         
         count1= count1+1
         df_cse[count1] = df_cse.shape[0]*""
         df_cse.iloc[:2,count1-1] = ROLL_NO, NAME
         df_cse.iloc[2:2+l,count1-1] = marks
         df_cse.iloc[-3,count1-1] = Odd_SGPA
         df_cse.iloc[-2,count1-1] = Even_SGPA
         df_cse.iloc[-1,count1-1] = YGPA
         # print(df_t)
         # print("Ok\n")

      elif 'IT' in stream.text:
   
         count2= count2+1         
         df_it[count2] = df_it.shape[0]*""
         df_it.iloc[:2,count2-1] = ROLL_NO, NAME
         df_it.iloc[2:2+l,count2-1] = marks
         df_it.iloc[-3,count2-1] = Odd_SGPA
         df_it.iloc[-2,count2-1] = Even_SGPA
         df_it.iloc[-1,count2-1] = YGPA
         # print(df_t)
         # print("Ok\n")

      elif 'ECE' in stream.text:
         
         count3= count3+1
         df_ece[count3] = df_ece.shape[0]*""
         df_ece.iloc[:2,count3-1] = ROLL_NO, NAME
         df_ece.iloc[2:2+l,count3-1] = marks
         df_ece.iloc[-3,count3-1] = Odd_SGPA
         df_ece.iloc[-2,count3-1] = Even_SGPA
         df_ece.iloc[-1,count3-1] = YGPA  
         # print(df_t)
         # print("Ok\n")
      
      elif 'BT' in stream.text:
         
         count4= count4+1
         df_bt[count4] = df_bt.shape[0]*""
         df_bt.iloc[:2,count4-1] = ROLL_NO, NAME
         df_bt.iloc[2:2+l,count4-1] = marks
         df_bt.iloc[-3,count4-1] = Odd_SGPA
         df_bt.iloc[-2,count4-1] = Even_SGPA
         df_bt.iloc[-1,count4-1] = YGPA  
         # print(df_t)
         # print("Ok\n")
      
      elif 'AEIE' in stream.text:
         
         count5= count5+1
         df_aeie[count5] = df_aeie.shape[0]*""
         df_aeie.iloc[:2,count5-1] = ROLL_NO, NAME
         df_aeie.iloc[2:2+l,count5-1] = marks
         df_aeie.iloc[-3,count5-1] = Odd_SGPA
         df_aeie.iloc[-2,count5-1] = Even_SGPA
         df_aeie.iloc[-1,count5-1] = YGPA  
         # print(df_t)
         # print("Ok\n")
      
      elif 'ChE' in stream.text:
            
         count6= count6+1
         df_che[count6] = df_che.shape[0]*""
         df_che.iloc[:2,count6-1] = ROLL_NO, NAME
         df_che.iloc[2:2+l,count6-1] = marks
         df_che.iloc[-3,count6-1] = Odd_SGPA
         df_che.iloc[-2,count6-1] = Even_SGPA
         df_che.iloc[-1,count6-1] = YGPA  
         # print(df_t)
         # print("Ok\n")
      
         
      elif 'ME' in stream.text:
         count7= count7+1
         df_me[count7] = df_me.shape[0]*""
         df_me.iloc[:2,count7-1] = ROLL_NO, NAME
         df_me.iloc[2:2+l,count7-1] = marks
         df_me.iloc[-3,count7-1] = Odd_SGPA
         df_me.iloc[-2,count7-1] = Even_SGPA
         df_me.iloc[-1,count7-1] = YGPA
         # print(df_t)
         # print("Ok\n")
      
      elif 'CE' in stream.text:
         
         count8= count8+1
         df_ce[count8] = df_ce.shape[0]*""
         df_ce.iloc[:2,count8-1] = ROLL_NO, NAME
         df_ce.iloc[2:2+l,count8-1] = marks
         df_ce.iloc[-3,count8-1] = Odd_SGPA
         df_ce.iloc[-2,count8-1] = Even_SGPA
         df_ce.iloc[-1,count8-1] = YGPA 
         # print(df_t)
         # print("Ok\n")
      
      elif 'EE' in stream.text:
         
         count9= count9+1
         df_ee[count9] = df_ee.shape[0]*""
         df_ee.iloc[:2,count9-1] = ROLL_NO, NAME
         df_ee.iloc[2:2+l,count9-1] = marks
         df_ee.iloc[-3,count9-1] = Odd_SGPA
         df_ee.iloc[-2,count9-1] = Even_SGPA
         df_ee.iloc[-1,count9-1] = YGPA  
         # print(df_t)
         # print("Ok\n")

      else:
         print(roll_num)
         break

   except NoSuchElementException:
         print("\nThere is no such student exist\n")
   except ValueError:
      print("\nThere is no such student exist\n")

   roll_num = roll_num+1
   if(str(roll_num)[-3:] >= "215"):
      roll_num = roll_num + 785
      print(roll_num)

   elif roll_num == 12619008001:
      roll_num = 12619013000
   elif roll_num == 12619014001:
      roll_num = 12619016000  
   elif roll_num == 12619017001:
      df_cse[count1+1] = df_cse.shape[0]*""
      df_it[count2+1] = df_it.shape[0]*""
      df_ece[count3+1] = df_ece.shape[0]*""
      df_bt[count4+1] = df_bt.shape[0]*""
      df_aeie[count5+1] = df_aeie.shape[0]*""
      df_che[count6+1] = df_che.shape[0]*""
      df_me[count7+1] = df_me.shape[0]*""
      df_ce[count8+1] = df_ce.shape[0]*""
      df_ee[count9+1] = df_ee.shape[0]*""

      roll_num = 12620001181
   elif roll_num ==  12620001211:
      roll_num = 12620002060
   elif roll_num ==  12620002068:
      roll_num = 12620003185
   elif roll_num ==  12620003209:
      roll_num = 12620005061
   elif roll_num ==  12620005071:
      roll_num = 12620006053
   elif roll_num ==  12620006061:
      roll_num = 12620007105
   elif roll_num ==  12620007133:
      roll_num = 12620013105
   



for i in range(2,4):
   count1 = count1 + i
   count2 = count2 + i
   count3 = count3 + i
   count4 = count4 + i
   count5 = count5 + i
   count6 = count6 + i
   count7 = count7 + i
   count8 = count8 + i
   count9 = count9 + i

   df_cse[count1] = df_cse.shape[0]*""
   df_it[count2] = df_it.shape[0]*""
   df_ece[count3] = df_ece.shape[0]*""
   df_bt[count4] = df_bt.shape[0]*""
   df_aeie[count5] = df_aeie.shape[0]*""
   df_che[count6] = df_che.shape[0]*""
   df_me[count7] = df_me.shape[0]*""
   df_ce[count8] = df_ce.shape[0]*""
   df_ee[count9] = df_ee.shape[0]*""


#converting data to excel sheet
with pd.ExcelWriter('4rd_Sem_Result.xlsx') as writer: 
   
   for i in range(0,9):
      tit_data[i] = tit_data[i].T
      if i==0 :
         df_cse = tit_data[i]
         df_cse.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==1:
         df_it  = tit_data[i]
         df_it.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==2:
         df_ece  = tit_data[i]
         df_ece.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==3:
         df_bt  = tit_data[i]
         df_bt.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==4:
         df_aeie  = tit_data[i]
         df_aeie.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==5:
         df_che  = tit_data[i]
         df_che.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==6:
         df_me  = tit_data[i]
         df_me.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==7:
         df_ce  = tit_data[i]
         df_ce.to_excel(writer, sheet_name=f'Sheet_{1+i}')
      elif i==8:
         df_ee  = tit_data[i]
         df_ee.to_excel(writer, sheet_name=f'Sheet_{1+i}')
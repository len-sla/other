from  pesel import *

#     def generate(cls, male: Optional[bool] = None,
#                  year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None):
#         """Generate random PESEL number and create instance of class Pesel

#         :param male: True for male, False for female
#         :type male: bool
#         :param year: The year of birth
#         :type year: int
#         :param month: The month of birth
#         :type month: int
#         :param day: The day of birth
#         :type day: int
#         :return: instance of class Pesel
#         :rtype: pesel.Pesel
#         """

pesele=[]

def save_Table_to_file(temp_table=pesele):
    
    with open(pesel_file_name, 'a') as f:
        for x, item in enumerate(temp_table):
            temp= '\n'+'> ##  Pesel nr:'+str(x+1)+ '/'+str(len(temp_table))+'\n'
            temp1='    \n'
            f.write(temp)
            f.write(pesel_file_name) 
            f.write(temp1)
            f.write("%s\n" % item)

def yesno(question):
    """Simple Yes/No Function."""
    prompt = f'{question} ? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return yesno(question)
    if ans == 'y':
        return True
    return False

m_s = yesno("Are you man Y/N")
year_s= input('give a year(XXXX) number of your birthday')
month_s= input('give a month number(1..12) of your birthday')
day_s=input('give a day number of your birthday')
ile_peseli_s=input('give number 1..100 this will be quantity of generated pesels')

if m_s == True:
    
    sex='male'
    male= True
    
else:
    sex='female'
    male= False
    
pesel_file_name=sex+'-ur-'+day_s+'-'+ month_s+'-'+year_s+'-pesel-x'+ile_peseli_s+'.txt'
print(pesel_file_name)
day=int(day_s)
month= int(month_s)
year= int(year_s)
ile_peseli=int(ile_peseli_s)


for i in range(1, ile_peseli+1):
    a= Pesel.generate(male, year, month, day)
    pesele.append(a)
    print(str(i).rjust(3),' -->', a)

save_Table_to_file(temp_table=pesele)
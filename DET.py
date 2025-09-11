# Daily Expense Tracker project
from tabulate import tabulate                          # we are using "Tabulate" module to print data in form of table 
import matplotlib.pyplot as plt

transactions= [['T01','Eggs','food',100],
         ['T02','jeans','clothes',1000],
         ['T03','facewash','health',200]]
tno=4
def iteminput():
    global tno
    tid = "T0"+str(tno)                               # to avoid dupliate transaction id's
    tno=tno+1
    item = input("enter  purchased item :")
    category =input("enter the category :")
    amount =int(input("enter the amount spent :"))
    transaction=[tid,item,category,amount]               # to track multiple trancastions of different items  we are using list
    transactions.append(transaction)                     # adding transaction data into global transcations list 
    return transaction


def Display():
    headers=["Transaction ID","Item","Category","Amount"]   # Table coloumn headings in tabulate function
    print(tabulate(transactions,headers=headers,tablefmt="rounded_outline"))  # passing transaction data into tabular function


def checkid(tid):
    for i in range(len(transactions)):         # checking tid is present in the given data to update values
        if tid in transactions[i]:              # for getting transaction index
            return i
    return -1
def dismesage(message):                         # to print custom messages
    print("successfully..!!",message)

def update():
    tid=input("enter transaction id (T0x) : ")
    rowindex=checkid(tid)
    if rowindex>=0:
        print("Choose the field to update:")
        print("1.Item name\t2.Category\t3.Amount")
        choice =int(input("enter your choice :"))
        match choice:                         # euqating the cases acccording to the number 
            case 1:
                iname=input("Enter item name :")
                transactions[rowindex][1]=iname         # using row index and coloumn index to access the required  value
                dismesage("updated item name"+tid)
            case 2:
                icat=input("enter categorey name :")
                transactions[rowindex][2]=icat 
                dismesage("updated categorey name"+tid) 
            case 3:
                iamo= int(input("enter amount :"))
                transactions[rowindex][3]=iamo 
                dismesage("updated amount "+tid)    
            case _:                                      #default case
                print("invalid choice.....!!!")    
    else:
        print("Transcation is not present,please try again")   

  
def Delete():
    tid=input("enter transaction id (T0x) : ")
    rowindex=checkid(tid)
    if rowindex>=0:
        removed_data=transactions.pop(rowindex)       # pop() is used to remove the items 
        dismesage(f"transaction {removed_data[0]} is deleted ")
    else:
        print("Transcation is not present,please try again") 
def Analysis():
    summary = {}           # using dictonaries to get summary like category:amount
    total=0
    for transcation in transactions:
        if transcation[2] in summary:                      # here transcation[2] is category 
            summary[transcation[2]] += transcation[3]      # here transcation[3] is amount
        else:
            summary[transcation[2]]=transcation[3]    
        total += transcation[3]    
    summary["total spent"]=total
    return summary
def DetaliedAnalysis():
    expenses = Analysis()  # get data
    
    # Extract categories and amounts
    categories = list(expenses.keys())
    amounts = list(expenses.values())

    # Remove "total spent" if present
    if "total spent" in categories:
        index = categories.index("total spent")
        categories.pop(index)
        amounts.pop(index)

    # Plot Pie Chart
    plt.text(0, 0, f"Total Spent: ₹{expenses['total spent']}", ha="center", va="center", fontsize=10, fontweight="bold")

    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Detailed Analysis")
    plt.show()

def main():
    while True:
        print("Welcome to the Expense tracker ")
        print("1.insert trancation\t2.Display transcations\t3.update transcations\t4.Delete transcation")
        print("5.Detalied analysis\t6.Exit")
        option=int(input("Choose an option : "))
        match option:
            case 1:
                iteminput()
            case 2:
                Display()
            case 3:
                update()
            case 4:
                Delete()
            case 5:
                DetaliedAnalysis()
            case 6:
                print("Closing the program....!!!,Thank-you")
                break
            case _:
                print("Invalid option")
main()
            
        

  



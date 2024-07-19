from tkinter import *
from tkinter.ttk import *
from treasury_web_scraper import get_treasury_securities

jsonlist = get_treasury_securities()

window = Tk()

window.rowconfigure(len(jsonlist)+1, minsize=10)
window.columnconfigure(2, minsize=10)
greeting = Label(window, text="Hello, Welcome to the MoneyWatch!")
greeting.grid(row=0,column=0, pady=2, columnspan=2)

row_index = 1
for each_security_json in jsonlist[:10]:
    """
        print("CUSIP: ", each_security_json["cusip"])
        print("Security Type", each_security_json["securityType"])
        print("Issued Date", each_security_json["issueDate"])
        print("Price Per 100", each_security_json["pricePer100"])
    """
    # this will create a label widget
    cusip_label = Label(window, text = "Cusip: ")
    pricePer100_label = Label(window, text = "Price Per 100:")
    security_type_label = Label(window, text = "Security Type:")
    issue_date_label = Label(window, text = "Issued Date: ")
    
    # grid method to arrange labels in respective
    # rows and columns as specified
    cusip_label.grid(row = row_index, column = 0, sticky = W, pady = 2)
    pricePer100_label.grid(row = row_index+1, column = 0, sticky = W, pady = 2)
    security_type_label.grid(row = row_index+2, column = 0, sticky = W, pady = 2)
    issue_date_label.grid(row = row_index+3, column = 0, sticky = W, pady = 2)
    
    # entry widgets, used to take entry from user
    cusip_value_label = Label(window, text = str(each_security_json["cusip"]))
    pp100_value_label = Label(window, text = str(each_security_json["pricePer100"]))
    sec_type_value_label = Label(window, text = str(each_security_json["securityType"]))
    issue_date_value_label = Label(window, text = str(each_security_json["issueDate"]))
    
    # this will arrange entry widgets
    cusip_value_label.grid(row = row_index, column = 1, pady = 2)
    pp100_value_label.grid(row = row_index+1, column = 1, pady = 2)
    sec_type_value_label.grid(row = row_index+2, column = 1, pady = 2)
    issue_date_value_label.grid(row = row_index+3, column = 1, pady = 2)
    row_index += row_index + 4 

window.mainloop()
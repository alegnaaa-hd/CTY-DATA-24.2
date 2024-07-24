

from Ben_David_Associates_Bank import Bank



carlisle_pa_branch = Bank()

new_customer_answer = ""
NO = "n"
while new_customer_answer != NO:
    
    print("Do you want to add a new customer's card to the bank ? ")
    new_customer_answer = str(input("Enter Yes/No : "))
    new_customer_answer = new_customer_answer.lower()
    new_customer_answer = new_customer_answer[0]

    if new_customer_answer == NO:
        break

    carlisle_pa_branch.get_customer_name_and_generate_new_card()
    carlisle_pa_branch.display_all_bank_cards()
    




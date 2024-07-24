

from Ben_David_Associates_Bank import Bank



carlisle_pa_branch = Bank()

NC = "nc"
TE = "te"
SC = "sc"
DS = "ds"
user_answer = ""
while user_answer != TE:
    
    print("Enter NC  for new credit card")
    print("Enter SC to search credit card by customer name")
    print("Enter DS to display all bank cards/customers")
    print("Enter TE to terminate")
    user_answer = str(input(" : "))
    user_answer = user_answer.lower()
    if user_answer == NC:
        carlisle_pa_branch.get_customer_name_and_generate_new_card()
    elif user_answer == SC:
        customer_name_to_search = str(input("Enter the customer's name to search for: "))
        card_found = carlisle_pa_branch.search_by_customer_name(customer_name=customer_name_to_search)
        if card_found != None:
            card_found.display_card_infos()
    elif user_answer == DS:
        carlisle_pa_branch.display_all_bank_cards()
    elif user_answer == TE:
        print("Exiting the bank app!")
    
    




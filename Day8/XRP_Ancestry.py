from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import json
import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.models.requests import AccountTx, Tx
import datetime
class AncestryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10)
        # Input for the wallet address
        self.address_input = TextInput(hint_text='Enter wallet address', size_hint=(1, 0.1))
        self.layout.add_widget(self.address_input)
        # Button to search for wallet ancestry
        self.search_button = Button(text='Search Wallet Ancestry', size_hint=(1, 0.1))
        self.search_button.bind(on_press=self.search_ancestry)
        self.layout.add_widget(self.search_button)
        # Label to display the wallet address
        self.wallet_address_label = Label(size_hint=(1, 0.1))
        self.layout.add_widget(self.wallet_address_label)
        # Label to display the latest transaction hash
        self.tx_hash_label = Label(size_hint=(1, 0.1))
        self.layout.add_widget(self.tx_hash_label)
        # ScrollView with a Label to display the ancestry results
        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.results_label = Label(size_hint_y=None, markup=True, text_size=(None, None))
        self.scroll_view.add_widget(self.results_label)
        self.layout.add_widget(self.scroll_view)
        # Bind the width of the results_label to the width of the scroll_view
        self.results_label.bind(texture_size=self.results_label.setter('size'))
        self.scroll_view.bind(width=lambda instance, value: setattr(self.results_label, 'text_size', (value, None)))
        return self.layout
    def search_ancestry(self, instance):
        address = self.address_input.text
        if not address:
            self.update_results_text('Please enter a wallet address.')
            return
        # Clear previous results
        self.results_label.text = ''
        # Update wallet address label
        self.wallet_address_label.text = f"Wallet Address: {address}"
        # XRP Ledger API call to get transactions
        client = JsonRpcClient("https://s2.ripple.com:51234/")
        acct_tx = AccountTx(
            account=address,
            limit=10  # Adjust the limit as needed
        )
        response = client.request(acct_tx)
        if response.is_successful():
            transactions = response.result["transactions"]
            transaction_pretty = json.dumps(transactions, indent=2)
            print("transactions[0:1]",transaction_pretty)
            if transactions:
                latest_tx_hash = transactions[0]["tx"]["hash"]
                self.tx_hash_label.text = f"Latest TX Hash: {latest_tx_hash}"
                for tx in transactions:
                    if 'tx' in tx:
                        tx_result = tx["tx"]
                        meta = tx.get("meta", {})
                        self.append_transaction_data(tx_result, meta)
                        # Follow the parent hash to trace the ancestry
                        parent_hash = tx_result.get("previous_txn_id", "N/A")
                        self.trace_ancestry(client, parent_hash)
            else:
                self.update_results_text('No transactions found.')
                self.tx_hash_label.text = ''
        else:
            self.update_results_text('Error retrieving transactions.')
            self.tx_hash_label.text = ''
    def trace_ancestry(self, client, tx_hash):
        if tx_hash == "N/A":
            return
        tx_request = Tx(transaction=tx_hash)
        tx_response = client.request(tx_request)
        if tx_response.is_successful():
            tx_result = tx_response.result
            meta = tx_response.result.get("meta", {})
            self.append_transaction_data(tx_result, meta)
            # Recursive call to trace further ancestry
            parent_hash = tx_result.get("previous_txn_id", "N/A")
            self.trace_ancestry(client, parent_hash)
    def append_transaction_data(self, tx_result, meta):
        ledger_index = tx_result.get("ledger_index", "N/A")
        txs_hash = tx_result.get("hash", "N/A")
        balance = self.get_balance_change(meta)
        close_time = tx_result.get("date", None)
        if close_time:
            close_time = datetime.datetime.fromtimestamp(close_time + 946684800).strftime('%Y-%m-%d %H:%M:%S')
        data = (
            f"Ledger Index: {ledger_index}\n"
            f"Balance Change: {balance}\n"
            f"Date & Time: {close_time}\n"
            f"Txs Hash: {txs_hash}\n\n"
        )
        self.update_results_text(data)
    def get_balance_change(self, meta):
        if "AffectedNodes" in meta:
            for node in meta["AffectedNodes"]:
                node = node.get("ModifiedNode", node.get("CreatedNode", node.get("DeletedNode", {})))
                if "FinalFields" in node and "Balance" in node["FinalFields"]:
                    balance = node["FinalFields"]["Balance"]
                    return balance
        return "N/A"
    def update_results_text(self, text):
        self.results_label.text += text
if __name__ == '__main__':
    AncestryApp().run()
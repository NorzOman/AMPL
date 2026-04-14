

import pandas as pd
from flask import Flask , render_template
from babel.numbers import format_currency

df = pd.read_csv("../data/soq_18_12_25.csv")

app = Flask(__name__)

@app.route("/")
def index():
    amount = (df['PURCHASE_PRICE'] * df['STOCK_QTY']).sum()
    inventoryValue = format_currency(amount,'INR',locale='en_IN')

    onOrder = (df['PURCHASE_PRICE'] * df['ON_ORDER_QTY']).sum()
    amount += onOrder
    estInventoryValue = format_currency(amount,'INR',locale='en_IN')
    return f"Inventory: {inventoryValue} | Estimated: {estInventoryValue}"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

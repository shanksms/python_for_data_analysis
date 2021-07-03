import pandas as pd
#install openpyxl package as well
order_df = pd.read_excel("order.xlsx")

agg_functions = {
    "sale_amount" : ['sum', 'mean'],
    "order_type" : ", ".join
}
grouped_order_df = order_df.groupby(by="order_id").agg(agg_functions)
print(grouped_order_df)
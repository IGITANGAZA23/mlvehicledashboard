import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd


def frequency_table(df):
    # Simple counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']
    # Convert to HTML using the correct method name: .to_html()
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center',
    )
    return table_html


def filter_by_price(df, min_price=5000):
    """
    Filter dataset where vehicle price is above min_price (default: 5000)
    and return HTML table formatted with Bootstrap classes.
    """
    # Detect price column in the dataset (selling_price or price)
    price_col = 'selling_price' if 'selling_price' in df.columns else 'price'
    filtered_df = df[df[price_col] > min_price]

    # Convert to HTML using .to_html()
    table_html = filtered_df.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center',
        index=False,
    )
    return table_html
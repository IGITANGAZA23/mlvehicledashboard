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
    price_col = 'selling_price'
    filtered_df = df[df[price_col] > min_price]

    table_html = filtered_df.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center',
        index=False,
    )
    return table_html


def sales_by_manufacturer_transmission(df):
    # Group by manufacturer and transmission and sum selling_price
    grouped = df.groupby(['manufacturer', 'transmission'])['selling_price'].sum().to_frame(name='total_selling_price')

    table_html = grouped.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center',
    )
    return table_html
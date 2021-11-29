"""
The data used in this research was downloaded on 29/Nov/2021.
"""

import pandas as pd


def print_percentage(label, amount, total_reference):
    percentage = (amount/total_reference)*100
    print(f"Percentage for {label}: {percentage}% ({amount})")


def group_crimes_per_year(df):
    print("1. Is crime going up from 2001 to present days?")
    result = df.groupby(["Year"]).size()
    result.sort_values(ascending=False)
    print(result)
    print()


def group_crimes_per_hours(df):
    print("2. What does crime in Chicago look like at different hours of the day?")
    df.index = pd.to_datetime(df["Date"])
    early_morning = df.between_time('04:00', '07:59')
    morning = df.between_time('08:00', '11:59')
    afternoon = df.between_time('12:00', '15:59')
    evening = df.between_time('16:00', '19:59')
    night = df.between_time('20:00', '23:59')
    late_night = df.between_time('00:00', '03:39')

    total_size = df.size

    print_percentage('Early Morning', early_morning.size, total_size)
    print_percentage('Morning', morning.size, total_size)
    print_percentage('Afternoon', afternoon.size, total_size)
    print_percentage('Evening', evening.size, total_size)
    print_percentage('Night', night.size, total_size)
    print_percentage('Late Night', late_night.size, total_size)
    print()


def group_crimes_per_type(df):
    print("3. What are the most common crimes?")
    result = df.groupby(["Primary Type"]).size()
    result.sort_values(ascending=False)
    print(result)
    print()


def group_crimes_per_seasons(df):
    print("4. How is the crime related to the four seasons?")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    winter = df.loc[
        (df['Month'] == 12) |
        (df['Month'] == 1) |
        (df['Month'] == 2)
    ]
    spring = df.loc[
        (df['Month'] == 3) |
        (df['Month'] == 4) |
        (df['Month'] == 5)
    ]
    summer = df.loc[
        (df['Month'] == 6) |
        (df['Month'] == 7) |
        (df['Month'] == 8)
    ]
    autumn = df.loc[
        (df['Month'] == 9) |
        (df['Month'] == 10) |
        (df['Month'] == 11)
    ]

    total_size = df.size

    print_percentage('Winter', winter.size, total_size)
    print_percentage('Spring', spring.size, total_size)
    print_percentage('Summer', summer.size, total_size)
    print_percentage('Autumn', autumn.size, total_size)
    print()


def group_crimes_per_holidays(df):
    print("5. Are there more or less crimes during holidays?")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    independence_day = df.loc[
        (df['Month'] == 7) |
        (df['Day'] == 4)
    ]
    christmas_eve = df.loc[
        (df['Month'] == 12) |
        (df['Day'] == 24)
    ]
    christmas = df.loc[
        (df['Month'] == 12) |
        (df['Day'] == 25)
    ]
    new_years_eve = df.loc[
        (df['Month'] == 12) |
        (df['Day'] == 31)
    ]
    new_year = df.loc[
        (df['Month'] == 1) |
        (df['Day'] == 1)
    ]

    total_size = df.size

    print_percentage('Independence Day', independence_day.size, total_size)
    print_percentage('Christmas\' Eve', christmas_eve.size, total_size)
    print_percentage('Christmas', christmas.size, total_size)
    print_percentage('New Year\'s Eve', new_years_eve.size, total_size)
    print_percentage('New Year', new_year.size, total_size)

    print()


if __name__ == '__main__':
    columns = [
        "Date",
        "Primary Type",
        "Year"
    ]
    crimes = pd.read_csv("Crimes_Subset_for_Testing.csv", usecols=columns)

    group_crimes_per_year(crimes)
    group_crimes_per_hours(crimes)
    group_crimes_per_type(crimes)
    group_crimes_per_seasons(crimes)
    group_crimes_per_holidays(crimes)

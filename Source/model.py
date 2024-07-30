from data_processing import df1_end_use, df1_product, df2_end_use, df2_product, df3_product, df3_subsector, df4_product, df4_mode_vehicle_type
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Danh sách các quốc gia cần dự đoán
# countries = ["IEA Total", "United Kingdom", "United States", "Japan", "Korea", "Italy", "France", "Germany", "Switzerland"]
num_years_to_forecast = 5
years = np.array([2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2020, 2021]).reshape(-1, 1)

# # --- Hàm điều chỉnh dữ liệu cho năm 2020 do COVID-19 ---
# def adjust_for_covid(df, column_name, change_percentage, country=None):
#     adjustment_factor = 1 + change_percentage
#     if country:
#         df.loc[(df['Country'] == country) & (df['Year'] == 2020), column_name] *= adjustment_factor
#     else:
#         df.loc[(df['Year'] == 2020), column_name] *= adjustment_factor
#
# # --- Hàm điều chỉnh dữ liệu cho năm 2021 ---
# def adjust_for_2021(df, column_name, increase_percentage, reduction_percentage=None):
#     if reduction_percentage is not None:
#         # Bù lại mức giảm so với trước đại dịch
#         adjustment_factor = 1 + (reduction_percentage / (1 - reduction_percentage))
#     else:
#         # Tăng dựa trên mức tăng so với năm 2019
#         adjustment_factor = 1 + increase_percentage
#     df.loc[(df['Year'] == 2021), column_name] *= adjustment_factor
#
# # --- Áp dụng điều chỉnh cho từng dataframe ---
# # 1. Residential (Sinh hoạt)
# adjust_for_covid(df1_end_use, 'Residential appliances', 0.4)  # Tăng nhu cầu điện (bù lại mức giảm 40%)
# adjust_for_2021(df1_product, 'Electricity (PJ)', 0.045)  # Nhu cầu điện tăng 4.5% so với 2019
#
# # 2. Services (Dịch vụ)
# for column_name in ['Services lighting', 'Services space cooling', 'Services space heating']:
#     adjust_for_covid(df2_end_use, column_name, 0.3) # Tăng nhu cầu điện (bù lại mức giảm 30%)
# adjust_for_2021(df2_product, 'Gas (PJ)', 0.032)  # Nhu cầu khí đốt tăng 3.2% so với 2019
#
# # 3. Industry (Công nghiệp)
# adjust_for_covid(df3_product, 'Gas (PJ)', 0.05)  # Giảm nhu cầu khí đốt 5% trên toàn cầu
# adjust_for_covid(df3_product, 'Gas (PJ)', 0.06, country='United States')  # Giảm nhu cầu khí đốt 6% ở Mỹ
# adjust_for_2021(df3_product, 'Gas (PJ)', 0.032) # Nhu cầu khí đốt tăng 3.2% so với 2019
# adjust_for_2021(df3_product, 'Biofuels and waste (PJ)', 0.083)
# adjust_for_2021(df3_product, 'Electricity (PJ)', 0.045) # Nhu cầu điện năng tăng 4.5%
#
# # 4. Transport (Vận tải)
# for column_name in ['Total passenger transport', 'Cars/light trucks', 'Motorcycles', 'Buses', 'Total freight transport', 'Freight trucks']:
#     adjust_for_covid(df4_mode_vehicle_type, column_name, 0.5)  # Tăng nhu cầu dầu mỏ (bù lại mức giảm 50%)
# adjust_for_covid(df4_mode_vehicle_type, 'Total airplanes', 0.6)  # Tăng nhu cầu nhiên liệu máy bay (bù lại mức giảm 60%)



# Hàm dự đoán cho một dòng dữ liệu
def forecast_row(row, column_name):
    X = years
    y = row[column_name].values.astype(float)  # Lấy giá trị từ cột tương ứng với 'column_name'

    # Kiểm tra NaN trong y
    if np.isnan(y).any():
        print(f"  Cảnh báo: Tìm thấy NaN trong cột '{column_name}' của quốc gia '{row['Country'].iloc[0]}'")
        print(f"  Dòng chứa NaN: {row}")

    # Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Xây dựng mô hình Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Dự đoán cho 5 năm tiếp theo
    future_years = np.arange(2022, 2022 + num_years_to_forecast).reshape(-1, 1)
    forecast = model.predict(future_years)
    forecast = np.maximum(forecast, 0)
    # Tính RMSE trên tập kiểm tra
    rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))

    return future_years, forecast, rmse

df1_end_use_forecast = pd.DataFrame()
df1_product_forecast = pd.DataFrame()
df2_end_use_forecast = pd.DataFrame()
df2_product_forecast = pd.DataFrame()
df3_subsector_forecast = pd.DataFrame()
df3_product_forecast = pd.DataFrame()
df4_mode_vehicle_type_forecast = pd.DataFrame()
df4_product_forecast = pd.DataFrame()

def transform_forecast_df(df, column_type):
    df = df.melt(id_vars=["Country", column_type, "Year"],
                 value_vars=[str(year) for year in range(2022, 2027)],
                 var_name="Year", value_name="Value")
    df = df.pivot_table(index=["Country", "Year"], columns=column_type, values="Value").reset_index()
    return df

# Duyệt qua từng dataframe và dự đoán cho các quốc gia được chỉ định
dataframes = [
    (df1_end_use, ['Residential appliances', 'Residential cooking', 'Residential lighting', 'Residential space cooling',
       'Residential space heating', 'Residential water heating'], "End use", "df1_end_use_forecast"),
    (df1_product, ['Biofuels and waste (PJ)', 'Coal and coal products (PJ)', 'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
       'Oil and oil products (PJ)', 'Other sources (PJ)'], "Product", "df1_product_forecast"),
    (df2_end_use, ['Services lighting', 'Services space cooling', 'Services space heating'], "End use",
     "df2_end_use_forecast"),
    (df2_product, ['Biofuels and waste (PJ)', 'Coal and coal products (PJ)', 'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
       'Oil and oil products (PJ)', 'Other sources (PJ)'], "Product", "df2_product_forecast"),
    (df3_subsector, ['Agriculture forestry fishing [ISIC 01-03]', 'Basic metals [ISIC 24]',
       'Chemicals and chemical Products [ISIC 20-21]',
       'Construction [ISIC 41-43]', 'Mining [ISIC 05-09]',
       'Non-metallic minerals [ISIC 23]',
       'Paper pulp and printing [ISIC 17-18]'], "Subsector", "df3_subsector_forecast"),
    (df3_product, ['Biofuels and waste (PJ)', 'Coal and coal products (PJ)', 'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
       'Oil and oil products (PJ)', 'Other sources (PJ)'], "Product", "df3_product_forecast"),
    (df4_mode_vehicle_type, ['Buses', 'Cars/light trucks', 'Freight trucks',
       'Motorcycles', 'Total airplanes', 'Total freight transport',
       'Total passenger transport', 'Total road', 'Total ships',
       'Total trains'], "Mode/vehicle type", "df4_mode_vehicle_type_forecast"),
    (df4_product, ['Coal and coal products (PJ)', 'Diesel and light fuel oil (PJ)',
       'Electricity (PJ)', 'Gas (PJ)', 'Heavy fuel oil (PJ)',
       'Jet fuel and aviation gasoline (PJ)', 'LPG (PJ)',
       'Motor gasoline (PJ)', 'Other sources (PJ)'], "Product", "df4_product_forecast")
]

for df, columns, column_type, forecast_df_name in dataframes:
    # print(f"--- Dự đoán cho {column_type} ---")
    countries = df["Country"].unique()

    # Tạo dataframe mới để lưu kết quả dự báo
    forecast_df = pd.DataFrame(columns=["Country", column_type] + [str(year) for year in range(2022, 2027)])

    for country in countries:
        country_data = df[df["Country"] == country]
        for column_name in columns:
            # In ra thông tin về dòng dữ liệu
            # print(f"- Quốc gia: {country}")
            # print(f"  {column_type}: {column_name}")

            # Dự đoán
            future_years, forecast, rmse = forecast_row(country_data, column_name)
            # for year, value in zip(future_years, forecast):
            #     print(f"  Năm {year[0]}: {value:.2f}")
            # print(f"  RMSE: {rmse:.2f}")  # In RMSE

            # Thêm kết quả dự báo vào dataframe
            new_row = {"Country": country, column_type: column_name}
            new_row.update({str(year[0]): value for year, value in zip(future_years, forecast)})
            forecast_df = pd.concat([forecast_df, pd.DataFrame([new_row])], ignore_index=True)

    # Lưu dataframe dự báo vào biến
    globals()[forecast_df_name] = forecast_df
    # print(f"Đã lưu kết quả dự báo vào dataframe '{forecast_df_name}'")

# BIẾN ĐỔI CÁC DATA FRAME ĐỂ TRỰC QUAN HÓA KẾT QUẢ DỰ BÁO
# from model import df1_end_use_forecast,df1_product_forecast, df2_end_use_forecast,df2_product_forecast,df3_product_forecast,df3_subsector_forecast, df4_mode_vehicle_type_forecast,df4_product_forecast

# Dataframe dự báo df1
df1_end_use_forecast = df1_end_use_forecast.melt(id_vars=["Country", "End use"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df1_end_use_forecast = df1_end_use_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="End use", values="Value").reset_index()
df1_product_forecast = df1_product_forecast.melt(id_vars=["Country", "Product"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df1_product_forecast = df1_product_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="Product", values="Value").reset_index()
# Dataframe dự báo df2
df2_end_use_forecast = df2_end_use_forecast.melt(id_vars=["Country", "End use"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df2_end_use_forecast = df2_end_use_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="End use", values="Value").reset_index()
df2_product_forecast = df2_product_forecast.melt(id_vars=["Country", "Product"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df2_product_forecast = df2_product_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="Product", values="Value").reset_index()
# Dataframe dự báo df3
df3_subsector_forecast = df3_subsector_forecast.melt(id_vars=["Country", "Subsector"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df3_subsector_forecast = df3_subsector_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="Subsector", values="Value").reset_index()
df3_product_forecast = df3_product_forecast.melt(id_vars=["Country", "Product"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df3_product_forecast = df3_product_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="Product", values="Value").reset_index()
# Dataframe dự báo df4
df4_mode_vehicle_type_forecast = df4_mode_vehicle_type_forecast.melt(id_vars=["Country", "Mode/vehicle type"],
                                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                                   var_name="Year",
                                                                   value_name="Value").reset_index(drop=True)
df4_mode_vehicle_type_forecast = df4_mode_vehicle_type_forecast.pivot_table(index=["Country", "Year"],
                                                                           columns="Mode/vehicle type", values="Value").reset_index()
df4_product_forecast = df4_product_forecast.melt(id_vars=["Country", "Product"],
                                                   value_vars=[str(year) for year in range(2022, 2027)],
                                                   var_name="Year",
                                                   value_name="Value").reset_index(drop=True)
df4_product_forecast = df4_product_forecast.pivot_table(index=["Country", "Year"],
                                                       columns="Product", values="Value").reset_index()

# In ra các dataframe dự báo
# print("\n--- df1_end_use_forecast ---\n", df1_end_use_forecast)
# print("\n--- df1_product_forecast ---\n", df1_product_forecast)
# print("\n--- df2_end_use_forecast ---\n", df2_end_use_forecast)
# print("\n--- df2_product_forecast ---\n", df2_product_forecast)
# print("\n--- df3_subsector_forecast ---\n", df3_subsector_forecast)
# print("\n--- df3_product_forecast ---\n", df3_product_forecast)
# print("\n--- df4_mode_vehicle_type_forecast ---\n", df4_mode_vehicle_type_forecast)
# print("\n--- df4_product_forecast ---\n", df4_product_forecast)
# print(df1_end_use_forecast.columns)
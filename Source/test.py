from data_processing import df1_end_use, df2_end_use, df3_subsector, df4_mode_vehicle_type

dataframes = [df1_end_use, df2_end_use, df3_subsector, df4_mode_vehicle_type]

for i, df in enumerate(dataframes):
    print(f"Danh sách quốc gia trong DataFrame {i+1}:")
    countries = df["Country"].unique()
    for country in countries:
        print(f"- {country}")
    print("-" * 20)
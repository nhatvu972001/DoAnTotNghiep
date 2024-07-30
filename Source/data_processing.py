import pandas as pd
import numpy as np

years = [2000, 2005, 2010, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# Sheet 1 Residential - Energy có tên biến là df1
df1 = pd.read_excel("D:\DoAnTotNghiep\Data\IEA-EnergyEnd-usesandEfficiencyIndicatorsdatabase-HighlightsNovember2023.xlsb", sheet_name="Residential - Energy",  skiprows=1)
columns_df1 = df1.columns
columns_new_df1 = [str(col)[-4:] for col in columns_df1 if isinstance(col, int)]
df1.columns = columns_df1[:3].tolist() + columns_new_df1
df1['2000'] = pd.to_numeric(df1['2000'], errors='coerce')
df1['2005'] = pd.to_numeric(df1['2005'], errors='coerce')
df1['2010'] = pd.to_numeric(df1['2010'], errors='coerce')
df1['2015'] = pd.to_numeric(df1['2015'], errors='coerce')
df1['2016'] = pd.to_numeric(df1['2016'], errors='coerce')
df1['2017'] = pd.to_numeric(df1['2017'], errors='coerce')
df1['2018'] = pd.to_numeric(df1['2018'], errors='coerce')
df1['2019'] = pd.to_numeric(df1['2019'], errors='coerce')
df1['2020'] = pd.to_numeric(df1['2020'], errors='coerce')
df1['2021'] = pd.to_numeric(df1['2021'], errors='coerce')
df1.replace("..", np.nan, inplace=True)
df1['Product'] = df1['Product'].str.strip()
df1['Country'] = df1['Country'].str.strip()

# 1.Xử lý dữ liệu đối với hàng có giá trị Gas (PJ) và Total Residential trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Gas (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df1.loc[(df1['End use'] == 'Total Residential') &
            (df1['Product'] == 'Gas (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Gas (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 2.Xử lý dữ liệu đối với hàng có giá trị Coal and coal products (PJ) và Total Residential trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Coal and coal products (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df1.loc[(df1['End use'] == 'Total Residential') &
            (df1['Product'] == 'Coal and coal products (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Coal and coal products (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 3.Xử lý dữ liệu đối với hàng có giá trị Biofuels and waste (PJ) và Total Residential trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Biofuels and waste (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df1.loc[(df1['End use'] == 'Total Residential') &
            (df1['Product'] == 'Biofuels and waste (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Biofuels and waste (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 4.Xử lý dữ liệu đối với hàng có giá trị Heat (PJ) và Total Residential trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Heat (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df1.loc[(df1['End use'] == 'Total Residential') &
            (df1['Product'] == 'Heat (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Heat (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 5.Xử lý dữ liệu đối với hàng có giá trị Other sources (PJ) và Total Residential trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Other sources (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df1.loc[(df1['End use'] == 'Total Residential') &
            (df1['Product'] == 'Other sources (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Total Residential') &
        (df1['Product'] == 'Other sources (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 6.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential space heating trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential space heating') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential space heating') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential space heating') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 7.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential space cooling trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential space cooling') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential space cooling') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential space cooling') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 8.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential water heating trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential water heating') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential water heating') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential water heating') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 9.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential cooking trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential cooking') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential cooking') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential cooking') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 10.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential lighting trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential lighting') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential lighting') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential lighting') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 11.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Residential appliances trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df1.loc[
        (df1['End use'] == 'Residential appliances') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df1.loc[(df1['End use'] == 'Residential appliances') &
            (df1['Product'] == 'Total final energy use (PJ)') &
            (df1['Country'] != 'IEA Total'), str(year)] = df1.loc[
        (df1['End use'] == 'Residential appliances') &
        (df1['Product'] == 'Total final energy use (PJ)') &
        (df1['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)
# HẾT SHEET 1 Residential - Energy...........................................
# Sheet 2 Services - Energy có tên biến là df2
df2 = pd.read_excel("D:\DoAnTotNghiep\Data\IEA-EnergyEnd-usesandEfficiencyIndicatorsdatabase-HighlightsNovember2023.xlsb", sheet_name="Services - Energy",  skiprows=1)
columns_df2 = df2.columns
columns_new_df2 = [str(col)[-4:] for col in columns_df2 if isinstance(col, int)]
df2.columns = columns_df2[:3].tolist() + columns_new_df2
df2['2000'] = pd.to_numeric(df2['2000'], errors='coerce')
df2['2005'] = pd.to_numeric(df2['2005'], errors='coerce')
df2['2010'] = pd.to_numeric(df2['2010'], errors='coerce')
df2['2015'] = pd.to_numeric(df2['2015'], errors='coerce')
df2['2016'] = pd.to_numeric(df2['2016'], errors='coerce')
df2['2017'] = pd.to_numeric(df2['2017'], errors='coerce')
df2['2018'] = pd.to_numeric(df2['2018'], errors='coerce')
df2['2019'] = pd.to_numeric(df2['2019'], errors='coerce')
df2['2020'] = pd.to_numeric(df2['2020'], errors='coerce')
df2['2021'] = pd.to_numeric(df2['2021'], errors='coerce')
df2.replace("..", np.nan, inplace=True)
df2['Product'] = df2['Product'].str.strip()
df2['Country'] = df2['Country'].str.strip()

# 1.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Services space heating trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df2.loc[
        (df2['End use'] == 'Services space heating') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df2.loc[(df2['End use'] == 'Services space heating') &
            (df2['Product'] == 'Total final energy use (PJ)') &
            (df2['Country'] != 'IEA Total'), str(year)] = df2.loc[
        (df2['End use'] == 'Services space heating') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 2.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Services space cooling trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df2.loc[
        (df2['End use'] == 'Services space cooling') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df2.loc[(df2['End use'] == 'Services space cooling') &
            (df2['Product'] == 'Total final energy use (PJ)') &
            (df2['Country'] != 'IEA Total'), str(year)] = df2.loc[
        (df2['End use'] == 'Services space cooling') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 3.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) trong cột Product và Services lighting trong cột End use nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df2.loc[
        (df2['End use'] == 'Services lighting') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df2.loc[(df2['End use'] == 'Services lighting') &
            (df2['Product'] == 'Total final energy use (PJ)') &
            (df2['Country'] != 'IEA Total'), str(year)] = df2.loc[
        (df2['End use'] == 'Services lighting') &
        (df2['Product'] == 'Total final energy use (PJ)') &
        (df2['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# HẾT SHEET 2 Services - Energy...........................................
# Sheet 3 Industry - Energy có tên biến là df3
df3 = pd.read_excel("D:\DoAnTotNghiep\Data\IEA-EnergyEnd-usesandEfficiencyIndicatorsdatabase-HighlightsNovember2023.xlsb", sheet_name="Industry - Energy",  skiprows=1)
columns_df3 = df3.columns
columns_new_df3 = [str(col)[-4:] for col in columns_df3 if isinstance(col, int)]
df3.columns = columns_df3[:3].tolist() + columns_new_df3
df3['2000'] = pd.to_numeric(df3['2000'], errors='coerce')
df3['2005'] = pd.to_numeric(df3['2005'], errors='coerce')
df3['2010'] = pd.to_numeric(df3['2010'], errors='coerce')
df3['2015'] = pd.to_numeric(df3['2015'], errors='coerce')
df3['2016'] = pd.to_numeric(df3['2016'], errors='coerce')
df3['2017'] = pd.to_numeric(df3['2017'], errors='coerce')
df3['2018'] = pd.to_numeric(df3['2018'], errors='coerce')
df3['2019'] = pd.to_numeric(df3['2019'], errors='coerce')
df3['2020'] = pd.to_numeric(df3['2020'], errors='coerce')
df3['2021'] = pd.to_numeric(df3['2021'], errors='coerce')
df3.replace("..", np.nan, inplace=True)
df3['Product'] = df3['Product'].str.strip()
df3['Country'] = df3['Country'].str.strip()
df3['Subsector'] = df3['Subsector'].str.strip()

# 1.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Paper pulp and printing [ISIC 17-18] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Paper pulp and printing [ISIC 17-18]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Paper pulp and printing [ISIC 17-18]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Paper pulp and printing [ISIC 17-18]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 2.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Chemicals and chemical Products [ISIC 20-21] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Chemicals and chemical Products [ISIC 20-21]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Chemicals and chemical Products [ISIC 20-21]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Chemicals and chemical Products [ISIC 20-21]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 3.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Non-metallic minerals [ISIC 23] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Non-metallic minerals [ISIC 23]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Non-metallic minerals [ISIC 23]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Non-metallic minerals [ISIC 23]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 4.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Basic metals [ISIC 24] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Basic metals [ISIC 24]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Basic metals [ISIC 24]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Basic metals [ISIC 24]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 5.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Mining [ISIC 05-09] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Mining [ISIC 05-09]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Mining [ISIC 05-09]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Mining [ISIC 05-09]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)

# 6.Xử lý dữ liệu đối với hàng có giá trị Oil and oil products (PJ) trong cột Product và Construction [ISIC 41-43] trong cột Subsector nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = np.nanmean(df3.loc[
        (df3['Subsector'] == 'Construction [ISIC 41-43]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)])
    mean_year_rounded = round(mean_year, 2)

    df3.loc[(df3['Subsector'] == 'Construction [ISIC 41-43]') &
            (df3['Product'] == 'Total final energy use (PJ)') &
            (df3['Country'] != 'IEA Total'), str(year)] = df3.loc[
        (df3['Subsector'] == 'Construction [ISIC 41-43]') &
        (df3['Product'] == 'Total final energy use (PJ)') &
        (df3['Country'] != 'IEA Total'), str(year)].fillna(mean_year_rounded)
# HẾT SHEET 3 Industry - Energy...........................................
# Sheet 4 Transport - Energy có tên biến là df4

df4 = pd.read_excel("D:\DoAnTotNghiep\Data\IEA-EnergyEnd-usesandEfficiencyIndicatorsdatabase-HighlightsNovember2023.xlsb", sheet_name="Transport - Energy",  skiprows=1)
columns_df4 = df4.columns
columns_new_df4 = [str(col)[-4:] for col in columns_df4 if isinstance(col, int)]
df4.columns = columns_df4[:3].tolist() + columns_new_df4
df4['2000'] = pd.to_numeric(df4['2000'], errors='coerce')
df4['2005'] = pd.to_numeric(df4['2005'], errors='coerce')
df4['2010'] = pd.to_numeric(df4['2010'], errors='coerce')
df4['2015'] = pd.to_numeric(df4['2015'], errors='coerce')
df4['2016'] = pd.to_numeric(df4['2016'], errors='coerce')
df4['2017'] = pd.to_numeric(df4['2017'], errors='coerce')
df4['2018'] = pd.to_numeric(df4['2018'], errors='coerce')
df4['2019'] = pd.to_numeric(df4['2019'], errors='coerce')
df4['2020'] = pd.to_numeric(df4['2020'], errors='coerce')
df4['2021'] = pd.to_numeric(df4['2021'], errors='coerce')
df4.replace("..", np.nan, inplace=True)
df4['Product'] = df4['Product'].str.strip()
df4['Country'] = df4['Country'].str.strip()
df4['Mode/vehicle type'] = df4['Mode/vehicle type'].str.strip()

# 1.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Total passenger transport trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Total passenger transport') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Total passenger transport') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Total passenger transport') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 2.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Cars/light trucks trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Cars/light trucks') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Cars/light trucks') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Cars/light trucks') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 3.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Motorcycles trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Motorcycles') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Motorcycles') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Motorcycles') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 4.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Buses trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Buses') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Buses') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Buses') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 5.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Total freight transport trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Total freight transport') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Total freight transport') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Total freight transport') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 6.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Freight trucks trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Freight trucks') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Freight trucks') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Freight trucks') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 7.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Total airplanes trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Total airplanes') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Total airplanes') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Total airplanes') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)

# 8.Xử lý dữ liệu đối với hàng có giá trị Total final energy use (PJ) và Total ships trong cột Mode/vehicle type nhưng loại trừ giá trị IEA Total trong cột Country
for year in years:
    # Tính giá trị trung bình cho năm hiện tại
    mean_year = df4.loc[
        (df4['Mode/vehicle type'] == 'Total ships') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].mean().round(2)

    df4.loc[(df4['Mode/vehicle type'] == 'Total ships') &
            (df4['Product'] == 'Total final energy use (PJ)') &
            (df4['Country'] != 'IEA Total'), str(year)] = df4.loc[
        (df4['Mode/vehicle type'] == 'Total ships') &
        (df4['Product'] == 'Total final energy use (PJ)') &
        (df4['Country'] != 'IEA Total'), str(year)].fillna(mean_year)
# Hết sheet 4 Transport - Energy

# BIẾN ĐỔI CÁC DATA FRAME ĐỂ DÊ DÀNG THỰC HIỆN TRỰC QUAN HÓA DỮ LIỆU
# Sheet 1 Residential - Energy
df1_year = pd.melt(df1, id_vars=["Country", "End use", "Product"],
                   value_vars=["2000", "2005", "2010", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
                   var_name="Year", value_name="Value")

# Biến đổi dataframe df1_year để có các cột mới dựa trên giá trị trong cột "End use" và cột "Product"
df1_end_use = df1_year.pivot_table(index=["Country", "Year"], columns="End use", values="Value").reset_index()
df1_end_use = df1_end_use.drop(columns="Total Residential")
df1_product = df1_year.pivot_table(index=["Country", "Year"], columns="Product", values="Value").reset_index()
df1_product = df1_product.drop(columns="Total final energy use (PJ)")
# HẾT SHEET 1 Residential - Energy...........................................
# Sheet 2 Services - Energy
df2_year = pd.melt(df2, id_vars=["Country", "End use", "Product"],
                   value_vars=["2000", "2005", "2010", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
                   var_name="Year", value_name="Value")

# Biến đổi dataframe df2_year để có các cột mới dựa trên giá trị trong cột "End use" và cột "Product"
df2_end_use = df2_year.pivot_table(index=["Country", "Year"], columns="End use", values="Value").reset_index()
df2_end_use = df2_end_use.drop(columns="Total Services")
df2_product = df2_year.pivot_table(index=["Country", "Year"], columns="Product", values="Value").reset_index()
df2_product = df2_product.drop(columns="Total final energy use (PJ)")

# HẾT SHEET 2 Services - Energy...........................................
# Sheet 3 Industry - Energy
df3_year = pd.melt(df3, id_vars=["Country", "Subsector", "Product"],
                   value_vars=["2000", "2005", "2010", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
                   var_name="Year", value_name="Value")

# Biến đổi dataframe df3_year để có các cột mới dựa trên giá trị trong cột "Subsector" và cột "Product"
df3_subsector = df3_year.pivot_table(index=["Country", "Year"], columns="Subsector", values="Value").reset_index()
df3_subsector = df3_subsector.drop(columns="Manufacturing [ISIC 10-18; 20-32]")
df3_product = df3_year.pivot_table(index=["Country", "Year"], columns="Product", values="Value").reset_index()
df3_product = df3_product.drop(columns="Total final energy use (PJ)")

# HẾT SHEET 3 Industry - Energy...........................................
# Sheet 4 Transport - Energy
df4_year = pd.melt(df4, id_vars=["Country", "Mode/vehicle type", "Product"],
                   value_vars=["2000", "2005", "2010", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
                   var_name="Year", value_name="Value")

# Biến đổi dataframe df4_year để có các cột mới dựa trên giá trị trong cột "Mode/vehicle type" và cột "Product"
df4_mode_vehicle_type = df4_year.pivot_table(index=["Country", "Year"], columns="Mode/vehicle type", values="Value").reset_index()
df4_mode_vehicle_type = df4_mode_vehicle_type.drop(columns="Total passenger and freight transport")
df4_product = df4_year.pivot_table(index=["Country", "Year"], columns="Product", values="Value").reset_index()
df4_product = df4_product.drop(columns="Total final energy use (PJ)")
# Hết sheet 4 Transport - Energy



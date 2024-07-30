import mplcursors as mplcursors

from data_processing import df1_end_use, df1_product, df2_end_use, df2_product, df3_product, df3_subsector, df4_product, df4_mode_vehicle_type
from model import df1_end_use_forecast, df1_product_forecast, df2_end_use_forecast, df2_product_forecast, \
    df3_product_forecast, df3_subsector_forecast, df4_mode_vehicle_type_forecast, df4_product_forecast
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
def set_country_data(country_name, selected_sector, top_content_frame, bottom_content_frame, forecast=False,
                     combined=False):
    plt.close('all')
    # Xóa biểu đồ cũ (nếu có)
    for widget in top_content_frame.winfo_children():
        widget.destroy()
    for widget in bottom_content_frame.winfo_children():
        widget.destroy()

    if combined:
        if selected_sector == "Residential":
            if forecast:
                df_end_use = pd.concat(
                    [df1_end_use[df1_end_use["Country"] == country_name],
                     df1_end_use_forecast[df1_end_use_forecast["Country"] == country_name]])
                df_product = pd.concat(
                    [df1_product[df1_product["Country"] == country_name],
                     df1_product_forecast[df1_product_forecast["Country"] == country_name]])
                fig1, ax1 = plt.subplots()
                create_chart_combined(df_end_use, country_name, top_content_frame, fig1, ax1, "Residential Energy Use")
                fig2, ax2 = plt.subplots()
                create_chart_combined(df_product, country_name, bottom_content_frame, fig2, ax2,
                                     "Residential Energy Production")
            else:
                df_end_use = df1_end_use
                df_product = df1_product
                fig1, ax1 = plt.subplots()
                create_chart_residential(df_end_use, country_name, top_content_frame, fig1, ax1)
                fig2, ax2 = plt.subplots()
                create_chart_residential_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Services":
            if forecast:
                df_end_use = pd.concat(
                    [df2_end_use[df2_end_use["Country"] == country_name],
                     df2_end_use_forecast[df2_end_use_forecast["Country"] == country_name]])
                df_product = pd.concat(
                    [df2_product[df2_product["Country"] == country_name],
                     df2_product_forecast[df2_product_forecast["Country"] == country_name]])
                fig1, ax1 = plt.subplots()
                create_chart_combined(df_end_use, country_name, top_content_frame, fig1, ax1, "Services Energy Use")
                fig2, ax2 = plt.subplots()
                create_chart_combined(df_product, country_name, bottom_content_frame, fig2, ax2,
                                     "Services Energy Production")
            else:
                df_end_use = df2_end_use
                df_product = df2_product
                fig1, ax1 = plt.subplots()
                create_chart_services(df_end_use, country_name, top_content_frame, fig1, ax1)
                fig2, ax2 = plt.subplots()
                create_chart_services_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Industry":
            if forecast:
                df_subsector = pd.concat(
                    [df3_subsector[df3_subsector["Country"] == country_name],
                     df3_subsector_forecast[df3_subsector_forecast["Country"] == country_name]])
                df_product = pd.concat(
                    [df3_product[df3_product["Country"] == country_name],
                     df3_product_forecast[df3_product_forecast["Country"] == country_name]])
                fig1, ax1 = plt.subplots()
                create_chart_combined(df_subsector, country_name, top_content_frame, fig1, ax1, "Industry Energy Use")
                fig2, ax2 = plt.subplots()
                create_chart_combined(df_product, country_name, bottom_content_frame, fig2, ax2,
                                     "Industry Energy Production")
            else:
                df_subsector = df3_subsector
                df_product = df3_product
                fig1, ax1 = plt.subplots()
                create_chart_industry(df_subsector, country_name, top_content_frame, fig1, ax1)
                fig2, ax2 = plt.subplots()
                create_chart_industry_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Transport":
            if forecast:
                df_mode_vehicle_type = pd.concat(
                    [df4_mode_vehicle_type[df4_mode_vehicle_type["Country"] == country_name],
                     df4_mode_vehicle_type_forecast[df4_mode_vehicle_type_forecast["Country"] == country_name]])
                df_product = pd.concat(
                    [df4_product[df4_product["Country"] == country_name],
                     df4_product_forecast[df4_product_forecast["Country"] == country_name]])
                fig1, ax1 = plt.subplots()
                create_chart_combined(df_mode_vehicle_type, country_name, top_content_frame, fig1, ax1,
                                     "Transport Energy Use")
                fig2, ax2 = plt.subplots()
                create_chart_combined(df_product, country_name, bottom_content_frame, fig2, ax2,
                                     "Transport Energy Production")
            else:
                df_mode_vehicle_type = df4_mode_vehicle_type
                df_product = df4_product
                fig1, ax1 = plt.subplots()
                create_chart_transport(df_mode_vehicle_type, country_name, top_content_frame, fig1, ax1)
                fig2, ax2 = plt.subplots()
                create_chart_transport_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        else:
            print("Lĩnh vực không hợp lệ")
            return

    elif forecast:
        if selected_sector == "Residential":
            df_end_use = df1_end_use_forecast
            df_product = df1_product_forecast
            fig1, ax1 = plt.subplots()
            create_chart_residential_forecast(df_end_use, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_residential_product_forecast(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Services":
            df_end_use = df2_end_use_forecast
            df_product = df2_product_forecast
            fig1, ax1 = plt.subplots()
            create_chart_services_forecast(df_end_use, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_services_product_forecast(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Industry":
            df_subsector = df3_subsector_forecast
            df_product = df3_product_forecast
            fig1, ax1 = plt.subplots()
            create_chart_industry_forecast(df_subsector, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_industry_product_forecast(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Transport":
            df_mode_vehicle_type = df4_mode_vehicle_type_forecast
            df_product = df4_product_forecast
            fig1, ax1 = plt.subplots()
            create_chart_transport_forecast(df_mode_vehicle_type, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_transport_product_forecast(df_product, country_name, bottom_content_frame, fig2, ax2)
        else:
            print("Lĩnh vực không hợp lệ")
            return
    else:
        if selected_sector == "Residential":
            df_end_use = df1_end_use
            df_product = df1_product
            fig1, ax1 = plt.subplots()
            create_chart_residential(df_end_use, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_residential_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Services":
            df_end_use = df2_end_use
            df_product = df2_product
            fig1, ax1 = plt.subplots()
            create_chart_services(df_end_use, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_services_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Industry":
            df_subsector = df3_subsector
            df_product = df3_product
            fig1, ax1 = plt.subplots()
            create_chart_industry(df_subsector, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_industry_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        elif selected_sector == "Transport":
            df_mode_vehicle_type = df4_mode_vehicle_type
            df_product = df4_product
            fig1, ax1 = plt.subplots()
            create_chart_transport(df_mode_vehicle_type, country_name, top_content_frame, fig1, ax1)
            fig2, ax2 = plt.subplots()
            create_chart_transport_product(df_product, country_name, bottom_content_frame, fig2, ax2)
        else:
            print("Lĩnh vực không hợp lệ")
            return

def create_chart_residential(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Residential appliances', 'Residential cooking',
       'Residential lighting', 'Residential space cooling',
       'Residential space heating', 'Residential water heating'], kind='bar', ax=ax)
    ax.set_title(f"Residential Energy Use in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def create_chart_services(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Services lighting', 'Services space cooling',
       'Services space heating'], kind='bar', ax=ax)
    ax.set_title(f"Services Energy Use in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def create_chart_industry(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Agriculture forestry fishing [ISIC 01-03]',
       'Basic metals [ISIC 24]',
       'Chemicals and chemical Products [ISIC 20-21]',
       'Construction [ISIC 41-43]', 'Mining [ISIC 05-09]',
       'Non-metallic minerals [ISIC 23]',
       'Paper pulp and printing [ISIC 17-18]'], kind='bar', ax=ax)
    ax.set_title(f"Industry Energy Use in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def create_chart_transport(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Buses', 'Cars/light trucks', 'Freight trucks',
       'Motorcycles', 'Total airplanes', 'Total freight transport',
       'Total passenger transport', 'Total road', 'Total ships',
       'Total trains'], kind='bar', ax=ax)
    ax.set_title(f"Transport Energy Use in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df1_product (Residential)
def create_chart_residential_product(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Residential Energy Production in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df2_product (Services)
def create_chart_services_product(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Services Energy Production in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df3_product (Industry)
def create_chart_industry_product(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Industry Energy Production in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df4_product (Transport)
def create_chart_transport_product(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Coal and coal products (PJ)', 'Diesel and light fuel oil (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heavy fuel oil (PJ)',
                                   'Jet fuel and aviation gasoline (PJ)', 'LPG (PJ)',
                                   'Motor gasoline (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Transport Energy Production in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ------------------------DỰ ĐOÁN -------------------------------

# Hàm vẽ biểu đồ cho df1_end_use_forecast (Residential)
def create_chart_residential_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Residential appliances', 'Residential cooking',
       'Residential lighting', 'Residential space cooling',
       'Residential space heating', 'Residential water heating'], kind='bar', ax=ax)
    ax.set_title(f"Residential Energy Use Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df1_product_forecast (Residential)
def create_chart_residential_product_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Residential Energy Production Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df2_end_use_forecast (Services)
def create_chart_services_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Services lighting', 'Services space cooling',
       'Services space heating'], kind='bar', ax=ax)
    ax.set_title(f"Services Energy Use Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df2_product_forecast (Services)
def create_chart_services_product_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Services Energy Production Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df3_subsector_forecast (Industry)
def create_chart_industry_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Agriculture forestry fishing [ISIC 01-03]',
       'Basic metals [ISIC 24]',
       'Chemicals and chemical Products [ISIC 20-21]',
       'Construction [ISIC 41-43]', 'Mining [ISIC 05-09]',
       'Non-metallic minerals [ISIC 23]',
       'Paper pulp and printing [ISIC 17-18]'], kind='bar', ax=ax)
    ax.set_title(f"Industry Energy Use Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df3_product_forecast (Industry)
def create_chart_industry_product_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                                   'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Industry Energy Production Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df4_mode_vehicle_type_forecast (Transport)
def create_chart_transport_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Buses', 'Cars/light trucks', 'Freight trucks',
       'Motorcycles', 'Total airplanes', 'Total freight transport',
       'Total passenger transport', 'Total road', 'Total ships',
       'Total trains'], kind='bar', ax=ax)
    ax.set_title(f"Transport Energy Use Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ cho df4_product_forecast (Transport)
def create_chart_transport_product_forecast(data, country_name, frame, fig, ax):
    ax.clear()
    country_data = data[data["Country"] == country_name]
    country_data.plot(x='Year', y=['Coal and coal products (PJ)', 'Diesel and light fuel oil (PJ)',
                                   'Electricity (PJ)', 'Gas (PJ)', 'Heavy fuel oil (PJ)',
                                   'Jet fuel and aviation gasoline (PJ)', 'LPG (PJ)',
                                   'Motor gasoline (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    ax.set_title(f"Transport Energy Production Forecast in {country_name}")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Hàm vẽ biểu đồ tổng hợp
def create_chart_combined(data, country_name, frame, fig, ax, title):
    ax.clear()

    if title == "Residential Energy Use":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year', y=['Residential appliances', 'Residential cooking',
                                        'Residential lighting', 'Residential space cooling',
                                        'Residential space heating', 'Residential water heating'], kind='bar', ax=ax)
    elif title == "Residential Energy Production":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year',
                         y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                            'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                            'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    elif title == "Services Energy Use":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year', y=['Services lighting', 'Services space cooling',
                                        'Services space heating'], kind='bar', ax=ax)
    elif title == "Services Energy Production":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year',
                         y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                            'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                            'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    elif title == "Industry Energy Use":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year', y=['Agriculture forestry fishing [ISIC 01-03]',
                                        'Basic metals [ISIC 24]',
                                        'Chemicals and chemical Products [ISIC 20-21]',
                                        'Construction [ISIC 41-43]', 'Mining [ISIC 05-09]',
                                        'Non-metallic minerals [ISIC 23]',
                                        'Paper pulp and printing [ISIC 17-18]'], kind='bar', ax=ax)
    elif title == "Industry Energy Production":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year',
                         y=['Biofuels and waste (PJ)', 'Coal and coal products (PJ)',
                            'Electricity (PJ)', 'Gas (PJ)', 'Heat (PJ)',
                            'Oil and oil products (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    elif title == "Transport Energy Use":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year', y=['Buses', 'Cars/light trucks', 'Freight trucks',
                                        'Motorcycles', 'Total airplanes', 'Total freight transport',
                                        'Total passenger transport', 'Total road', 'Total ships',
                                        'Total trains'], kind='bar', ax=ax)
    elif title == "Transport Energy Production":
        country_data = data[data["Country"] == country_name]
        country_data.plot(x='Year', y=['Coal and coal products (PJ)', 'Diesel and light fuel oil (PJ)',
                                        'Electricity (PJ)', 'Gas (PJ)', 'Heavy fuel oil (PJ)',
                                        'Jet fuel and aviation gasoline (PJ)', 'LPG (PJ)',
                                        'Motor gasoline (PJ)', 'Other sources (PJ)'], kind='bar', ax=ax)
    else:
        print("Tiêu đề không hợp lệ")
        return

    ax.set_title(f"{title} in {country_name} (Combined)")
    plt.xticks(rotation=0, ha='center')
    mplcursors.cursor(ax, hover=True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


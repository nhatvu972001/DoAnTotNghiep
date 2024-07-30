from data_processing import df1_end_use, df1_product, df2_end_use, df2_product, df3_product, df3_subsector, df4_product, \
    df4_mode_vehicle_type, df1, df2, df3, df4
from model import df1_end_use_forecast, df1_product_forecast, df2_end_use_forecast, df2_product_forecast, \
    df3_product_forecast, df3_subsector_forecast, df4_mode_vehicle_type_forecast, df4_product_forecast
from visualization import set_country_data
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser

def show_energy_usage():
    global usage_frame
    hide_all_frames()
    usage_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def show_energy_forecast():
    global forecast_frame
    hide_all_frames()
    forecast_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def show_combined_data():
    global combined_frame
    hide_all_frames()
    combined_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def hide_all_frames():
    if usage_frame:
        usage_frame.pack_forget()
    if forecast_frame:
        forecast_frame.pack_forget()
    if combined_frame:
        combined_frame.pack_forget()


# Hàm tạo nút với icon
def create_icon_button(parent, text, icon_path, command):
    icon = Image.open(icon_path)
    icon = icon.resize((20, 20))  # Thay đổi kích thước icon nếu cần
    photo = ImageTk.PhotoImage(icon)
    button = tk.Button(parent, text=text, image=photo, compound=tk.LEFT, command=command)
    button.image = photo  # Lưu trữ image để tránh bị garbage collected
    return button


def show_countries(df, sector, residential_btn, service_btn, industrial_btn, transport_btn):
    global usage_frame, selected_sector, sector_label, country_frame, top_content_frame, bottom_content_frame

    # Xóa các widget cũ (nếu có)
    for widget in usage_frame.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [residential_btn, service_btn, industrial_btn,
                                                           transport_btn, sector_label]:
            widget.destroy()
    if country_frame:
        country_frame.destroy()

    # Cập nhật hoặc tạo label hiển thị lĩnh vực
    if sector_label:
        sector_label.config(text=sector)
    else:
        sector_label = tk.Label(usage_frame, text=sector, font=("Arial", 16, "bold"), bg="#A0E3F2")
        sector_label.grid(row=5, column=0, columnspan=2, pady=5)

    # Lưu trữ thông tin lĩnh vực
    selected_sector = sector

    # Tạo frame con cho các nút quốc gia
    country_frame = tk.Frame(usage_frame, bd=2, relief=tk.GROOVE)
    country_frame.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

    country_frame.grid_columnconfigure(0, weight=1)
    country_frame.grid_columnconfigure(1, weight=1)
    country_frame.grid_columnconfigure(2, weight=1)

    # Tạo nút cho mỗi quốc gia
    countries = df["Country"].unique()
    col = 0
    row = 0
    for country in countries:
        country_btn = tk.Button(country_frame, text=country, bd=0, bg="#A0E3F2", font=("Arial", 10),
                                command=lambda c=country: set_country_data(c, selected_sector, top_content_frame,
                                                                           bottom_content_frame))
        country_btn.grid(row=row, column=col, sticky="ew", padx=4, pady=4)
        col += 1
        if col == 3:
            col = 0
            row += 1


def show_countries_forecast(df, sector, residential_forecast_btn, service_forecast_btn, industrial_forecast_btn,
                            transport_forecast_btn):
    global forecast_frame, selected_sector, forecast_sector_label, country_frame, top_content_frame, bottom_content_frame

    # Xóa các widget cũ (nếu có) trong forecast_frame
    for widget in forecast_frame.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [residential_forecast_btn, service_forecast_btn,
                                                           industrial_forecast_btn, transport_forecast_btn,
                                                           forecast_sector_label]:
            widget.destroy()
    if country_frame:
        country_frame.destroy()

    # Cập nhật hoặc tạo label hiển thị lĩnh vực trong forecast_frame
    if forecast_sector_label:
        forecast_sector_label.config(text=sector + " Forecast")
    else:
        forecast_sector_label = tk.Label(forecast_frame, text=sector + " Forecast", font=("Arial", 16, "bold"),
                                         bg="#A0E3F2")
        forecast_sector_label.grid(row=5, column=0, columnspan=2, pady=5)

    # Lưu trữ thông tin lĩnh vực
    selected_sector = sector

    # Tạo frame con cho các nút quốc gia trong forecast_frame
    country_frame = tk.Frame(forecast_frame, bd=2, relief=tk.GROOVE)
    country_frame.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

    country_frame.grid_columnconfigure(0, weight=1)
    country_frame.grid_columnconfigure(1, weight=1)
    country_frame.grid_columnconfigure(2, weight=1)

    # Tạo nút cho mỗi quốc gia trong forecast_frame
    countries = df["Country"].unique()
    col = 0
    row = 0
    for country in countries:
        country_btn = tk.Button(country_frame, text=country, bd=0, bg="#A0E3F2", font=("Arial", 10),
                                command=lambda c=country: set_country_data(c, selected_sector, top_content_frame,
                                                                           bottom_content_frame, forecast=True))
        country_btn.grid(row=row, column=col, sticky="ew", padx=4, pady=4)
        col += 1
        if col == 3:
            col = 0
            row += 1


def show_countries_combined(df, sector, residential_combined_btn, service_combined_btn, industrial_combined_btn,
                            transport_combined_btn):
    global combined_frame, selected_sector, combined_sector_label, country_frame, top_content_frame, bottom_content_frame

    for widget in combined_frame.winfo_children():
        if isinstance(widget, tk.Button) and widget not in [residential_combined_btn, service_combined_btn,
                                                           industrial_combined_btn, transport_combined_btn,
                                                           combined_sector_label]:
            widget.destroy()
    if country_frame:
        country_frame.destroy()

    if combined_sector_label:
        combined_sector_label.config(text=sector + " Combined")
    else:
        combined_sector_label = tk.Label(combined_frame, text=sector + " Combined", font=("Arial", 16, "bold"),
                                         bg="#A0E3F2")
        combined_sector_label.grid(row=5, column=0, columnspan=2, pady=5)

    selected_sector = sector

    country_frame = tk.Frame(combined_frame, bd=2, relief=tk.GROOVE)
    country_frame.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

    country_frame.grid_columnconfigure(0, weight=1)
    country_frame.grid_columnconfigure(1, weight=1)
    country_frame.grid_columnconfigure(2, weight=1)

    countries = df["Country"].unique()
    col = 0
    row = 0
    for country in countries:
        country_btn = tk.Button(country_frame, text=country, bd=0, bg="#A0E3F2", font=("Arial", 10),
                                command=lambda c=country: set_country_data(c, selected_sector, top_content_frame,
                                                                           bottom_content_frame, combined=True, forecast=True))
        country_btn.grid(row=row, column=col, sticky="ew", padx=4, pady=4)
        col += 1
        if col == 3:
            col = 0
            row += 1


def main():
    global root, usage_frame, forecast_frame, combined_frame, \
        sector_label, forecast_sector_label, combined_sector_label, selected_sector, \
        country_frame, forecast_country_frame, \
        top_content_frame, bottom_content_frame

    sector_label = None
    forecast_sector_label = None
    combined_sector_label = None
    country_frame = None
    forecast_country_frame = None
    root = tk.Tk()
    root.title("Dự báo tình hình sử dụng năng lượng")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    menu_frame = tk.Frame(root, bg="#17C3B2")
    menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

    border_frame = tk.Frame(menu_frame, bg="black", width=3)
    border_frame.pack(side="right", fill="y")

    title_label = tk.Label(menu_frame, text="MENU", font=("Arial", 24, "bold"), fg="black", bg="#17C3B2")
    title_label.pack(pady=20)

    # Tạo nút menu với icon
    menu_items = [
        ("ENERGY USE", "../Assets/lighting.png", show_energy_usage),
        ("FORECAST ENERGY USE", "../Assets/forecast.png", show_energy_forecast),
        ("COMBINED DATA", "../Assets/combine.png", show_combined_data)
    ]
    for text, icon_path, command in menu_items:
        menu_button = create_icon_button(menu_frame, text, icon_path, command)
        # menu_button.config(font=("Arial", 16, "bold"), pady=5)
        menu_button.pack(fill=tk.X, pady=20)

    # Tạo Frame cho nội dung bên phải
    energy_frame = tk.Frame(root)
    energy_frame.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)

    usage_frame = tk.Frame(energy_frame, bd=0, relief=tk.RAISED, bg="#A0E3F2")

    usage_frame.grid_columnconfigure(0, weight=1)
    usage_frame.grid_columnconfigure(1, weight=1)
    title_label_usage_frame = tk.Label(usage_frame, text="ENERGY USE", font=("Arial", 20, "bold"), fg="black",
                                       bg="#A0E3F2")
    title_label_usage_frame.grid(row=0, column=0, columnspan=2, pady=27)

    # Tạo nút lĩnh vực với icon
    residential_btn = create_icon_button(usage_frame, "Residential", "../Assets/residential.png",
                                        lambda: show_countries(df1_product, "Residential", residential_btn,
                                                              service_btn, industrial_btn, transport_btn))
    residential_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    service_btn = create_icon_button(usage_frame, "Services", "../Assets/services.png",
                                      lambda: show_countries(df2_product, "Services", residential_btn, service_btn,
                                                             industrial_btn, transport_btn))
    service_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    industrial_btn = create_icon_button(usage_frame, "Industry", "../Assets/industry.jpg",
                                         lambda: show_countries(df3_subsector, "Industry", residential_btn,
                                                                service_btn, industrial_btn, transport_btn))
    industrial_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    transport_btn = create_icon_button(usage_frame, "Transport", "../Assets/transport.png",
                                        lambda: show_countries(df4_mode_vehicle_type, "Transport", residential_btn,
                                                              service_btn, industrial_btn, transport_btn))
    transport_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    forecast_frame = tk.Frame(energy_frame, bd=0, relief=tk.RAISED, bg="#A0E3F2")
    forecast_frame.grid_columnconfigure(0, weight=1)
    forecast_frame.grid_columnconfigure(1, weight=1)

    title_label_usage_frame = tk.Label(forecast_frame, text="ENERGY FORECAST", font=("Arial", 20, "bold"), fg="black",
                                       bg="#A0E3F2")
    title_label_usage_frame.grid(row=0, column=0, columnspan=2, pady=27)

    # Tạo nút lĩnh vực forecast với icon
    residential_forecast_btn = create_icon_button(forecast_frame, "Residential", "../Assets/residential.png",
                                                  lambda: show_countries_forecast(df1_end_use_forecast, "Residential",
                                                                                   residential_forecast_btn,
                                                                                   service_forecast_btn,
                                                                                   industrial_forecast_btn,
                                                                                   transport_forecast_btn))
    residential_forecast_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    service_forecast_btn = create_icon_button(forecast_frame, "Services", "../Assets/services.png",
                                              lambda: show_countries_forecast(df2_end_use_forecast, "Services",
                                                                               residential_forecast_btn,
                                                                               service_forecast_btn,
                                                                               industrial_forecast_btn,
                                                                               transport_forecast_btn))
    service_forecast_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    industrial_forecast_btn = create_icon_button(forecast_frame, "Industry", "../Assets/industry.jpg",
                                                 lambda: show_countries_forecast(df3_subsector_forecast, "Industry",
                                                                                  residential_forecast_btn,
                                                                                  service_forecast_btn,
                                                                                  industrial_forecast_btn,
                                                                                  transport_forecast_btn))
    industrial_forecast_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    transport_forecast_btn = create_icon_button(forecast_frame, "Transport", "../Assets/transport.png",
                                                  lambda: show_countries_forecast(df4_mode_vehicle_type_forecast,
                                                                                   "Transport",
                                                                                   residential_forecast_btn,
                                                                                   service_forecast_btn,
                                                                                   industrial_forecast_btn,
                                                                                   transport_forecast_btn))
    transport_forecast_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    combined_frame = tk.Frame(energy_frame, bd=0, relief=tk.RAISED, bg="#A0E3F2")
    combined_frame.grid_columnconfigure(0, weight=1)
    combined_frame.grid_columnconfigure(1, weight=1)
    title_label_combined_frame = tk.Label(combined_frame, text="ENERGY COMBINED", font=("Arial", 20, "bold"),
                                          fg="black",
                                          bg="#A0E3F2")
    title_label_combined_frame.grid(row=0, column=0, columnspan=2, pady=27)

    # Tạo nút lĩnh vực combined với icon
    residential_combined_btn = create_icon_button(combined_frame, "Residential", "../Assets/residential.png",
                                                  lambda: show_countries_combined(df1_end_use, "Residential",
                                                                                  residential_combined_btn,
                                                                                  service_combined_btn,
                                                                                  industrial_combined_btn,
                                                                                  transport_combined_btn))
    residential_combined_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    service_combined_btn = create_icon_button(combined_frame, "Services", "../Assets/services.png",
                                              lambda: show_countries_combined(df2_end_use, "Services",
                                                                              residential_combined_btn,
                                                                              service_combined_btn,
                                                                              industrial_combined_btn,
                                                                              transport_combined_btn))
    service_combined_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    industrial_combined_btn = create_icon_button(combined_frame, "Industry", "../Assets/industry.jpg",
                                                 lambda: show_countries_combined(df3_subsector, "Industry",
                                                                                  residential_combined_btn,
                                                                                  service_combined_btn,
                                                                                  industrial_combined_btn,
                                                                                  transport_combined_btn))
    industrial_combined_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    transport_combined_btn = create_icon_button(combined_frame, "Transport", "../Assets/transport.png",
                                                  lambda: show_countries_combined(df4_mode_vehicle_type,
                                                                                   "Transport",
                                                                                   residential_combined_btn,
                                                                                   service_combined_btn,
                                                                                   industrial_combined_btn,
                                                                                   transport_combined_btn))
    transport_combined_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=9, sticky="ew")

    # Tạo Frame cho nội dung chính (biểu đồ)
    content_frame = tk.Frame(root, relief=tk.GROOVE)
    content_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)

    top_content_frame = tk.Frame(content_frame)
    top_content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    bottom_content_frame = tk.Frame(content_frame)
    bottom_content_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Tạo frame cho các icon liên hệ
    contact_frame = tk.Frame(menu_frame, bg="#17C3B2")
    contact_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

    # Tạo icon liên hệ với icon
    contact_items = [
        ("Facebook", "../Assets/facebook.jpg", "https://www.facebook.com/nhvu0907/"),
        ("IEA", "../Assets/iea.png", "https://www.iea.org/"),
        ("Github", "../Assets/github.png", "https://github.com/nhatvu972001/"),
        ("HCMUNRE", "../Assets/hcmunre.png", "https://hcmunre.edu.vn/")
    ]
    for text, icon_path, link in contact_items:
        contact_button = create_icon_button(contact_frame, text, icon_path,
                                            lambda l=link: webbrowser.open_new_tab(l))
        contact_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
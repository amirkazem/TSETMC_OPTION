
# بسته اختیارات خرید و فروش بورس تهران
# TSETMC_OPTION
Version1
Tehran Stock Exchange Trading Options Package
This package provides an API and a web interface (using Flask) for interacting with Tehran Stock Exchange (TSE) trading options data, including buy and sell permissions. It allows you to fetch, analyze, and visualize stock market data programmatically or through a user-friendly web interface.
        
Features:
    **Tehran Stock Exchange (TSE) Trading Options API: Access buy/sell options data via a RESTful API.
    **Web Interface: A Flask-based web application that dynamically displays trading options data in a table format, with search and export features.
    **Real-Time Data Updates: The API fetches real-time data, updating every 5 seconds for accuracy.
    **Excel Export: Export the trading data tables to Excel for further analysis.
Setup Instructions:
Prerequisites:
Create a Virtual Environment:
        
    In your terminal, navigate to the project directory and run:
        python -m venv venv

Activate the Virtual Environment:
    On Windows:
    venv\Scripts\activate
    On macOS/Linux:
     source venv/bin/activate
     
Install Dependencies:
    pip install -r requirements.txt

Running the Flask Web Application:
  After activating the virtual environment and installing dependencies, start the Flask application by running:
    flask run
  The web application will be accessible at http://127.0.0.1:5000/ in your browser, where you can interact with the dynamic tables and visualize the data.
        ![image](https://github.com/user-attachments/assets/80c8c6be-b3d5-40e9-9402-a14d63e59de4)
Using the API:
To use the API directly, you can make HTTP requests to the following endpoints:

  GET /api/data_call: Fetch call option data.
  GET /api/data_put: Fetch put option data.

 ![image](https://github.com/user-attachments/assets/e1d36106-28f7-42b5-a3a7-f01e1f005642)



#بسته اختیارات خرید و فروش بورس تهران
ا        ین بسته یک API و یک رابط وب (با استفاده از Flask) برای تعامل با داده‌های اختیارات خرید و فروش بورس تهران (TSE) فراهم می‌کند. این امکان را به شما می‌دهد که داده‌های بازار بورس را به‌طور برنامه‌نویسی یا از طریق یک رابط کاربری ساده مشاهده و تحلیل کنید.

ویژگی‌ها:
        API اختیارات خرید و فروش بورس تهران (TSE): دسترسی به داده‌های اختیارات خرید/فروش از طریق یک API RESTful.
        رابط وب: یک اپلیکیشن وب مبتنی بر Flask که داده‌های اختیارات خرید و فروش بورس تهران را به‌طور دینامیک در قالب جدول نمایش می‌دهد، همراه با قابلیت جستجو و امکان  داده‌ها به Excel.
        بروزرسانی داده‌ها به‌صورت بلادرنگ: API داده‌ها را به‌صورت بلادرنگ دریافت می‌کند و هر ۵ ثانیه یکبار بروزرسانی می‌شود.
        Excel: امکان صادرات جداول داده‌های بورس به فرمت Excel برای تحلیل‌های بیشتر.

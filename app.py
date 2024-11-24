from flask import Flask, jsonify, render_template
import pandas as pd
from CaptureData import capture_option_data

app = Flask(__name__)


# API ها برای ارائه داده‌ها
@app.route('/api/data_call')
def get_data_call():
    call_option_df, put_option_df, df_final_data = capture_option_data(sleep_time=1.5)


    for col1 in list(call_option_df.columns):
        call_option_df.loc[:, col1] = call_option_df[col1].astype(str).map(lambda x: str(x))
    return jsonify({"data": call_option_df.to_dict(orient="records")})


@app.route('/api/data_put')
def get_data_put():
    call_option_df, put_option_df, df_final_data = capture_option_data(sleep_time=1.5)
    for col1 in list(call_option_df.columns):
        put_option_df.loc[:, col1] = put_option_df[col1].astype(str).map(lambda x: str(x))
    return jsonify({"data": put_option_df.to_dict(orient="records")})


# صفحه اصلی
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

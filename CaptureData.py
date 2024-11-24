import pandas as pd
import requests
from fake_useragent import UserAgent
from time import sleep
import jdatetime as jd
import datetime as dt

col_rename_TSETMC=pd.read_excel('DATA_SOURCE/columns_data_name.xlsx')

def col_rename_function2(col_rename_TSETMC):
    index_to_type = dict(zip(col_rename_TSETMC['index'], col_rename_TSETMC.type))
    index_to_BULK_DATA_COLUMN_NAMES = dict(zip(col_rename_TSETMC['index'], col_rename_TSETMC.BULK_DATA_COLUMN_NAMES))
    index_to_SYMBOL_INFO_COLUMN_NAMES = dict(zip(col_rename_TSETMC['index'], col_rename_TSETMC.SYMBOL_INFO_COLUMN_NAMES))
    index_to_persian_col_name = dict(zip(col_rename_TSETMC['index'], col_rename_TSETMC.persian_col_name))


    return {
        'index_to_type':index_to_type,
        'index_to_BULK_DATA_COLUMN_NAMES': index_to_BULK_DATA_COLUMN_NAMES,
        'index_to_SYMBOL_INFO_COLUMN_NAMES': index_to_SYMBOL_INFO_COLUMN_NAMES,
        'index_to_persian_col_name': index_to_persian_col_name,

    }


def capture_option_data(sleep_time=1.5):
    sleep(sleep_time)
    col_rename=col_rename_function2(col_rename_TSETMC=col_rename_TSETMC)

    fake_user_agent = UserAgent()
    dict_data_source={
        "bourse": 1,
        "fara_bourse": 2
    }
    dict_final_data={
    "bourse": pd.DataFrame(),
    "fara_bourse": pd.DataFrame()
    }
    df_final_data=pd.DataFrame()
    for k,v in dict_data_source.items():
        url = f"https://cdn.tsetmc.com/api/Instrument/GetInstrumentOptionMarketWatch/{v}"
        headers = {'User-Agent': fake_user_agent.random}
        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
            final_response=pd.DataFrame(response.json()['instrumentOptMarketWatch'])

            for col1 in list(final_response.columns):
                try:
                    type_1=col_rename['index_to_type'][col1]
                    final_response.loc[:, col1] = final_response[col1].astype(type_1)

                except:
                    pass
            dict_final_data[k]=final_response

        except Exception as e:
            print(f"{e}")
            raise

    for k, v in dict_final_data.items():
        data=v.assign(Bazar=k)
        df_final_data=pd.concat([df_final_data,data])


    call_options_col = [column for column in df_final_data.columns if  (not column.endswith("_P"))]
    put_option_col = [column for column in df_final_data.columns if  (not column.endswith("_C"))]
    call_option_df=df_final_data.loc[:,call_options_col]
    put_option_df=df_final_data.loc[:,put_option_col]

    call_option_df.columns = [column.replace("_C", "") if  (column.endswith("_C")) else column for column in call_option_df.columns]
    put_option_df.columns = [column.replace("_P", "") if  (column.endswith("_P")) else column for column in put_option_df.columns]
    download_datetime_jalali=jd.datetime.now().__str__()
    download_datetime_miladi=dt.datetime.now().__str__()
    call_option_df=call_option_df.assign(download_datetime_jalali=download_datetime_jalali,
                                         download_datetime_miladi=download_datetime_miladi)
    put_option_df = put_option_df.assign(download_datetime_jalali=download_datetime_jalali,
                                           download_datetime_miladi=download_datetime_miladi)

    df_final_data = df_final_data.assign(download_datetime_jalali=download_datetime_jalali,
                                           download_datetime_miladi=download_datetime_miladi)

    return call_option_df,put_option_df,df_final_data



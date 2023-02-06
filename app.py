import psutil
import os
import pandas as pd
import random
import time

df = pd.DataFrame(data={
        "process": [],
        "cpu_per": [],
        "ram_per": [],
        "ram_total_GB": [],
    })


def measure():
    current_date = time.localtime()
    current_time = time.strftime("%H:%M:%S", time.localtime())
    stats = {
        "process": os.getpid(),
        "cpu_per": int(psutil.cpu_percent()),
        "ram_per": psutil.virtual_memory().percent,
        "ram_total_GB": round(psutil.virtual_memory().total / 1073741824, 2),
        "random": random.randrange(10000),
        "year": current_date.tm_year,
        "month": current_date.tm_mon,
        "day": current_date.tm_mday,
        "time": f"{current_time}"
    }
    return stats


def write_data(stats):
    global df
    df = df.append(stats, ignore_index=True)
    return df


def write_to_file(dataframe):
    c_date = time.localtime()
    file_name = f"machine-id_{c_date.tm_year}_{c_date.tm_mon}_{c_date.tm_mday}_{c_date.tm_hour}_{c_date.tm_min}.csv"

    dataframe.to_csv(file_name)


if __name__ == "__main__":
    i = 0
    while i < 20:
        write_data(measure())
        # time.sleep(random.randint(1, 3))
        i += 1
    write_to_file(df)
    print(df)

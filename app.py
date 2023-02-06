import psutil
import os


def measure():
    stats = {
        "process": os.getpid(),
        "cpu_per": int(psutil.cpu_percent()),
        "ram_per": psutil.virtual_memory().percent,
        "ram_total_GB": round(psutil.virtual_memory().total / 1073741824, 2),
    }
    return stats


if __name__ == "__main__":
    print(measure())

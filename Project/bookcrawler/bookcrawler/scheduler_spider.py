from apscheduler.schedulers.background import BackgroundScheduler
import os
import time
import datetime


def task_book_spider():
    """
    网站初始url
    :return:
    """
    # 你的spider启动命令
    current_path = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_path, 'generate_start_url.py')
    print(target_path)
    os.system(f'python {target_path}')

if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    # 每天9点添加初始url
    scheduler.add_job(task_book_spider, 'cron', hour=9, minute=0)

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
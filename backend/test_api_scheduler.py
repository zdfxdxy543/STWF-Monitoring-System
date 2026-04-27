import requests
import time
import schedule

API_URL = "http://localhost:8000/api/test/write"

def call_test_api():
    """调用测试API"""
    try:
        response = requests.post(API_URL, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] API调用成功: {data.get('message', 'OK')}")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] API调用失败: HTTP {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 连接失败: 无法连接到后端服务，请确保后端正在运行")
    except requests.exceptions.Timeout:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 请求超时")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 错误: {e}")

def main():
    print("=" * 50)
    print("定时测试API调用程序")
    print("=" * 50)
    print(f"API地址: {API_URL}")
    print("调用间隔: 每1分钟")
    print("按 Ctrl+C 停止程序")
    print("=" * 50)

    schedule.every(1).minutes.do(call_test_api)

    call_test_api()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

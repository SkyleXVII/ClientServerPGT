import uvicorn
from fastapi import FastAPI
from admin_gui import start_gui
from threading import Thread

app = FastAPI(title="Price GameTracker API")

@app.on_event("startup")
async def startup():
    # Инициализация подключений к БД и сервисов
    pass

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    try:
        from admin_gui import start_gui
        # Запуск API в отдельном потоке
        api_thread = Thread(target=run_api, daemon=True)
        api_thread.start()
        
        # Запуск GUI
        start_gui()
    except ImportError as e:
        print(f"GUI module not found: {e}")
        # Если GUI не доступен, просто запускаем API
        run_api()
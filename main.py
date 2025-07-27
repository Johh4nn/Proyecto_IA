import multiprocessing
import os

def run_backend():
    print("[INFO] Iniciando backend Flask...")
    os.system("python data/model/backend/api.py")
    print("[INFO] Backend Flask finalizado.")

def run_frontend():
    print("[INFO] Iniciando frontend Flask...")
    os.system("python data/model/frontend/app.py")
    print("[INFO] Frontend Flask finalizado.")
    print("[INFO] Accede al frontend en: http://localhost:5000")

if __name__ == "__main__":
    print("[MAIN] Lanzando procesos...")

    # Crear procesos paralelos para backend y frontend
    p1 = multiprocessing.Process(target=run_backend)
    p2 = multiprocessing.Process(target=run_frontend)

    p1.start()
    p2.start()

    print("[MAIN] Procesos iniciados. Esperando que terminen...")

    p1.join()
    p2.join()

    print("[MAIN] Ambos procesos han finalizado.")

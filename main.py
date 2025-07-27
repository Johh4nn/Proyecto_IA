import multiprocessing
import os

#ejecuta el archivo api.py
def run_backend():
    print("[INFO] Iniciando backend Flask...")
    os.system("python data/model/backend/api.py")
    print("[INFO] Backend Flask finalizado.")

# ejecuta el archivo app.py de Gradio
def run_frontend():
    print("[INFO] Iniciando frontend Gradio...")
    os.system("python frontend/app.py")
    print("[INFO] Frontend Gradio finalizado.")

if __name__ == "__main__":
    print("[MAIN] Lanzando procesos...")

    p1 = multiprocessing.Process(target=run_backend)
    p2 = multiprocessing.Process(target=run_frontend)

    p1.start()
    p2.start()

    print("[MAIN] Procesos iniciados. Esperando que terminen...")

    p1.join()
    p2.join()

    print("[MAIN] Ambos procesos han finalizado.")


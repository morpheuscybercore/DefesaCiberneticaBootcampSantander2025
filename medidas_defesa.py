# medidas_defesa.py
import os
import psutil
import time

class SecurityMeasures:
    @staticmethod
    def detect_suspicious_processes():
        """Detecta processos suspeitos"""
        suspicious_keywords = ['keylogger', 'ransom', 'crypto', 'stealer']
        print("🔍 Procurando processos suspeitos...")
        
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                proc_name = proc.info['name'].lower()
                for keyword in suspicious_keywords:
                    if keyword in proc_name:
                        print(f"🚨 Processo suspeito: {proc.info['name']} (PID: {proc.info['pid']})")
            except:
                pass
    
    @staticmethod
    def monitor_file_changes(directory="."):
        """Monitora mudanças em arquivos"""
        print(f"👀 Monitorando mudanças em: {directory}")
        
        original_files = set(os.listdir(directory))
        
        while True:
            time.sleep(5)
            current_files = set(os.listdir(directory))
            
            new_files = current_files - original_files
            deleted_files = original_files - current_files
            
            if new_files:
                print(f"📁 Novos arquivos: {new_files}")
            if deleted_files:
                print(f"🗑️  Arquivos deletados: {deleted_files}")
            
            original_files = current_files
    
    @staticmethod
    def show_prevention_tips():
        """Mostra dicas de prevenção"""
        tips = """
        🛡️  MEDIDAS DE PREVENÇÃO CONTRA MALWARES:
        
        1. ✅ Use antivírus atualizado
        2. ✅ Mantenha o sistema operacional atualizado
        3. ✅ Crie backups regulares
        4. ✅ Desconfie de emails e anexos suspeitos
        5. ✅ Use senhas fortes e autenticação em 2 fatores
        6. ✅ Eduque usuários sobre phishing
        7. ✅ Use firewall ativado
        8. ✅ Instale apenas software de fontes confiáveis
        9. ✅ Monitore atividades suspeitas na rede
        10.✅ Implemente políticas de segurança
        
        🎯 Lembre-se: A melhor defesa é a prevenção!
        """
        print(tips)

if __name__ == "__main__":
    security = SecurityMeasures()
    security.detect_suspicious_processes()
    security.show_prevention_tips()

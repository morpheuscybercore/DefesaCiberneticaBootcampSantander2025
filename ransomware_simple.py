# ransomware_simple.py
import os
import base64

class SimpleRansomwareSim:
    def __init__(self):
        self.test_files = []
        
    def create_test_files(self):
        """Cria arquivos de teste"""
        for i in range(3):
            filename = f"test_file_{i}.txt"
            with open(filename, 'w') as f:
                f.write(f"Conteúdo importante do arquivo {i}\n")
                f.write("Dados sensíveis para teste educativo\n")
            self.test_files.append(filename)
            print(f"📄 Criado: {filename}")
    
    def fake_encrypt(self, filename):
        """Simula criptografia (apenas codifica em base64)"""
        with open(filename, 'r') as f:
            content = f.read()
        
        # "Criptografia" simulada
        encrypted = base64.b64encode(content.encode()).decode()
        
        with open(filename + ".encrypted", 'w') as f:
            f.write(encrypted)
        
        # Remove o original
        os.remove(filename)
        print(f"🔒 Arquivo 'criptografado': {filename}")
    
    def fake_decrypt(self, encrypted_file):
        """Simula descriptografia"""
        with open(encrypted_file, 'r') as f:
            encrypted_content = f.read()
        
        # "Descriptografia" simulada
        decrypted = base64.b64decode(encrypted_content.encode()).decode()
        
        original_name = encrypted_file.replace(".encrypted", "")
        with open(original_name, 'w') as f:
            f.write(decrypted)
        
        os.remove(encrypted_file)
        print(f"🔓 Arquivo descriptografado: {original_name}")
    
    def show_ransom_note(self):
        """Exibe mensagem de resgate simulada"""
        note = """
        ⚠️  SEUS ARQUIVOS FORAM CRIPTOGRAFADOS! ⚠️
        
        Todos os seus arquivos importantes foram criptografados.
        Para recuperá-los, você precisa pagar um resgate.
        
        ❌ NÃO tente descriptografar sozinho
        ❌ NÃO reinstale o sistema
        ✅ Entre em contato com o suporte
        
        --- ESTE É UM SIMULADOR EDUCATIVO ---
        """
        print(note)
    
    def simulate_attack(self):
        """Simula o ataque completo"""
        print("🔧 Criando arquivos de teste...")
        self.create_test_files()
        
        print("\n🔒 Simulando criptografia...")
        for file in self.test_files:
            self.fake_encrypt(file)
        
        print("\n💸 Exibindo mensagem de resgate...")
        self.show_ransom_note()
        
        input("\nPressione Enter para descriptografar os arquivos...")
        
        print("\n🔓 Recuperando arquivos...")
        for file in self.test_files:
            self.fake_decrypt(file + ".encrypted")
        
        print("✅ Todos os arquivos foram recuperados!")

if __name__ == "__main__":
    print("🎓 SIMULADOR DE RANSOMWARE - FINS EDUCATIVOS\n")
    simulator = SimpleRansomwareSim()
    simulator.simulate_attack()

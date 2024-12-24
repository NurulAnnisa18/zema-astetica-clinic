# menu_system.py
import mysql.connector
from datetime import datetime
from colorama import Fore, Back, Style, init
import os
from tabulate import tabulate
from art import text2art
import time
from function import (  # Import semua fungsi yang sudah dibuat
    insert_customer,
    insert_many_customers,
    show_customers,
    update_customer,
    search_customer,
    delete_customer,
    insert_layanan,
    insert_many_layanan,
    show_layanan,
    update_layanan,
    search_layanan,
    delete_layanan,
    insert_pembayaran,
    show_pembayaran,
    update_pembayaran,
    insert_staff,
    delete_staff,
    update_staff,
    show_staff,
    insert_transaksi,
    delete_transaksi,
    update_transaksi,
    show_transaksi,
    update_stock,
    show_products
)

# Initialize colorama
init(autoreset=True)

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zema_estetika"
)

class MenuSystem:
    def _init_(self, connection):
        self.connection = connection

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, text):
        self.clear_screen()
        banner = text2art(text, font='small')
        print(Fore.CYAN + banner)
        print(Fore.YELLOW + "=" * 80)
        print(Style.RESET_ALL)

    def show_loading(self):
        print(Fore.CYAN + "\nLoading", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

    def handle_customer_menu(self):
        while True:
            self.print_header("CUSTOMER MANAGEMENT")
            print(f"{Fore.CYAN}╔══════════════════════════════════╗")
            print(f"{Fore.CYAN}║{Fore.WHITE}       MENU CUSTOMER             {Fore.CYAN}║")
            print(f"{Fore.CYAN}╠══════════════════════════════════╣")
            print(f"{Fore.CYAN}║{Fore.WHITE} 1. Insert Satu Customer        {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 2. Insert Banyak Customer      {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 3. Tampilkan Semua Customer    {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 4. Update Customer             {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 5. Cari Customer              {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 6. Hapus Customer             {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.RED} 0. Kembali ke Menu Utama      {Fore.CYAN}║")
            print(f"{Fore.CYAN}╚══════════════════════════════════╝{Style.RESET_ALL}")
            
            choice = input(f"{Fore.YELLOW}Pilih menu > {Style.RESET_ALL}")
            self.show_loading()
            
            try:
                if choice == "1":
                    insert_customer(self.connection)
                elif choice == "2":
                    insert_many_customers(self.connection)
                elif choice == "3":
                    show_customers(self.connection)
                elif choice == "4":
                    update_customer(self.connection)
                elif choice == "5":
                    search_customer(self.connection)
                elif choice == "6":
                    delete_customer(self.connection)
                elif choice == "0":
                    break
                else:
                    print(f"{Fore.RED}Menu tidak valid!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
            
            input(f"\n{Fore.GREEN}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")

    def handle_layanan_menu(self):
        while True:
            self.print_header("LAYANAN MANAGEMENT")
            print(f"{Fore.CYAN}╔══════════════════════════════════╗")
            print(f"{Fore.CYAN}║{Fore.WHITE}       MENU LAYANAN              {Fore.CYAN}║")
            print(f"{Fore.CYAN}╠══════════════════════════════════╣")
            print(f"{Fore.CYAN}║{Fore.WHITE} 1. Insert Satu Layanan         {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 2. Insert Banyak Layanan       {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 3. Tampilkan Semua Layanan     {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 4. Update Layanan              {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 5. Cari Layanan               {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 6. Hapus Layanan              {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.RED} 0. Kembali ke Menu Utama      {Fore.CYAN}║")
            print(f"{Fore.CYAN}╚══════════════════════════════════╝{Style.RESET_ALL}")
            
            choice = input(f"{Fore.YELLOW}Pilih menu > {Style.RESET_ALL}")
            self.show_loading()
            
            try:
                if choice == "1":
                    insert_layanan(self.connection)
                elif choice == "2":
                    insert_many_layanan(self.connection)
                elif choice == "3":
                    show_layanan(self.connection)
                elif choice == "4":
                    update_layanan(self.connection)
                elif choice == "5":
                    search_layanan(self.connection)
                elif choice == "6":
                    delete_layanan(self.connection)
                elif choice == "0":
                    break
                else:
                    print(f"{Fore.RED}Menu tidak valid!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
            
            input(f"\n{Fore.GREEN}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")

    # Implementasi menu-menu lainnya dengan pola yang sama...

    def run(self):
        while True:
            self.print_header("ZEMA ESTETIKA MANAGEMENT SYSTEM")
            print(f"{Fore.CYAN}╔══════════════════════════════════╗")
            print(f"{Fore.CYAN}║{Fore.WHITE}         MENU UTAMA              {Fore.CYAN}║")
            print(f"{Fore.CYAN}╠══════════════════════════════════╣")
            print(f"{Fore.CYAN}║{Fore.WHITE} 1. Menu Customer               {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 2. Menu Layanan               {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 3. Menu Pembayaran            {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 4. Menu Staff                 {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 5. Menu Transaksi             {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.WHITE} 6. Menu Product               {Fore.CYAN}║")
            print(f"{Fore.CYAN}║{Fore.RED} 0. Exit                       {Fore.CYAN}║")
            print(f"{Fore.CYAN}╚══════════════════════════════════╝{Style.RESET_ALL}")
            
            choice = input(f"{Fore.YELLOW}Pilih menu > {Style.RESET_ALL}")
            self.show_loading()
            
            try:
                if choice == "1":
                    self.handle_customer_menu()
                elif choice == "2":
                    self.handle_layanan_menu()
                elif choice == "3":
                    self.handle_pembayaran_menu()
                elif choice == "4":
                    self.handle_staff_menu()
                elif choice == "5":
                    self.handle_transaksi_menu()
                elif choice == "6":
                    self.handle_product_menu()
                elif choice == "0":
                    print(f"{Fore.YELLOW}Terima kasih telah menggunakan sistem ini!{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED}Menu tidak valid!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    class MenuSystem:  # Menggunakan MenuSystem bukan Menusystem
    def __init__(self, connection):
        self.connection = connection
import mysql.connector
from datetime import datetime
from colorama import Fore, Back, Style, init
import os
from tabulate import tabulate
from art import text2art
import time
import sys
from typing import List, Tuple, Dict, Any

# Initialize colorama
init(autoreset=True)

class DatabaseConnection:
    def _init_(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="zema_estetika"
            )
            print(f"{Fore.GREEN}Database connection successful!{Style.RESET_ALL}")
        except mysql.connector.Error as err:
            print(f"{Fore.RED}Error connecting to database: {err}{Style.RESET_ALL}")
            sys.exit(1)

    def _enter_(self):
        return self.connection

    def _exit_(self, exc_type, exc_val, exc_tb):
        if self.connection.is_connected():
            self.connection.close()

class UIHelper:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_header(text: str):
        """Print stylized header with custom art"""
        UIHelper.clear_screen()
        banner = text2art(text, font='small')
        print(Fore.CYAN + banner)
        print(Fore.YELLOW + "=" * 80)
        print(Style.RESET_ALL)

    @staticmethod
    def show_loading():
        """Show animated loading indicator"""
        print(Fore.CYAN + "\nLoading", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\n")

    @staticmethod
    def print_success(message: str):
        print(f"\n{Fore.GREEN}✔ {message}{Style.RESET_ALL}")

    @staticmethod
    def print_error(message: str):
        print(f"\n{Fore.RED}✘ {message}{Style.RESET_ALL}")

    @staticmethod
    def print_table(headers: List[str], data: List[Tuple]):
        """Print formatted table with data"""
        if not data:
            print(f"\n{Fore.YELLOW}No data available.{Style.RESET_ALL}")
            return
        
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

class CustomerManager:
    def _init_(self, connection):
        self.connection = connection

    def insert_customer(self):
        """Insert a single customer record"""
        try:
            print(f"\n{Fore.CYAN}=== Insert New Customer ==={Style.RESET_ALL}")
            name = input("Name: ")
            phone = input("Phone: ")
            address = input("Address: ")
            tgl_lahir = input("Birth Date (YYYY-MM-DD): ")

            cursor = self.connection.cursor()
            query = """
                INSERT INTO customers (name, phone, address, tgl_lahir) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, phone, address, tgl_lahir))
            self.connection.commit()
            UIHelper.print_success("Customer added successfully!")
        except mysql.connector.Error as err:
            UIHelper.print_error(f"Error: {err}")

    def show_customers(self):
        """Display all customers"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            UIHelper.print_table(headers, customers)
        except mysql.connector.Error as err:
            UIHelper.print_error(f"Error: {err}")

    # Add other customer-related methods here...



class MenuSystem:
    def _init_(self):
        self.db = DatabaseConnection()

    def display_menu(self, title: str, options: Dict[str, str]) -> str:
        """Display menu and return user choice"""
        while True:
            UIHelper.print_header(title)
            print(f"{Fore.CYAN}╔{'═' * 38}╗")
            print(f"║{title.center(38)}║")
            print(f"╠{'═' * 38}╣")
            
            for key, value in options.items():
                if key == '0':
                    print(f"║{Fore.RED} {key}. {value:<35}{Fore.CYAN}║")
                else:
                    print(f"║{Fore.WHITE} {key}. {value:<35}{Fore.CYAN}║")
            
            print(f"╚{'═' * 38}╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.YELLOW}Select option >{Style.RESET_ALL}")
            UIHelper.show_loading()
            
            if choice in options:
                return choice
            UIHelper.print_error("Invalid option!")
            time.sleep(1)

    def main_menu(self):
        """Main application menu"""
        options = {
            '1': 'Customer Management',
            '2': 'Service Management',
            '3': 'Payment Management',
            '4': 'Staff Management',
            '5': 'Transaction Management',
            '6': 'Product Management',
            '0': 'Exit'
        }

        while True:
            choice = self.display_menu("ZEMA ESTETIKA SYSTEM", options)
            
            if choice == '1':
                self.customer_menu()
            elif choice == '2':
                self.service_menu()
            elif choice == '3':
                self.payment_menu()
            elif choice == '4':
                self.staff_menu()
            elif choice == '5':
                self.transaction_menu()
            elif choice == '6':
                self.product_menu()
            elif choice == '0':
                if self.confirm_exit():
                    break

    def customer_menu(self):
        """Customer management menu"""
        with DatabaseConnection() as connection:
            customer_manager = CustomerManager(connection)
            options = {
                '1': 'Add New Customer',
                '2': 'Add Multiple Customers',
                '3': 'View All Customers',
                '4': 'Update Customer',
                '5': 'Search Customer',
                '6': 'Delete Customer',
                '0': 'Back to Main Menu'
            }

            while True:
                choice = self.display_menu("CUSTOMER MANAGEMENT", options)
                
                if choice == '1':
                    customer_manager.insert_customer()
                elif choice == '2':
                    customer_manager.insert_many_customers()
                elif choice == '3':
                    customer_manager.show_customers()
                elif choice == '4':
                    customer_manager.update_customer()
                elif choice == '5':
                    customer_manager.search_customer()
                elif choice == '6':
                    customer_manager.delete_customer()
                elif choice == '0':
                    break
                
                input(f"\n{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")

    def confirm_exit(self) -> bool:
        """Show exit confirmation dialog"""
        print(f"\n{Fore.YELLOW}Are you sure you want to exit? (y/n){Style.RESET_ALL}")
        return input().lower().strip() == 'y'

    # Add other menu methods (service_menu, payment_menu, etc.) following the same pattern...

def main():
    try:
        menu_system = MenuSystem()
        menu_system.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Program terminated by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
    finally:
        print(f"\n{Fore.CYAN}Thank you for using Zema Estetika Management System!{Style.RESET_ALL}")

if __name__ == "__main__":
        main()
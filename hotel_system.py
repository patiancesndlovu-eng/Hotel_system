import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class SkyCastPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Skyview Towers Executive Suite | Developed by Patie  Staicey")
        self.root.geometry("900x750")
        self.root.configure(bg="#0f172a")

        # --- DATA STORAGE ---
        self.rooms = {
            "101": {"type": "Standard", "price": 100, "status": "Available", "guest": "", "extras": 0},
            "201": {"type": "Deluxe", "price": 250, "status": "Available", "guest": "", "extras": 0},
            "301": {"type": "Presidential", "price": 700, "status": "Available", "guest": "", "extras": 0}
        }
        
        self.menu = {
            "Breakfast Buffet": 25,
            "Luxury Steak": 45,
            "Pink Mocktail": 12,
            "Club Sandwich": 18,
            "Spa Session": 80
    
        }

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background="#0f172a", borderwidth=0)
        style.configure("TNotebook.Tab", background="#1e293b", foreground="white", padding=[20, 10], font=("Poppins", 10))
        style.map("TNotebook.Tab", background=[("selected", "#ec4899")], foreground=[("selected", "white")])

    def create_widgets(self):
        # Header
        header = tk.Label(self.root, text="SKYVIEW TOWERS", font=("Poppins", 28, "bold"), fg="#ec4899", bg="#0f172a")
        header.pack(pady=20)

        # Tab Control
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=1, fill="both", padx=20, pady=10)

        # Create Tabs
        self.room_tab = tk.Frame(self.tabs, bg="#1e293b")
        self.food_tab = tk.Frame(self.tabs, bg="#1e293b")
        self.staff_tab = tk.Frame(self.tabs, bg="#1e293b")

        self.tabs.add(self.room_tab, text="🏨 ROOM RESERVATIONS")
        self.tabs.add(self.food_tab, text="🍽️ FOOD & SERVICES")
        self.tabs.add(self.staff_tab, text="🔑 STAFF PORTAL")

        self.setup_room_tab()
        self.setup_food_tab()
        self.setup_staff_tab()

        # Footer
        tk.Label(self.root, text="© 2026 Staicey Ndlovu | Advanced Hospitality Logic", fg="#475569", bg="#0f172a").pack(pady=10)

    # --- TAB 1: ROOM RESERVATIONS ---
    def setup_room_tab(self):
        container = tk.Frame(self.room_tab, bg="#1e293b", padx=30, pady=30)
        container.pack(fill="both")

        tk.Label(container, text="Guest Registration", font=("Poppins", 14, "bold"), fg="#ec4899", bg="#1e293b").grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
        
        tk.Label(container, text="Guest Name:", fg="white", bg="#1e293b").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(container, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        tk.Label(container, text="Room Number:", fg="white", bg="#1e293b").grid(row=2, column=0, sticky="w")
        self.room_choice = ttk.Combobox(container, values=list(self.rooms.keys()), state="readonly")
        self.room_choice.grid(row=2, column=1, pady=5)

        tk.Button(container, text="CONFIRM BOOKING", bg="#ec4899", fg="white", font=("Poppins", 10, "bold"), 
                  command=self.book_room, width=20, relief="flat").grid(row=3, column=0, columnspan=2, pady=20)

        self.room_display = tk.Text(container, height=10, bg="#0f172a", fg="#ec4899", padx=10, pady=10)
        self.room_display.grid(row=4, column=0, columnspan=2, sticky="we")
        self.update_room_display()

    # --- TAB 2: FOOD & SERVICES ---
    def setup_food_tab(self):
        container = tk.Frame(self.food_tab, bg="#1e293b", padx=30, pady=30)
        container.pack(fill="both")

        tk.Label(container, text="Digital Menu & Amenities", font=("Poppins", 14, "bold"), fg="#8b5cf6", bg="#1e293b").pack(anchor="w")
        
        # Menu Selection
        tk.Label(container, text="Select Item:", fg="white", bg="#1e293b").pack(pady=5)
        self.item_choice = ttk.Combobox(container, values=list(self.menu.keys()), state="readonly", width=40)
        self.item_choice.pack()

        tk.Label(container, text="Assign to Room:", fg="white", bg="#1e293b").pack(pady=5)
        self.assign_room = ttk.Combobox(container, values=list(self.rooms.keys()), state="readonly", width=10)
        self.assign_room.pack()

        tk.Button(container, text="ADD TO BILL", bg="#8b5cf6", fg="white", font=("Poppins", 10, "bold"), 
                  command=self.order_food, width=20, relief="flat").pack(pady=20)

        self.service_log = tk.Text(container, height=8, bg="#0f172a", fg="#8b5cf6", padx=10, pady=10)
        self.service_log.pack(fill="x")

    # --- TAB 3: STAFF PORTAL ---
    def setup_staff_tab(self):
        container = tk.Frame(self.staff_tab, bg="#1e293b", padx=30, pady=30)
        container.pack(fill="both")

        tk.Label(container, text="Internal Staff Access", font=("Poppins", 14, "bold"), fg="white", bg="#1e293b").pack(pady=10)
        
        tk.Label(container, text="Staff ID:", fg="white", bg="#1e293b").pack()
        self.staff_id = tk.Entry(container, show="*", width=20)
        self.staff_id.pack(pady=5)

        tk.Button(container, text="GENERATE REVENUE REPORT", bg="#334155", fg="white", command=self.staff_report).pack(pady=10)
        tk.Button(container, text="CHECKOUT GUEST", bg="#f43f5e", fg="white", command=self.checkout_ui).pack(pady=5)

    # --- CORE LOGIC ---
    def update_room_display(self):
        self.room_display.delete('1.0', tk.END)
        header = f"{'ROOM':<10} {'STATUS':<15} {'GUEST':<20} {'SERVICES'}\n"
        self.room_display.insert(tk.END, header + "-"*60 + "\n")
        for rm, data in self.rooms.items():
            line = f"{rm:<10} {data['status']:<15} {data['guest']:<20} ${data['extras']}\n"
            self.room_display.insert(tk.END, line)

    def book_room(self):
        name = self.name_entry.get()
        rm = self.room_choice.get()
        if name and rm:
            if self.rooms[rm]["status"] == "Available":
                self.rooms[rm]["status"] = "Occupied"
                self.rooms[rm]["guest"] = name
                messagebox.showinfo("Skyview Towers", f"Room {rm} Reserved for {name}")
                self.update_room_display()
            else:
                messagebox.showerror("Error", "Room is already Occupied")
        else:
            messagebox.showwarning("Warning", "Complete all fields")

    def order_food(self):
        item = self.item_choice.get()
        rm = self.assign_room.get()
        if item and rm:
            if self.rooms[rm]["status"] == "Occupied":
                price = self.menu[item]
                self.rooms[rm]["extras"] += price
                self.service_log.insert(tk.END, f"[{datetime.now().strftime('%H:%M')}] {item} added to Room {rm} (${price})\n")
                self.update_room_display()
            else:
                messagebox.showerror("Error", "Cannot order food for an empty room.")

    def checkout_ui(self):
        rm = self.room_choice.get()
        if rm and self.rooms[rm]["status"] == "Occupied":
            base = self.rooms[rm]["price"]
            extra = self.rooms[rm]["extras"]
            total = base + extra
            guest = self.rooms[rm]["guest"]
            
            receipt = f"GUEST: {guest}\nRoom Base: ${base}\nServices: ${extra}\nTOTAL DUE: ${total}"
            messagebox.showinfo("Final Invoice", receipt)
            
            self.rooms[rm]["status"] = "Available"
            self.rooms[rm]["guest"] = ""
            self.rooms[rm]["extras"] = 0
            self.update_room_display()
        else:
            messagebox.showwarning("Error", "Select an occupied room to checkout")

    def staff_report(self):
        if self.staff_id.get() == "STAICEY2026":
            total_revenue = sum(data['extras'] for data in self.rooms.values() if data['status'] == "Occupied")
            messagebox.showinfo("Staff Report", f"Active Room Services Revenue: ${total_revenue}")
        else:
            messagebox.showerror("Denied", "Invalid Staff Credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = SkyCastPro(root)
    root.mainloop()
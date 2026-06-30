"""
PROBLEM STATEMENT:
Write a program to Create ticket booking system.
"""

class Event:

    """Represents a specific show, movie, or event.
       This class tracks the event name, total available seats, ticket price,
       and manages booked seat numbers to ensure tickets aren't double-booked."""

    def __init__(self, event_id, name, total_seats, ticket_price):
    
        self.event_id = event_id
        
        self.name = name
        
        self.total_seats = total_seats
        
        self.ticket_price = ticket_price
        
        self.booked_seats = set()


    def get_available_seats_count(self):
    
        """Calculates the remaining number of unbooked seats.
           The time complexity of this subtraction operation is O(1)."""
           
        return self.total_seats - len(self.booked_seats)


    def book_tickets(self, num_tickets):
    
        """Books a requested quantity of tickets for this event.
           Allocates incremental seat numbers starting from seat 1 up to total_seats."""
           
        if num_tickets <= 0:
        
            print("\nError: You must book at least 1 ticket.")
            
            return
            
        available = self.get_available_seats_count()
        
        if num_tickets > available:
        
            print(f"\nError: Not enough seats available. Remaining: {available}")
            
            return
            
        newly_booked = []
        
        seat_candidate = 1
        
        while len(newly_booked) < num_tickets and seat_candidate <= self.total_seats:
        
            if seat_candidate not in self.booked_seats:
            
                self.booked_seats.add(seat_candidate)
                
                newly_booked.append(seat_candidate)
                
            seat_candidate += 1
            
        total_cost = num_tickets * self.ticket_price
        
        print(f"\nSuccessfully booked {num_tickets} ticket(s) for '{self.name}'!")
        
        print(f"Allocated Seats: {newly_booked}")
        
        print(f"Total Amount Paid: ${total_cost:.2f}")


class TicketSystem:

    """Manages multiple events and coordinates user transactions.
       It stores data inside a dictionary mapping an event ID to an Event object.
       The time complexity to look up or add an event is O(1) on average."""

    def __init__(self):
    
        self.events = {}


    def add_event(self, event_id, name, total_seats, ticket_price):
    
        """Registers a brand new event into the database system."""
        
        if event_id in self.events:
        
            print(f"\nError: Event ID {event_id} already exists.")
            
            return
            
        new_event = Event(event_id, name, total_seats, ticket_price)
        
        self.events[event_id] = new_event
        
        print(f"\nEvent '{name}' added successfully to the catalog!")


    def display_events(self):
    
        """Prints all events, pricing structures, and current seating availability."""
        
        if not self.events:
        
            print("\nThere are no upcoming events listed at this time.")
            
            return
            
        print("\n--- Upcoming Events Catalog ---")
        
        for event_id, ev in self.events.items():
        
            rem = ev.get_available_seats_count()
            
            print(f"ID: {event_id} | Name: {ev.name} | Price: ${ev.ticket_price:.2f} | Available Seats: {rem}/{ev.total_seats}")


booking_system = TicketSystem()

booking_system.add_event("101", "Inception Live Concert", 50, 120.00)

booking_system.add_event("102", "Cyberpunk Movie Premiere", 100, 15.50)

while True:

    print("\n==============================")
    
    print("    TICKET BOOKING SYSTEM")
    
    print("==============================")
    
    print("1. View Upcoming Events")
    
    print("2. Book Show Tickets")
    
    print("3. Admin: Add New Event")
    
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
    
        booking_system.display_events()
        
    elif choice == "2":
    
        booking_system.display_events()
        
        if booking_system.events:
        
            ev_id = input("\nEnter the Event ID you wish to book: ")
            
            if ev_id in booking_system.events:
            
                try:
                
                    qty = int(input("Enter number of tickets to purchase: "))
                    
                    booking_system.events[ev_id].book_tickets(qty)
                    
                except ValueError:
                
                    print("\nError: Please enter a valid integer for ticket quantity.")
                    
            else:
            
                print("\nError: Invalid Event ID selected.")
                
    elif choice == "3":
    
        new_id = input("Enter unique Event ID: ")
        
        new_name = input("Enter Event Name: ")
        
        try:
        
            seats = int(input("Enter total seat capacity: "))
            
            price = float(input("Enter single ticket price ($): "))
            
            booking_system.add_event(new_id, new_name, seats, price)
            
        except ValueError:
        
            print("\nError: Invalid entry numbers for capacity or price.")
            
    elif choice == "4":
    
        print("\nThank you for choosing our ticketing platform. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please pick an alternative number from 1 to 4.")
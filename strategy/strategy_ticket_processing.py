# Sample strategy implementation using abstract class 

import string
import random

from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    return "".join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

class CustomerSupport:
    ticket_list: List[SupportTicket] = []    
    
    def create_ticket(self, customer, issue):
        self.ticket_list.append(SupportTicket(customer, issue))
        
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ordered_list = processing_strategy.create_ordering(self.ticket_list)
        
        if len(ordered_list) == 0:
            print("All Done! Nothing to process!")
            return 

        for ticket in ordered_list:
            self.process_ticket(ticket)
            
    def process_ticket(self, ticket: SupportTicket):
        print("==========================")
        print(f"ID:\t\t{ticket.id}")
        print(f"Customer:\t{ticket.customer}")
        print(f"Issue:\t\t{ticket.issue}")
        print("==========================")
        
app = CustomerSupport()

app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Igor Burgitch", "I deleted the internet, the world is in danger.")
app.create_ticket("Wall Entina", "My vacuum cleaner robot is rude to me")

app.process_tickets(RandomOrderingStrategy())
#ticket class

class Ticket:
    def __init__(self, ticketNumber, seatingNumber):
        self.__ticketNumber = ticketNumber
        self.__seatingNumber = seatingNumber
    
    @property
    def get_ticket_number(self):
        return self.__ticketNumber
    
    def get_seating_number(self):
        return self.__seatingNumber
    
    def __str__(self):
        return f"Ticket Infomation:\n Ticket Number: {self.__ticketNumber}\n Seating Number: {self.__seatingNumber}\n"
        
    
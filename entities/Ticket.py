class Ticket:
    def __init__(self, ticket_number: int, employee_id: int, reimbursement_reason: str, reimbursement_ticket_amount: float):
        self.ticket_number = ticket_number
        self.employee_id = employee_id
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_ticket_amount = reimbursement_ticket_amount


        
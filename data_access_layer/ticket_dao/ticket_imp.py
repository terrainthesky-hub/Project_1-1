from typing import List

from custom_exceptions.bad_ticket_info import BadTicketInfo
from custom_exceptions.connection_problem import ConnectionProblem
from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.ticket_dao.ticket_interface import TicketDAOInterface
from entities.Ticket import Ticket
from utils.manage_connection import connection


class TicketDAOImp(TicketDAOInterface):

    def create_ticket(self, employee_id: int, reimbursement_reason: str, reimbursement_ticket_amount: float):
        try:
            sql = "insert into ticket values(default, %s, %s, %s) returning ticket_number"
            cursor = connection.cursor()
            cursor.execute(sql, (employee_id, reimbursement_reason, reimbursement_ticket_amount))
            connection.commit()
            Ticket_number = cursor.fetchone()[0]
            return Ticket_number
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

    def get_ticket_by_ticket_number(self, ticket_number: int):
        sql = "select * from ticket where ticket_number = %s"
        cursor = connection.cursor()
        cursor.execute(sql[ticket_number])
        record = cursor.fetchone()
        if len(record) != 0:
            ticket = Ticket(*record)
            return ticket
        else:
            raise BadTicketInfo("Not ticket with that ticket number was found")

    def get_all_ticket_by_employee_id(self, employee_id: int) -> List[Ticket]:
        sql = "select * from ticket where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        if len(records) != 0:
            tickets = []
            for record in records:
                ticket = Ticket(*record)
                tickets.append(Ticket.ticket_dictionary_conversion(ticket))
            return tickets
        else:
            raise BadTicketInfo("No tickets found with that employee number were found")

    def update_ticket(self, ticket: Ticket) -> Ticket:
        sql = "update * ticket where ticket_number = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [ticket.reimbursement_reason, ticket.reimbursement_ticket_amount])
        connection.commit()
        if cursor.rowcount != 0:
            return ticket
        else:
            raise BadTicketInfo("No ticket with that ticket number was found")

    def delete_ticket(self, ticket_number: int):
        try:
            sql = "delete from ticket where ticket_number = %s"
            cursor = connection.cursor()
            cursor.execute(sql[ticket_number])
            connection.commit()
            if cursor.rowcount != 0:
                return True
            else:
                raise NothingDeleted("Ticket was not deleted")
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

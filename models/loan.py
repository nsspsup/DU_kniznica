
# models/loan.py

class Loan:
    def __init__(self, id, book_id, member_id, loan_date, return_date=None):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.return_date = return_date

    def __repr__(self):
        return f"<Loan book_id={self.book_id} member_id={self.member_id}>"

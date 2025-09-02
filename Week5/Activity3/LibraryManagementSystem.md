#  Library Management System

### Class Diagram

![Yoobee College Database Schema](class_diagram.png)

1. Book: Bibliographic record (title, author, ISBN, publicationDate). One Book can have many physical copies.
2. Genre: Lookup table of genres.
3. BookGenre: Junction entity implementing many-to-many between Book and Genre.
4. BookCopy: A physical, lendable copy. Has a status (Available, CheckedOut, Lost).
5. Member: Library patron with contact details and membershipExpirationDate.
6. Librarian: Staff / admin user. Used optionally to record who performed actions (provenance).
7. Loan: Circulation record linking a Member to a BookCopy with borrowDate, dueDate, and returnDate.
8. Fine: Overdue charge attached to a Loan; includes amount, paid flag, and paymentDate.


### Use-Case Diagram

![Yoobee College Database Schema](use_case_diagram.png)

# Actors
• Member: A library patron who searches the catalog, borrows/returns books, views loans, and pays fines.
• Librarian: Staff who can also register members and add books/copies, in addition to borrowing/returning on behalf of patrons.

# Key Use Cases
• Search Catalog: Find books by title/author/ISBN and filter by genre.
• Borrow Book: Create a loan for an available copy after eligibility checks.
• Return Book: Close a loan and restore copy availability; compute overdue fine if late.
• View My Loans: Show a member’s current loans with due dates.
• Pay Fine: Settle overdue fines (after late returns).
• Add New Book & Copies: Create a new book record and physical copies (admin).
• Register Member: Add a new library member with an expiry date (admin).
# Sub Use Cases (Reusable Checks)
• Calculate Fine: Compute overdue days × daily rate during returns.
• Check Eligibility: Composite check ensuring membership valid, loan limit not exceeded, and copy available.
• Check Membership Valid: Membership not expired as of today.
• Check Loan Limit (≤5): Member has no more than 5 concurrent open loans.
• Check Copy Availability: A physical copy exists that is not already on loan.


### Sequence Diagram

![Yoobee College Database Schema](a_check_availability.png)
# A) Check Availability
• Goal: See if a free physical copy exists for the chosen book.
• Trigger: Member clicks 'Borrow this book'.
• System: Finds the book by ISBN/title, then looks for an available copy.
• Outcome: If a copy is found → continue to eligibility checks. If none → show 'No copies available. Place a hold / join the waitlist.'

![Yoobee College Database Schema](b1_membership_valid.png)
# B1) Membership Valid?
• Goal: Ensure the library card is still valid.
• System: Compares membershipExpirationDate with today.
• Outcome: Valid → continue. Expired → stop and show 'Membership expired—please renew.'

![Yoobee College Database Schema](b2_loan_limit.png)
# B2) Loan Limit (≤ 5)?
• Goal: Enforce the policy of maximum 5 active loans.
• System: Counts the member’s open loans.
• Outcome: ≤5 → continue. >5 → stop and show 'You already have 5+ books out—return some first.'

![Yoobee College Database Schema](b3_unpaid_fines.png)
# B3) Unpaid Fines?
• Goal: Block borrowing if old fines are unpaid.
• System: Checks total outstanding fines.
• Outcome: 0 → continue. >0 → stop and show 'Borrowing blocked until fines are paid.'

![Yoobee College Database Schema](c_create_loan.png)
# C) Create Loan
• Goal: Finalize the borrow after all checks pass.
• System: Creates the Loan (borrowDate and dueDate) and marks the copy OnLoan.
• Member sees: 'Success—your loan is active. Due on {dueDate}.'

![Yoobee College Database Schema](d_borrows.png)
# D) Borrow — Failure Reasons
• Goal: Explain clearly why borrowing was stopped and what to do next.
• Possible messages: 'No copies available—place a hold', 'Membership expired—renew to borrow', 'Limit reached (5)—return some books first', 'Unpaid fines—pay to continue'.

![Yoobee College Database Schema](e_find_open_loan.png)
# E) Find Open Loan (for Return)
• Goal: Make sure the system is returning the correct active loan for that copy.
• System: Looks up the open loan by copyId.
• Outcome: Found → continue with return. Not found → show 'No active loan for this copy—please see the desk.'

![Yoobee College Database Schema](f_fine_calculate.png)
# F) Fine Calculation
• Goal: Work out late days and the fine amount.
• System: Compares dueDate with today to compute days overdue and fine.
• Outcome: Fine = 0 → 'Returned on time.' Fine > 0 → 'Overdue {days} day(s). Fine: {amount}.' (Member can pay now or later.)

![Yoobee College Database Schema](g_update_return.png)
# G) Close Loan & Update Copy
• Goal: Finish the return and update availability.
• System: Sets returnDate on the loan and marks the copy Available.
• Member sees: No fine → 'Returned on time—thank you.' Fine due → 'Returned—You owe {amount} for {days} day(s).'


### Activity Diagram

![Yoobee College Database Schema](borrow_book.png)
# Borrow Book
• Member chooses a book. System checks membership, available copy, loan limit and fines. If OK, member confirms and the system creates the loan, marks the copy on-loan, and shows the due date.
	
![Yoobee College Database Schema](return_book.png)
# Return Book
• Member brings the copy. System scans and finds the open loan. If overdue, it calculates the fine. Member pays if needed; system records the return and sets the copy to Available.

![Yoobee College Database Schema](new_book.png)
# Add New Book & Copies (Admin)
• Librarian enters a new title and quantity of copies. The system creates the book and copy records and confirms.

# Register Member (ADmin)
![Yoobee College Database Schema](new_member.png)
• Librarian inputs details. System creates the member, sets expiry, and provides a card for the librarian to hand over.


![Yoobee College Database Schema](pay_fine.png)
# Pay Fine
• Member reviews outstanding fines, selects a payment method, pays and gets a receipt. Status becomes Paid.

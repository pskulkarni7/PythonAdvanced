import csv

def display_customers():
    """Display customer information in a formatted manner.

    :param customers: An iterable of customer data, where each customer is represented as a list.
    """ 
    with open('customers.csv', 'r') as customer_data:
      customers = csv.reader(customer_data)
      print("Customer ID, First Name, Last Name, Email")
      for customer in customers:
          customer_id = customer[0]
          first_name = customer[2]
          last_name = customer[3]
          email_id = customer[9]
          print(f"Customer #{customer_id}, {first_name} {last_name}, {email_id}")

with open('customers.csv', 'r') as customer_data:
  customers = csv.reader(customer_data)

display_customers()

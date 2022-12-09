#`Doctor Booking System (Healthy-Afya App)`
## SEPA Program Sprint Two

# Problem Definition
From time to time, patients usually require specialized treatment in cities such as
Nairobi. You can either visit the doctor's office to get an appointment or make a phone
call. We want to simplify the process by allowing patients to see a list of doctors in a
certain city and book an appointment with them.
I want to building a web application called Healthy-Afya . The
admin should be able to create user accounts for doctors and then doctors can login
and create their schedule. A patient first needs to create a user account before being
able to book a doctor. You can also explore options for doctors to create their own
accounts but these accounts should be verified by the admin first before they appear
for patients to book.
So there are 3 user levels, administrator, doctor and patient. When a patient books an
appointment with a certain specialist, they get an automated email. When a doctor logs
into the system, they should see a list of patients that have booked their services and
the appointment times
# Sprint Outcomes
At the end of the Sprint, the learner is expected to:
1. Be able to use the Django framework in developing a web application
2. Have a good understanding of database design in SQL
3. Be able to integrate SQL Database in data storage for a Django web app

# Figma Design File

## About Healthy-Afya
Healthy Afya is A Doctor Management System
This program is developed  using Django framework.
It is a multi user application .
The three Users in this system are:
 - Admin
 - Patient
 - Doctor

 A Patient creates their accounts and logs  in to the system. Once logged in , a patient can View appointments, book an appointment and apply to be a doctor. If a patient applies to be a doctor, their request is not immediately approved.
 A doctor has to register as a Patient then apply to be a doctor or have their accounts created by an admin. A doctor views appointments; approves, accepts or rejects them. A doctor can also create their schedule.

# Healthy-Afya at a glance
![image](landingpage.png)

## Table of contents
* [About Healthy-Afya](#AboutHealthy-Afya)
* [Technologies](#Technologies)
* [Features](#Features)
* [Setup](#Setup)

## Technologies
* Language: [Python 3.8](https://www.python.org/downloads/release/python-3810/)
* [JSON](https://www.json.org/json-en.html)
* [GMAIL](https://www.google.com/gmail/about/)
* IDE: [Pycharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

## Features
## Patient Dashboard
A patient dashboard appears once a User is authenitciated as a Patient
# Patient Dashboard
![image](patient_dashboard.png)
### Customer Operations
A user is able to feed into the system customer data, view available customers, update existing customer data and delete a particular customer. All customer records can further be accessed.
A customer can be able to view available products or exit at this stage. 
The customer details are stored in customers.json

    Sample Customer details Format
    ```
        [
            {
                "name": "Vincent Kimutai",
                "age": "24",
                "email": "kimutai@gmail.com",
                "phone": "0723265092"
                  "id": "5",
            },
        ]
    ```
### Product Operations
A user can key in the product's data for inventory purposes, view the available products, update product data and delete a product. 
A customer can proceed to purchases at this point here-in or exit the program.
The products are stored at products.json file

    Sample Product details Format
    ```
        [
            {
                "name": "Dell laptop",
                "quantity": 800,
                "cost": 66_500,
                "id": 2
            },
        ]
    ```
### Purchase function
Before a customer makes any purchases, they first need to be authenticated.
When the customer is authenticated, they can then proceed to view all the available products and their quantities.
A customer can then begin to make purchases. The products they purchases are added to a cart and the totals for each product and its quantities are calculated at that point, if the customer wishes to proceed to make purchases, then their sub-totals
will be added to the previous. 
When the customer is done purchasing, a receipt is given to them which contains their name, the product they purchased, the quantities and the total cost.
The customer is further asked whether they would like to receive such a receipt via email. If the customer accepts, the receipt is send to their email and this only happens if the customer provided an existing email.
The program then terminates at this point.
Further advancement could include having a customer purchase history, checking whether a product really exists before adding it to the products json file.


## Setup
### Requirements
Python 3 is required to be installed in your system. Depending on your operating system, you can download one that is compatible from the [Official Python website](https://www.python.org/downloads/) 
### Installation
To install this application, one is required to clone this repo by running the following command on your terminal:
```bash 
git clone https://github.com/VincentLangat033/healthy-afya-app.git
```
Then enter the folder of the application by running:
```bash 
cd point-of-sale-terminal
```
Start the program by running the following command:
```bash 
python main.py
```
## Known Bugs
There are no known bugs in this program and all the functionalities stated to be executable are indeed working.

## Contributions
Feel free to fork and clone this repository and contribute to it!
```bash 
git clone https://github.com/VincentLangat033/healthy-afya-app.git
```

Author
---
This project was developed by : [Vincent Langat](https://github.com/VincentLangat033)
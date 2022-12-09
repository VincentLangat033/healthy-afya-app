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
[Figma File](https://www.figma.com/file/5LyjtuZYyO29cX7KYdCBWp/Afya-app?node-id=0%3A1&t=Aq7NIndp40eDr9eb-0)

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
* Language: [DJANGO](https://docs.djangoproject.com/en/4.1/)
* [MYSQL](https://www.mysql.com/)
* [GMAIL](https://www.google.com/gmail/about/)

## Features
## Patient Dashboard
A patient dashboard appears once a User is authenitciated as a Patient
# Patient Dashboard
![image](patient_dashboard.png)
### Patient Journey
- A patient is able to create an account and login
- A patient can book an appointment with a doctor according to their desired regions
- As soon as they book, they'll receive an eamil that their appointment is pending awaiting the Doctors approval
- A patient can apply to be a doctor
- A patient can then log off the system ( A few other links still cooking😊)

### Doctor Dashboard
![image](doctor-dashboard.png)

### Doctor Journey
Once a Doctor is approved and/or created by the admin, they will be able to log in and perform the following:
- View  their appointments where they can reject or approve
- Create their Schedule
- They can log off at any time.

### Admin Dashboard
![image](admin_dashboard.png)




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
## Challenges during development
- Production server a bit slow   [Link](https://kim-healthy-afya-app.up.railway.app/) 
- Used Tailwind for styling and had to occasionally revert to vanilla css
- Further integrating and utilization of Models in django
- Trouble implementing django authentication systems (managed to get it done)

## Known Bugs
There are no known bugs, however you may find some buttons are unresponsive


## Contributions
Feel free to fork and clone this repository and contribute to it!
```bash 
git clone https://github.com/VincentLangat033/healthy-afya-app.git
```

Author
---
This project was developed by : [Vincent Langat](https://github.com/VincentLangat033)
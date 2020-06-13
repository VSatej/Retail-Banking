"""
    CREATE DATABASE xplore;

    USE xplore;

    CREATE TABLE userstore(
<<<<<<< HEAD
        Login VARCHAR(20) NOT NULL PRIMARY KEY,
        Password VARCHAR(20) NOT NULL,
        TimeStamp TIMESTAMP NOT NULL
=======
        login varchar(50) NOT NULL PRIMARY KEY,
        password VARCHAR(20) NOT NULL,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
>>>>>>> 3d1682aa68936cf10aac44d12602286d5d98e710
    );

    CREATE TABLE Customer(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Name VARCHAR(20) NOT NULL,
        Address VARCHAR(40) NOT NULL,
        Age INT NOT NULL
    );

    CREATE TABLE Account(
<<<<<<< HEAD
        Customer_ID INT NOT NULL PRIMARY KEY,
        Account_ID INT NOT NULL,
=======
        Customer_ID INT NOT NULL,
        Account_ID INT NOT NULL PRIMARY KEY,
>>>>>>> 3d1682aa68936cf10aac44d12602286d5d98e710
        Balance INT NOT NULL,
        CR_Data DATE NOT NULL,
        CR_LastDate DATE NOT NULL,
        Duration INT NOT NULL
    );

    CREATE TABLE Transactions(
        Customer_ID INT NOT NULL PRIMARY KEY,
        Account_Type VARCHAR(20) NOT NULL,
        Transaction_Date DATE NOT NULL,
        Source_AccountType VARCHAR(20) NOT NULL,
        Target_AccountType VARCHAR(20) NOT NULL
    );

    CREATE TABLE CustomerStatus(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(20) NOT NULL,
        Last_Updated VARCHAR(20) NOT NULL
    );

    CREATE TABLE AccountStatus(
        Customer_ID INT NOT NULL PRIMARY KEY,
        Account_ID INT NOT NULL,
        Account_Type VARCHAR(20) NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(20) NOT NULL,
        Last_Updated VARCHAR(20) NOT NULL
    );

"""
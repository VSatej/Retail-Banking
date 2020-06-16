"""
    CREATE DATABASE xplore;

    USE xplore;

    CREATE TABLE userstore(
        login varchar(50) NOT NULL PRIMARY KEY,
        password VARCHAR(20) NOT NULL,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE Customer(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Name VARCHAR(40) NOT NULL,
        Address VARCHAR(100) NOT NULL,
        Age INT NOT NULL
    );

    CREATE TABLE Account(
        Customer_ID INT NOT NULL,
        Account_ID INT NOT NULL PRIMARY KEY,
        Balance INT NOT NULL,
        CR_Data DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CR_LDate DATE,
        Duration INT NOT NULL DEFAULT 10
    );

    CREATE TABLE Transactions(
        Customer_ID INT NOT NULL,
        Account_Type VARCHAR(20) NOT NULL,
        Transaction_Date DATE NOT NULL,
        Source_AccountType VARCHAR(20) NOT NULL,
        Target_AccountType VARCHAR(20) NOT NULL
    );

    CREATE TABLE CustomerStatus(
        SSN_ID INT NOT NULL,
        Customer_ID INT NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(100) NOT NULL,
        Last_Updated DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE AccountStatus(
        Customer_ID INT NOT NULL,
        Account_ID INT NOT NULL,
        Account_Type VARCHAR(20) NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(100) NOT NULL,
        Last_Updated DATETIME DEFAULT CURRENT_TIMESTAMP
    );

"""
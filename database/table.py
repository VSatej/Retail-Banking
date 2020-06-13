"""
    CREATE DATABASE xplore;

    USE xplore;

    CREATE TABLE userstore(
        Login VARCHAR(20) NOT NULL PRIMARY KEY,
        Password VARCHAR(20) NOT NULL,
        TimeStamp TIMESTAMP NOT NULL
    );

    CREATE TABLE Customer(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Name VARCHAR(20) NOT NULL,
        Address VARCHAR(40) NOT NULL,
        Age INT NOT NULL
    );

    CREATE TABLE Account(
        Customer_ID INT NOT NULL PRIMARY KEY,
        Account_ID INT NOT NULL,
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
"""
    CREATE DATABASE xplore;

    USE xplore;

    CREATE TABBLE userstore(
        Login VARCHAR(20) NOT NULL,
        Password VARCHAR(20) NOT NULL,
        TimeStamp TIMESTAMP NOT NULL
    );

    CREATE TABLE Customer(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Name VARCHAR(20) NOT NULL,
        Address VARCHAR(20) NOT NULL,
        Age INT NOT NULL
    );

    CREATE TABLE Account(
        Customer_ID INT NOT NULL ,
        Account_ID INT NOT NULL,
        Balance INT NOT NULL,
        CR_Data INT NOT NULL,
        CR_LastDate Date NOT NULL,
        Duration INT NOT NULL
    );

    CREATE TABLE Transactions(
        Customer_ID INT NOT NULL,
        Account_Type VARCHAR(20) NOT NULL,
        Transaction_Date DATE NOT NULL,
        Source_AccountType VARCHAR(20) NOT NULL,
        Target_AccountType VARCHAR(20) NOT NULL,
    );

    CREATE TABLE CustomerStatus(
        SSN_ID INT NOT NULL PRIMARY KEY,
        Customer_ID INT NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(20) NOT NULL,
        Last_Updated VARCHAR(20) NOT NULL
    );

    CREATE TABLE AccountStatus(
        Customer_ID INT NOT NULL,
        Account_ID INT NOT NULL,
        Account_Type VARCHAR(20) NOT NULL,
        Status VARCHAR(20) NOT NULL,
        Message VARCHAR(20) NOT NULL,
        Last_Updated VARCHAR(20) NOT NULL
    );

"""
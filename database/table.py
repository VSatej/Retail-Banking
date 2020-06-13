"""
    CREATE DATABASE xplore;

    USE xplore;

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

    DESCRIBE CUSTOMERSTATUS;

    DESCRIBE ACCOUNTSTATUS;

    SELECT * FROM CUSTOMERSTATUS;

    SELECT * FROM ACCOUNTSTATUS;

"""
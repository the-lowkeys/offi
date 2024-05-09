--Table Generation Section--

CREATE TABLE Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    TransactionType VARCHAR(8) NOT NULL,
    EmployeeID INTEGER NOT NULL,
    FileID INTEGER NOT NULL,
    DrawerID INTEGER NOT NULL,
    CabinetID INTEGER NOT NULL
);

CREATE TABLE Cabinets (
    CabinetID INTEGER PRIMARY KEY AUTOINCREMENT,
    CabinetLabel VARCHAR(50) NOT NULL,
    DrawerMaxFileCount INTEGER NOT NULL,
    CabinetRowCount INTEGER NOT NULL,
    CabinetColumnCount INTEGER NOT NULL,
    CabinetRoom VARCHAR(50) NOT NULL,
    CabinetFloor INTEGER NOT NULL
);

CREATE TABLE Drawers (
    DrawerID INTEGER PRIMARY KEY AUTOINCREMENT,
    DrawerLabel VARCHAR(50) NOT NULL,
    FileCount INTEGER NOT NULL,
    CabinetID INTEGER NOT NULL,
    CabinetRow INTEGER NOT NULL,
    CabinetColumn INTEGER NOT NULL,
);

CREATE TABLE Files (
    FileID INTEGER PRIMARY KEY AUTOINCREMENT,
    FileLabel VARCHAR(50) NOT NULL,
    FileDescription VARCHAR(2000),
    DrawerID INTEGER NOT NULL
);

--Heap Locations--

INSERT INTO Cabinets() VALUES ()
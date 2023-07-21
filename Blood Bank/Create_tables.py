import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "bloodBank"
)

myCursor = mydb.cursor()

sql_command = """

CREATE TABLE donor (
    donor_id INT,
    donor_name VARCHAR(20),
    donor_phone CHAR(11),
    donor_dob DATE,
    donor_gender VARCHAR(11),
    donor_address VARCHAR(20),
    donor_weight INT,
    donor_bp VARCHAR(10),
    donor_ic VARCHAR(20),
    doctor_id INT,
    PRIMARY KEY (donor_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id),
    CHECK (donor_gender IN ("Male", "Female", "Other"))
);
CREATE TABLE donor (
    donor_id INT,
    donor_name VARCHAR(20),
    donor_phone CHAR(11),
    donor_dob DATE,
    donor_gender VARCHAR(11),
    donor_address VARCHAR(20),
    donor_weight INT,
    donor_bp VARCHAR(10),
    donor_ic VARCHAR(20),
    doctor_id INT,
    PRIMARY KEY (donor_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id),
    CHECK (donor_gender IN ("Male", "Female", "Other"))
);

CREATE TABLE blood_bank(
    bb_id INT,
    bb_name VARCHAR(20),
    bb_address VARCHAR(20),
    PRIMARY KEY(bb_id)
);

CREATE TABLE blood(
    blood_type VARCHAR(11),
    donor_id INT,
    bb_id INT,
    FOREIGN KEY(donor_id) REFERENCES donar(donor_id),
    FOREIGN KEY(bb_id) REFERENCES blood_bank(bb_id),
);

CREATE TABLE patient(
    p_id INT,
    p_name VARCHAR(30),
    p_address VARCHAR(30),
    p_phone CHAR(11),
    hospital_address VARCHAR(20),
    PRIMARY KEY(p_id)
);

CREATE TABLE blood_delevery(
    bb_id INT,
    p_id INT,
    FOREIGN KEY(bb_id) REFERENCES blood_bank(bb_id),
    FOREIGN KEY(p_id) REFERENCES patient(p_id)
);


"""

myCursor.execute(sql_command)
mydb.commit()
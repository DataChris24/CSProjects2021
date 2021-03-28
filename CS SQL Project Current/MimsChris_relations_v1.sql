CREATE TABLE business (
    bus_id          CHAR(22)    NOT NULL   PRIMARY KEY,
    bus_name        VARCHAR(50) NOT NULL,
    bus_address     VARCHAR(50) NOT NULL,
    bus_city        VARCHAR(30) NOT NULL,
    bus_state       CHAR(2)     NOT NULL,
    bus_zip         CHAR(5)     NOT NULL,
    bus_lat         CHAR(21)    NOT NULL,
    bus_long        CHAR(21)    NOT NULL,
    bus_isOpen      BOOLEAN
);

CREATE TABLE yelpUser (
    user_id         CHAR(22)    NOT NULL    PRIMARY KEY,
    user_name       VARCHAR(50) NOT NULL,
    user_yelpstart  DATE        NOT NULL,
);

CREATE TABLE review (
    review_id           CHAR(22)    NOT NULL    PRIMARY KEY,
    review_userId       CHAR(22)    NOT NULL,
    reivew_businessId   CHAR(22)    NOT NULL,
    review_stars        INTEGER     NOT NULL,
    review_date         DATE        NOT NULL,
    review_text         TEXT        NOT NULL,
    review_useful       INTEGER     NOT NULL,
    review_funny        INTEGER     NOT NULL,
    review_cool         INTEGER     NOT NULL,
    CONSTRAINT fk_review_yelpuser FOREIGN KEY(review_userId) REFERENCES yelpUser(user_id),
    CONSTRAINT fk_review_business FOREIGN KEY(reivew_businessId) REFERENCES business(bus_id)
);

CREATE TABLE friendship (
    friendship_yelpUser1   CHAR(22)    NOT NULL,
    friendship_yelpUser2   CHAR(22)    NOT NULL,
    CONSTRAINT pk_friendship PRIMARY KEY(friendship_yelpUser1, friendship_yelpUser2),
    CONSTRAINT fk_friendship_yelpUser1  FOREIGN KEY(friendship_yelpUser1) REFERENCES yelpUser(user_id),
    CONSTRAINT fk_friendship_yelpUser2  FOREIGN KEY(friendship_yelpUser2) REFERENCES yelpUser(user_id)
);

CREATE TABLE check_in (
    ci_businessId       CHAR(22)    NOT NULL,
    ci_day_of_week      CHAR(9)     NOT NULL,
    ci_hour             TIME        NOT NULL,
    ci_count            INTEGER     NOT NULL,
    CONSTRAINT pk_check_in PRMARY KEY(ci_businessId, ci_day_of_week, ci_hour),
    CONSTRAINT fk_check_in_business FOREIGN KEY(ci_businessId) REFERENCES business(bus_id)
);
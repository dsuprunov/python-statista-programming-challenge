CREATE VIEW person_as_csv AS
SELECT
    person.age AS age,
    working_class.working_class AS workclass,
    person.final_weight AS fnlwgt,
    education.education AS education,
    education.years AS "educational-num",
    marital_status.marital_status AS "marital-status",
    occupation.occupation AS occupation,
    family_relationship.family_relationship AS relationship,
    race.race AS race,
    gender.gender AS gender,
    person.capital_gain AS "capital-gain",
    person.capital_loss AS "capital-loss",
    person.hours_per_week AS "hours-per-week",
    country.country AS "native-country",
    income.income AS income
FROM
    person
LEFT JOIN
    country ON country.id = person.native_country_id
LEFT JOIN
    gender ON gender.id = person.gender_id
LEFT JOIN
    race ON race.id = person.race_id
LEFT JOIN
    occupation ON occupation.id = person.occupation_id
LEFT JOIN
    income ON income.id = person.income_id
LEFT JOIN
    family_relationship ON family_relationship.id = person.family_relationship_id
LEFT JOIN
    marital_status ON marital_status.id = person.marital_status_id
LEFT JOIN
    education ON education.id = person.education_id
LEFT JOIN
    working_class ON working_class.id = person.working_class_id
;

SELECT
    *
FROM
    person_as_csv
LIMIT
    0, 5
;
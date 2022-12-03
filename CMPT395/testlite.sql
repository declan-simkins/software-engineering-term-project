insert into user_myuser
(id, password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
values (1, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 1, 'admin', 'John', 'Doe', 'email@email.com', 1, 1, '2018-03-25 19:50:40.005625'),
(2, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(3, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family2', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(4, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family4', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(5, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family3', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(6, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family14', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(7, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family5', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(8, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family6', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(9, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family7', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(10, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family8', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(11, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family9', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(12, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family10', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(13, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family11', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(14, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family12', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
(15, 'pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'family13', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625');

insert into user_family (familyID, family_name, email, user_id)
values (1, 'admin', 'email@email.com', 1),
(2, 'family1', 'email@email.com', 2),
(3, 'family2', 'email@email.com', 3),
(4, 'family3', 'email@email.com', 4),
(5, 'family4', 'email@email.com', 5),
(6, 'family5', 'email@email.com', 6),
(7, 'family6', 'email@email.com', 7),
(8, 'family7', 'email@email.com', 8),
(9, 'family8', 'email@email.com', 9),
(10, 'family9', 'email@email.com', 10);

insert into user_volunteer (volunteerID, first_name, last_name, email, family_id)
values (3, 'volunteer1', 'Smith', 'email@email.com', 2),
(4, 'volunteer1', 'Smith', 'email@email.com', 3),
(5, 'volunteer1', 'Smith', 'email@email.com', 4),
(6, 'volunteer1', 'Smith', 'email@email.com', 5),
(7, 'volunteer2', 'Smith', 'email@email.com', 5),
(8, 'volunteer1', 'Smith', 'email@email.com', 6),
(9, 'volunteer1', 'Smith', 'email@email.com', 7),
(10, 'volunteer1', 'Smith', 'email@email.com', 8);


insert into user_child (childID, first_name, last_name, classroom, family_id)
values (1, 'child1', 'last1', 'red', 2),
(2, 'child2', 'last1', 'blue', 2),
(3, 'child1', 'last3', 'red', 3),
(4, 'child1', 'last4', 'red', 4),
(5, 'child1', 'last5', 'red', 5),
(6, 'child1', 'last6', 'red', 6),
(7, 'child1', 'last7', 'red', 7),
(8, 'child1', 'last8', 'green', 8),
(9, 'child2', 'last8', 'grey', 8),
(10, 'child3', 'last8', 'blue', 8),
(11, 'child4', 'last8', 'blue', 8);



insert into user_signup (signupID, date, start_time, end_time, classroom, volunteer_id)
values (1, '2018-03-25', '8:30:00', '9:00:00', 'red', 3),
(2, '2018-03-25', '8:30:00', '9:00:00', 'red', 4),
(3, '2018-03-25', '8:30:00', '9:00:00', 'blue', 5),
(4, '2018-03-25', '8:30:00', '9:00:00', 'blue', 6),
(5, '2018-03-25', '8:30:00', '9:00:00', 'red', 7),
(6, '2018-03-25', '12:00:00', '13:00:00', 'red', 8),
(7, '2018-03-25', '12:00:00', '13:00:00', 'yellow', 9),
(8, '2018-03-25', '12:00:00', '13:00:00', 'green', 10),
(9, '2018-03-25', '13:30:00', '15:00:00', 'red', 6),
(10, '2018-03-25', '13:30:00', '15:00:00', 'red', 5),
(11, '2018-03-27', '13:30:00', '15:00:00', 'red', 4),
(12, '2018-03-25', '8:30:00', '9:00:00', 'blue', 10),
(13, '2018-03-26', '13:30:00', '15:00:00', 'red', 3);


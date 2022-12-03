insert into 395db.user_myuser
(password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
values ('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 1, 'admin', 'John', 'Doe', 'email@email.com', 1, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'smith1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'jones1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'trump1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'doe1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'bond1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'morgan1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'west1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625');

insert into 395db.user_family (family_name, email, user_id)
values ('Admin', 'email@email.com', 1),
('Smith', 'email@email.com', 2),
('Jones', 'email@email.com', 3),
('Trump', 'email@email.com', 4),
('Doe', 'email@email.com', 5),
('Bond', 'email@email.com', 6),
('Morgan', 'email@email.com', 7),
('West', 'email@email.com', 8);


insert into 395db.user_volunteer (first_name, last_name, email, family_id)
values ('Tom', 'Smith', 'email@email.com', 2),
('Jack', 'Jones', 'email@email.com', 3),
('Jill', 'Jones', 'email@email.com', 3),
('Tracy', 'McNanny', 'nany@email.com', 3),
('Donald', 'Trump', 'email@email.com', 4),
('John', 'Doe', 'email@email.com', 5),
('Dianna', 'Black', 'email@email.com', 5),
('Tina', 'Bond', 'email@email.com', 6),
('Tammy', 'West', 'email@email.com', 8),
('Mark', 'Morgan', 'email@email.com', 7),
('Sally', 'Morgan', 'email@email.com', 7),
('Admin', '1', 'admin@email.com', 1);


insert into 395db.user_child (first_name, last_name, classroom, family_id)
values ('Timmy', 'Smith', 'red', 2),
('Jane', 'Smith', 'blue', 2),
('Tommy', 'Jones', 'red', 3),
('Jr.', 'Trump', 'green', 4),
('Jane', 'Doe', 'blue', 5),
('Charlie', 'Smith', 'red', 6),
('Sally', 'Morgan', 'blue', 7),
('Chuck', 'West', 'green', 8),
('Jim', 'West', 'green', 8),
('Stacy', 'Park', 'blue', 8),
('Sally', 'Bond', 'red', 8);



insert into 395db.user_signup (date, start_time, end_time, classroom, volunteer_id)
values ('2018-04-04', '8:45:00', '11:00:00', 'Red', 3),
('2018-04-04', '8:50:00', '10:00:00', 'Green', 10),
('2018-04-04', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-04', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-04', '13:00:00', '15:45:00', 'Blue', 7),
('2018-04-04', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-04', '12:00:00', '12:45:00', 'Blue', 9),
('2018-04-04', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-04', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-05', '8:50:00', '11:00:00', 'Red', 3),
('2018-04-05', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-05', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-05', '12:50:00', '15:00:00', 'Red', 10),
('2018-04-05', '13:00:00', '15:45:00', 'Blue', 7),
('2018-04-05', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-05', '12:00:00', '12:45:00', 'Blue', 9),
('2018-04-05', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-05', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-06', '8:50:00', '11:00:00', 'Red', 3),
('2018-04-06', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-06', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-06', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-06', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-06', '12:00:00', '12:45:00', 'Blue', 8),
('2018-04-06', '12:00:00', '12:45:00', 'Blue', 9),
('2018-04-06', '12:00:00', '12:45:00', 'Green', 10),
('2018-04-06', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-09', '8:50:00', '11:00:00', 'Red', 3),
('2018-04-09', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-09', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-09', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-09', '13:00:00', '15:45:00', 'Blue', 10),
('2018-04-09', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-09', '12:00:00', '12:45:00', 'Blue', 9),
('2018-04-09', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-09', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-10', '8:50:00', '11:00:00', 'Red', 10),
('2018-04-10', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-10', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-10', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-10', '13:00:00', '15:45:00', 'Blue', 7),
('2018-04-10', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-10', '12:00:00', '12:45:00', 'Blue', 9),
('2018-04-10', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-10', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-11', '8:50:00', '11:00:00', 'Red', 3),
('2018-04-11', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-11', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-11', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-11', '13:00:00', '15:45:00', 'Blue', 7),
('2018-04-11', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-11', '12:00:00', '12:45:00', 'Blue', 10),
('2018-04-11', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-11', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-12', '8:50:00', '11:00:00', 'Grey', 3),
('2018-04-12', '8:50:00', '10:00:00', 'Grey', 4),
('2018-04-12', '8:50:00', '11:00:00', 'Grey', 5),
('2018-04-12', '12:50:00', '15:00:00', 'Grey', 6),
('2018-04-12', '13:00:00', '15:45:00', 'Grey', 10),
('2018-04-12', '12:00:00', '12:45:00', 'Grey', 8),
('2018-04-12', '12:00:00', '12:45:00', 'Grey', 9),
('2018-04-12', '12:00:00', '12:45:00', 'Purple', 1),
('2018-04-12', '13:30:00', '15:30:00', 'Purple', 2),
('2018-04-16', '8:50:00', '11:00:00', 'Red', 10),
('2018-04-16', '8:50:00', '10:00:00', 'Green', 4),
('2018-04-16', '8:50:00', '11:00:00', 'Blue', 5),
('2018-04-16', '12:50:00', '15:00:00', 'Purple', 6),
('2018-04-16', '13:00:00', '15:45:00', 'Purple', 7),
('2018-04-16', '12:00:00', '12:45:00', 'Purple', 8),
('2018-04-16', '12:00:00', '12:45:00', 'Purple', 9),
('2018-04-16', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-16', '13:30:00', '15:30:00', 'Green', 2),
('2018-04-13', '8:50:00', '11:00:00', 'Purple', 3),
('2018-04-13', '8:50:00', '10:00:00', 'Purple', 4),
('2018-04-13', '8:50:00', '11:00:00', 'Purple', 5),
('2018-04-13', '12:50:00', '15:00:00', 'Red', 6),
('2018-04-13', '13:00:00', '15:45:00', 'Blue', 7),
('2018-04-13', '12:00:00', '12:45:00', 'Red', 8),
('2018-04-13', '12:00:00', '12:45:00', 'Purple', 10),
('2018-04-13', '12:00:00', '12:45:00', 'Green', 1),
('2018-04-13', '13:30:00', '12:45:00', 'Green', 2);

insert into 395db.fieldtrip_fieldtrip (title, location, info, classes, date)
values ('Waterpark', 'WEM', 'Please bring bathing suits', 'Red, Green, Purple', '2018-04-13'),
('Picnic', 'Park', 'Please bring food', 'Blue, Grey, Red', '2018-04-27'),
('Animal Studies', 'Zoo', 'Wear sunscreen', 'All', '2018-05-04');

insert into 395db.fieldtrip_fieldtripsignup (trip_id, volunteer_id)
values (1, 3),
(1, 7),
(1, 9),
(1, 1),
(2, 2),
(2, 4),
(3, 5),
(3, 6),
(3, 8),
(3, 10);

insert into 395db.weeklycalendar_classroom (title, color)
values ('Red', 'Red'),
('Grey', 'Grey'),
('Blue', 'Blue'),
('Green', 'Green'),
('Purple', 'Purple');

insert into 395db.weeklycalendar_timeslot (title, start, end, multiplier)
values ('Morning', '8:45:00', '11:50:00', 1),
('Lunch', '11:50:00', '13:00:00', 2),
('Afternoon', '12:50', '15:45', 1);


insert into 395db.timeoffrequests_timeoffrequest (start_date, end_date, reason_for_time_off, status, family_id)
values ('2018-04-16', '2018-04-22', 'Golf trip', 'p', 4),
('2018-04-23', '2018-04-29', 'Funeral', 'p', 2),
('2018-04-23', '2018-04-29', 'Vacation', 'p', 8);


insert into 395db.user_timetransfer (date, time, from_family_id, to_family_id)
values ('2018-04-10', '2:00', 7, 8),
('2018-04-10', '1:30', 5, 4),
('2018-04-10', '1:00', 3, 2);








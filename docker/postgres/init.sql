CREATE TABLE days(
  id serial,
  name varchar(255),
  primary key(id)
);
INSERT INTO days(name)
VALUES ('Sunday'), ('Monday'), ('Tuesday'), ('Wednesday'), ('Thursday'), ('Friday'), ('Friday'), ('Saturday');

CREATE TABLE genders(
  id serial,
  name varchar(255),
  primary key(id)
);
INSERT INTO genders(name)
VALUES ('male'), ('female'), ('nonbinary');

CREATE TABLE memberships(
  id serial,
  name varchar(255),
  primary key(id)
);
INSERT INTO memberships(name)
VALUES ('YWCA'), ('YMCA');

CREATE TABLE times(
  id serial,
  name varchar(255),
  primary key(id)
);
INSERT INTO times(name)
VALUES ('early morning'), ('late morning'), ('afternoon'), ('evening'), ('night'), ('late night');

CREATE TABLE workouts(
  id serial,
  name varchar(255),
  primary key(id)
);
INSERT INTO workouts(name)
VALUES ('cardio'), ('strength'), ('team sports'), ('group classes');

CREATE TABLE users(
  id serial,
  name varchar(255),
  email varchar(255),
  gender_id serial,
  primary key(id),
  foreign key(gender_id) references genders(id)
);
INSERT INTO users(name, email, gender_id)
VALUES ('Jordan', 'f1@user.com', 1), ('Avery', 'm1@user.com', 2);

CREATE TABLE messages(
  id serial,
  user_id_0 int,
  user_id_1 int,
  pending boolean,
  primary key (id),
  foreign key (user_id_0) references users(id),
  foreign key (user_id_1) references users(id)
);
INSERT INTO messages(user_id_0, user_id_1, pending)
VALUES (1, 2, true);

CREATE TABLE membership_locations(
  id serial,
  membership_id int,
  location varchar(255),
  primary key (id),
  foreign key (membership_id) references memberships(id)
);
INSERT INTO membership_locations(membership_id, location)
VALUES (1, 'Uptown'), (1, 'Midtown'), (1, 'Downtown');

CREATE TABLE user_memberships(
  id serial,
  user_id serial,
  membership_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (membership_id) references memberships(id)
);
INSERT INTO user_memberships(user_id, membership_id)
VALUES (1, 1);

CREATE TABLE user_pref_days(
  id serial,
  user_id serial,
  day_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (day_id) references days(id)
);
INSERT INTO user_pref_days(user_id, day_id)
VALUES (1, 1);

CREATE TABLE user_pref_genders(
  id serial,
  user_id serial,
  gender_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (gender_id) references genders(id)
);
INSERT INTO user_pref_genders(user_id, gender_id)
VALUES (1, 1);

CREATE TABLE user_pref_locations(
  id serial,
  user_id serial,
  membership_location_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (membership_location_id) references membership_locations(id)
);
INSERT INTO user_pref_locations(user_id, membership_location_id)
VALUES (1, 1);

CREATE TABLE user_pref_times(
  id serial,
  user_id serial,
  time_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (time_id) references times(id)
);
INSERT INTO user_pref_times(user_id, time_id)
VALUES (1, 1);

CREATE TABLE user_pref_workouts(
  id serial,
  user_id serial,
  workout_id serial,
  primary key (id),
  foreign key (user_id) references users(id),
  foreign key (workout_id) references workouts(id)
);
INSERT INTO user_pref_workouts(user_id, workout_id)
VALUES (1, 1);

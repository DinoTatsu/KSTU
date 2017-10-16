use TWDB;

create table notes(
	noteID int identity(1, 1) not null,
	created date,
	title varchar(20),
	article varchar(255),
	constraint PK_notesID primary key (noteID)
)

create table comments(
	commentID smallint identity(1, 1) not null,
	created date,
	author varchar(20),
	comment varchar(256),
	art_id smallint,
	constraint PK_commentsID primary key (commentID)
)
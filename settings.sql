drop database if exists superhero_database_app;
drop role if exists superherousernew;
CREATE DATABASE superhero_database_app;
CREATE USER superherousernew WITH PASSWORD 'superhero_database_app';
GRANT ALL PRIVILEGES ON DATABASE superhero_database_app TO superherousernew;
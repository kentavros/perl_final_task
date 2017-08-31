#!D:\Dwimperl\perl\bin\perl.exe

use strict;
use warnings;
use Data::Dumper;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Utils::Db;

my $q=CGI->new;
print $q->header;

# FORRR TEST ONLY!!!!!

my $dbh=Utils::Db->new();
#my $query = "SELECT * FROM users";
#print Dumper($dbh->select($query));

#my $queryUpdate = 'UPDATE users SET name=\'Fedr\', email=\'fedr@email.ru\', pass=\'555555\' WHERE id=2';
#$dbh->update($queryUpdate);

#my $queryIns = 'INSERT INTO user (name, email, pass) VALUES (\'kostia3\', \'kostia3@email.com\', \'password3456789\')';
#$dbh->insert($queryIns);

my $qeruDel = 'DELETE FROM users WHERE id=5';
$dbh->delete($qeruDel);
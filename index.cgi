#!/usr/bin/perl -w

####!D:\Dwimperl\perl\bin\perl.exe

use strict;
use warnings;
use Data::Dumper;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Utils::Db;
use Utils::Validate;

my $q=CGI->new;
print $q->header;

# FORRR TEST ONLY!!!!!
#print 'test';
my $dbh=Utils::Db->new();
#my $query = "SELECT * FROM users";
#print Dumper($dbh->select($query));

#my $queryUpdate = 'UPDATE users SET name=\'Fedr\', email=\'fedr@email.ru\', pass=\'555555\' WHERE id=2';
#$dbh->update($queryUpdate);

#my $queryIns = 'INSERT INTO user (name, email, pass) VALUES (\'kostia3\', \'kostia3@email.com\', \'password3456789\')';
#$dbh->insert($queryIns);

#my $qeruDel = 'DELETE FROM users WHERE id=5';
#$dbh->delete($qeruDel);

my $valid=Utils::Validate->new();
#if ($valid->valEmail(' SasSSSha671@yandex.ru '))
#{print 'true____!'}

#if ($valid->valPass(' asdssdsdf1234 '))
#{print 'true!!!'}


#if($valid->valName('<br> Sasha '))
#{print 'True';}

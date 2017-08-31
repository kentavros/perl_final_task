package Utils::Validate;

use strict;
use warnings;
use Data::Dumper;

sub new
{
    my $class = ref($_[0])||$_[0];
    return bless {}, $class;
}

sub valName
{

}

sub valEmail
{
    my ($self, $email) = @_;
    $email = lc($email);
    #tag delete
    $email =~s/<(?:[^>'"]*|(['"]).*?\1)*>//gs;
    #space delete
    $email =~ s/^\s+|\s+$//g;
    my $pattern = qr/^[a-z0-9_\.\-]+\@([a-z0-9\-]+\.)+[a-z]{2,4}$/;
    my $errors = '';
    if ($email !~ /$pattern/i){
        $errors .= 'Invalid email address!<br>';
    }
    if (length($email) > 50)
    {
        $errors .='Length email over 50 characters!<br>';
    }
    if ($errors eq '')
    {
        return $email;
    }
    else
    {
        return $errors;
    }
}

sub valPass
{
    my ($self, $pass) = @_;
    my $errors = '';
    #tag delete
    $pass =~s/<(?:[^>'"]*|(['"]).*?\1)*>//gs;
    #space delete
    $pass =~ s/^\s+|\s+$//g;
    if ($pass !~ /^[a-z0-9_\-]{6,16}$/i)
    {
        $errors .='Only letters and numbers are allowed in the password!<br>';
    }
    if (length($pass) > 16 || length($pass) < 6)
    {
        $errors .='Password length must be greater than 6 or less than 16 characters<br>';
    }
    if ($errors eq '')
    {
        return $pass;
    }
    else
    {
       return $errors;
    }
}
#user6
1;
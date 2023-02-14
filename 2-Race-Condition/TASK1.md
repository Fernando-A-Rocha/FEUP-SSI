# Nando

## Task 1: Choosing Our Target

By editing the `etc/passwd` file with a superuser, we can add a new user with a set name, UID and password by creating a new line.

`test:U6aMy0wojraho:0:0:test:/root:/bin/bash`

This makes a user with ID 0 and a magic password which is a string that we know will allow us to login with no password. We can login using `su test` and pressing Enter. We confirm that this user has root privileges.

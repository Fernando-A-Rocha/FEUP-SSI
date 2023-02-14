# Race-Condition Vulnerability Lab

[https://seedsecuritylabs.org/Labs_20.04/Software/Race_Condition/](https://seedsecuritylabs.org/Labs_20.04/Software/Race_Condition/)

## Work

Part of the **SSI Course Unit** at [FEUP](https://sigarra.up.pt/feup/en/WEB_PAGE.INICIAL).

**Team**:

- João Pedro Rodrigues da Silva [[up201906478]](mailto:up201906478@edu.fe.up.pt);
- António Bernardo Linhares Oliveira [[up202204184]](mailto:up202204184@edu.fe.up.pt);
- Fernando Adriano Ramalho Rocha [[up202200589]](mailto:up202200589@edu.fe.up.pt).

The group has followed the instructions on the lab page, and has documented the process as well as the answers to the questions indicated in the lab tasks.

## Task 1: Choosing Our Target

By editing the `etc/passwd` file with a superuser, we can add a new user with a set name, UID and password by creating a new line.

`test:U6aMy0wojraho:0:0:test:/root:/bin/bash`

This makes a user with ID 0 and a magic password which is a string that we know will allow us to login with no password. We can login using `su test` and pressing Enter. We confirm that this user has root privileges.

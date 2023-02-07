# 1. Shellshock Attack Lab

[https://seedsecuritylabs.org/Labs_20.04/Software/Shellshock/](https://seedsecuritylabs.org/Labs_20.04/Software/Shellshock/)

Around 2014, bash received an update which fixed the "shellshock" vulnerability. This allowed you to define environment variables that would be executed by bash (on new shell creation, it tried to convert environment variables into eventual functions). This was a huge security issue because it allowed you to execute arbitrary code on the server. This lab will teach you how to exploit this vulnerability.

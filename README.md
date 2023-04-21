<h1 align="center"><p><img src="http://assets.tira.io/tira-icons/tira-logo-32px-white.png" style="vertical-align:bottom"> TIRA Integrated Research Architecture </p></h1>


This repository contains the source code for all components of the [TIRA](https://www.tira.io) shared task platform.

## Setup Your Local Development Environment

First, please clone the repository:
```
git clone git@github.com:tira-io/tira.git
```

Please change your directory to `application`:
```
cd application
```

Install your virtual environment via:
```
make setup
```

If you want to work on production data, please ensure that you can login to ssh.webis.de, and then do the following:

```
scp scp <YOUR-USER-NAME>@ssh.webis.de:/mnt/ceph/storage/data-in-production/tira/development-database-dumps/django-db-dump.zip .data-dumps/django-db-dump.zip

# The zip is password protected, the process asks for the passord.
# A member of the TIRA team can provide you with the password (located in the password database `webis.uni-weimar.de:code-admin/passwords` -> Generic -> tira-development-database-dump).
make import-data-from-dump
```

Then, to start TIRA locally, please start:

```
make webpack-watch
```

and 

```
make run-develop
```

Then, you can point your browser to the specified URL.

## Resources
* [Wiki](../../wiki): Getting started with TIRA as a developer/administrator
* [User Docs](https://www.tira.io/t/getting-started/1364): Getting started with TIRA as a user
* [Papers](https://webis.de/publications.html?q=tira): List of publications
* [Contribution Guide](CONTRIBUTING.md): How to contribute to the TIRA project

## Create New Zip of the Database Dump

Go the the password database `webis.uni-weimar.de:code-admin/passwords` -> Generic -> tira-development-database-dump

```
cd /mnt/ceph/storage/data-in-production/tira/development-database-dumps/
zip --encrypt django-db-dump-<DATE>.zip /mnt/ceph/tira/state/db-backup/django-db-dump-<DATE>.json
ln -s django-db-dump-<DATE>.zip django-db-dump.zip
```

## Paper

If you use TIRA in your own research, please be sure to cite our paper

```
@InProceedings{froebe:2023b,
  address =                  {Berlin Heidelberg New York},
  author =                   {Maik Fr{\"o}be and Matti Wiegmann and Nikolay Kolyada and Bastian Grahm and Theresa Elstner and Frank Loebe and Matthias Hagen and Benno Stein and Martin Potthast},
  booktitle =                {Advances in Information Retrieval. 45th European Conference on {IR} Research ({ECIR} 2023)},
  month =                    apr,
  publisher =                {Springer},
  series =                   {Lecture Notes in Computer Science},
  site =                     {Dublin, Irland},
  title =                    {{Continuous Integration for Reproducible Shared Tasks with TIRA.io}},
  todo =                     {doi, month, pages, code},
  year =                     2023
}
```
## License

[MIT License](LICENSE)

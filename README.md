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

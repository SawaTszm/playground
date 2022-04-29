# sample-poetry

## Installing

```bash
$pip install poetry
```

## Create New Project

```bash
$poetry new sample-project
```

This will create the following files and folders:

```txt
sample-project
├── README.rst
├── pyproject.toml
├── sample_project
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_sample_project.py
```

## Add New Dependency

```bash
$cd sample-project
$poetry add [--dev] <package name>
```

This downloads and install a dependency inside the virtual environment managed by Poetry,  
and adds or updates `poetry.lock` file, and updates `pyproject.toml`.

## Remove Deoendency

```bash
$poetry remove <package name>
```

This is very simple :)

## Use Virtual Environment

```bash
# not active
$poetry run python -m pytest

# active
$poetry shell
```

## Use Exsting Environment

```bash
$poetry install [--no-dev]
```

## Reference

[Poetry - Python dependency management and packaging made easy.](https://python-poetry.org/)  
[GitHub - python-poetry/poetry: Python dependency management and packaging made easy.](https://github.com/python-poetry/poetry)  
[Modern Python Environments - dependency and workspace management | TestDriven.io](https://testdriven.io/blog/python-environments/)  

## めも

Pipenvなんかにはないスマートな依存関係の解決ができるよって言ってる  
確かに`pipenv uninstall`は依存関係を見てないし、言われてみればinstallでコケることも割とあるので、
`poetry remove`とそのスマートさがよしなにしてくれるなら嬉しいなーという感じ  

参考：[Pipenv uninstallよりcleanの方が多分便利 - Qiita](https://qiita.com/eduidl/items/c0e8256bb3a5a735d19c)  

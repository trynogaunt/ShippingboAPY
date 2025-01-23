# ShippingboAPY

Welcome to the ShippingboAPY project! This README will guide you through the setup and usage of the project.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

ShippingboAPY is a Python library designed to facilitate integration with the Shippingbo API. It allows developers to easily access Shippingbo features such as product management, order handling, and shipping directly from their Python applications. Whether you are a beginner or an experienced developer, ShippingboAPY offers a simple and intuitive interface to interact with the Shippingbo API.

## Installation

To get started with ShippingboAPY, follow these steps:

```sh
 # Linux/MacOS
 python -m pip install -U shippingboapy

 # Windows
 py -3 -m pip install -U shippingboapy
```

## Usage

```py
import shippingboapy

api = shippingboapy 

products = api.get_products()

for product in products
    print(product)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
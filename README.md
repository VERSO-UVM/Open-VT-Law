# Open VT Law

## Overview
Currently Vermont legal statutes are publically stored as html [The Vermont Statutes Online](https://legislature.vermont.gov/statutes/), and amendments (Bill & Resolutions) are seperate documents that call out specific changes seperate from the law. We believe this both makes it much harder to understand how law changes over time, and is prevents easy computational analysis that could help us understand the current and potential future implications of law.

Interesting Read: [Democratizing the Law with Open Data](https://law.mit.edu/pub/democratizingthelawwithopendata/release/2)

Open VT Law is an open-source project designed to simplify the process of extracting information from html containing Vermont Statutes and Laws and place it into structured json format as well as a simple single text format for reading. The goal of this tool is to automate the process of downloading the statutes from the State of Vermont website, convert those into a single txt file and a json file with metadata. Additional goals are using the version control to demostrate a new way to view amendments as a pull request. The hope is to then demo this to the State of Vermont and propose new ways that they can publically share the law.

## Features
html to Text Conversion: Efficiently extracts text from The Vermont Statutes Online and add to a single txt file.
Structured JSON Output: Transforms the extracted text into a well-organized JSON format for easy data manipulation.
Add metadate: Add labels that help enrich the text
Process Bills: Create pull requests that show the proposed changes by bills in session

## Getting Started
Prerequisites
Python 3.x

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/VERSO-UVM/Open-VT-Law.git


## Usage
Download Vermont Statutes and Laws html files from the State of Vermont page 
Save to a single txt file in the txt folder
Run py script for converting to json
Find the generated JSON files in the json_output directory.

## Contributing
We welcome contributions! Please follow our [Contribution Guidelines](https://github.com/VERSO-UVM/Open-VT-Law/blob/main/CONTRIBUTING.md) to get started.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/VERSO-UVM/Open-VT-Law/blob/main/LICENSE) file for details.

## Acknowledgments
Special thanks to the State of Vermont for their public access to Vermont Statutes

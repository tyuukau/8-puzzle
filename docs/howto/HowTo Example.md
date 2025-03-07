# How to Add a HowTo in Config File

## Introduction
This guide will walk you through the process of adding a HowTo in a config file. This involves using the `args` property to inject properties into a liquid template and the `file` property to append the extracted content of a file to a liquid template. 

## Step-by-Step Instructions

1. **Understand the `args` property**: The `args` property is used to inject properties into a liquid template. Any property set in `args` can be accessed in the liquid template.

2. **Understand the `file` property**: The `file` property appends the extracted content of a file to a liquid template. This is done using JSONPath or the `extract` property that uses LLM to extract content from the file.

3. **Create a liquid template**: Developers must create a liquid template in the `.code-narrator/gpt_questions` directory. This template file is used to ask GPT questions.

:::note
Remember to replace any secret information with ***** to maintain security.
:::

By following these steps, developers can successfully add a HowTo in a config file.
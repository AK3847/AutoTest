# *Auto~Test*

## Prompt Strategy:
- Find the prompt [here](instruction_prompt.txt)
- I have used Test Case writing strategy as given here [BrowserStack](https://www.browserstack.com/guide/how-to-write-test-cases), [Coursera](https://www.coursera.org/articles/how-to-write-test-cases) and [testsigma](https://testsigma.com/guides/test-cases-for-manual-testing/)

- To prevent the LLM from deviating outside the given Task,I have added: 
    > Follow the given Test Case Template closely and avoid generating any extra text. 

- To prevent the LLM from over-memeriozing the facts/data given in the images and focus more on the funcionality, I have added: 
    > Do not hardcode the data show in the images, it's for showing purpose only, generalize the Test Cases by Focusing on the Feature that's been show in the images

- To Generate the Output in Markdown format, which is much easier to read and display, I have modified the Test Case accordingly: [check the template](instruction_prompt.txt) and each field's format in it.

- I have added one example in ``Test Steps`` as *One-Shot prompting* to get better results.

## Python-Packages:
> See the requirements in [requirements.txt](requirements.txt)
```bash
    Flask
    openai
```
## Screenshots:
![Web-Interface](/screenshots/image.png)
![Generated-Output-1](/screenshots/image1.png)
![Generated-Output-2](/screenshots/image2.png)


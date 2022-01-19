# Markdown Syntax and Tips

[Here is a link to a markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

<br>

## Headers
---

Use ```#``` at the start of a line to create Headers.  
There are 6 sizes of headers, use ```#```, ```##``` etc. to get different sizes.  
The largest size is automatically underlined.  
Use ```---``` to create an underline / line break manually.

> # Header 1
> ## Header 2
> ### Header 3
> #### Header 4
> ##### Header 5
> ###### Header 6

<br>

## Writing code
---

Use \```python  
write  
python  
code  
here```   
to create a code block.

```python
def greeting():
    print("Hello World")
```

<br>

## Fonts
---

\*Italics* --> *Italics*

\*\*Bold** --> **Bold**

\*\*\_Bold and Italics_** --> **_Bold and Italics_**

\~\~Strikethrough~~ --> ~~Strikethrough~~

<br>

## Lists
---

Use ```1. 2.``` etc. for ordered lists.
1. Ordered item 1
2. Ordered item 2


Use ```*``` for unordered lists.
* Unordered item 1
* Unordered item 2

It's possible to nest lists. Just indent the line appropriately
1. item
    * item
    * item
2. item
    * item
        * item

<br>

## Block Quote
---
Use ```>``` at the start of a line to make a block quote. Use it at the start of multiple successive lines to make a multi line block quote

> This is a block quote. It's super cool.  
> It's good for grouping and/or highlighting blocks of text.

<br>

## Links
---
syntax ---> \[Take me to google]\(https://google.com "Hover text")

[Take me to google](https://google.com "Hover text")

<br>

## Images
---
Inline style syntax ---> \!\[alt text](image.png "Hover text")  
![Markdown symbol](markdown_logo.png "Markdown Logo")

Reference style syntax   
---> \!\[alt text]\[Logo]  
---> \[Logo]: markdown_logo.png "Hover text"

![alt text][logo]  

[logo]: markdown_logo.png "Hover text"

<br>

## Tables  
---
Using pipes and dashed you can create tables.  
  
  
\| col1 | col2 | col3 |  
\| --- |:---:| ---:|  
\|val1 |val2 |val3 |  
\|left aligned|center aligned|right aligned|

|col1 |col2 |col3 |  
| --- |:---:| ---:|
|val1 |val2 |val3 |
|left aligned|center aligned|right aligned|
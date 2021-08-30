# Keep Figures Close To Corresponding Text

Do your best to keep the text and the corresponding figures close to each other. 
Ideally the figure and the explanatory text should be on the same page. Rarely it can be on a different page, but there has to be a strong reason for that. 

Tricks that you can use to bring figures closer to text:

- in LaTeX you can use the [h!] parameter for includegraphics - this instructs LaTeX to try to move the image at that very spot in the document flow (h stands for here!)
- you can sometimes force start a new section on a new page by using ```\newline``` in order to allow a figure and associated text to be on the same page. A reader will forgive you for the extra empty space at the bottom of the previous pavge, if he does not have to go back and forth in your document to understand it. 

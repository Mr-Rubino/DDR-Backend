# Backend for EduVision

EduVision+ is an iOS application that allows users to scan text from documents and extracts summaries and relevant Wikipedia links. 
The app uses Vision and VisionKit frameworks for OCR, and a custom backend for processing the scanned text.



## /summarize endpoint (POST)

Generates a summary based on a given text


<b> Form Arguments: </b>
* String text: text to retrieve dbpedia sources from

<b> Returns: </b>
* JSON summary: JSON object of the generated summary

## /questions endpoint (POST)

Generates 3 multiple choice questions based on a given text

<b> Form Arguments: </b>
* String text: text to retrieve dbpedia sources from

<b> Returns: </b>
* JSON questions: JSON object of the generated questions and answers


## /wiki endpoint (POST)

Finds dbpedia links in a given text using the NLP program

<b> Form Arguments: </b>
* String text: text to retrieve dbpedia sources from
* String language: language abbreviation according to ISO 639-1

<b> Returns: </b>
* JSON wikiLinks: JSON object of the found dbpedia articles
# Women’s Underrepresentation in the news quotations.
## File Description

+ `data_analysis.ipynb`: Conducting some basic analyze of processed QuoteBank data.
+ `data_preprocess.ipynb`: Preprocessing the original QuoteBank data.
+ `generate_mapper.ipynb`: Generate the mapper that map Qids in QuoteBank data into real values.
+ `keyword_analyze.ipynb`: Extract different topics according to predefined keywords, and analyze the sentiments for each topic.
+ `grouped_gender.ipynb`: For different news outlets, speaker's nationality and party, group them monthly according to different genders.
+ `gender_freq.ipynb`: Generate the frequencies of speaker, # occurrences, and # of quotations.

## Abstract

Gender bias in the news media has received increasing attention, and the differences introduced by gender in news coverage have been examined from a variety of perspectives. 
However, quotation–which is widespread in all types of news coverage–has not received enough attention. 
Quotes are simple, direct, and accurate reflections of the speaker's point of view, and quoted information in the news allows us to explore gender bias in the news from a fresh angle.

Thus, we then introduce a new set of questions: Do male speakers speak truly more “louder” than females? If it is true, is this caused by news coverage or just the gender itself?
Furthermore, can we infer the portraits of each gender statistically from quotations?

In short, our data story not only analyzes the preferences of various news media when quoting speakers from different genders, but also the influence of numerous parties and nationalities on gender bias.
In addition, we explore gender bias under self-defined topics and linguistic level to better understand the reasons behind the appearance of bias in quotations.
## Research Questions

We plan to continue our research in the following directions, and we list here various questions to go on exploring under each topic.

+ How gender bias is reflected under different topics.
+ What is the percentage of female politicians mentioned or quoted for each outlet, and the average across outlets?
+ What kind of topics do different genders focus on?
+ The difference of the media quoting sentences from males and females, and how they change over time.
+ Is gender discrimination aggravating or mitigating over time?

## Methods

- **log-log plot.** We applied the log-log plot method to check whether our data’s distribution follows the power law.
- **TF-IDF.** If we want to extract quotations about one topic, TF-IDF can be an easy and plausible method. In the beginning, we counted tokens’ frequency in quotations to observe the topics from the word itself. However, the effect wasn’t good, hence we discarded it and chose TF-IDF.
- **Tokenize and stemming.** The common way to analyse texts is by tokenizing them to obtain every single word. As words have different senses(e.g. have -- had, having), stemming is also necessary for better analysis. Here, we used NLTK(Natural Language Toolkit) for processing.
- **Combining variables with time/date.** A proper way to explore the trend for topics in subgroups(e.g. gender, party and publisher) is by observing the data over time. We aggregated the data by “date” and took week as a unit bin inste**ad of the day, aiming to reduce the fluctuation under fine-grained.
- **BERT for sentiment analyze.** We use the BERT model to classify quotations to different sentiments. 
- **Logistic Regression for linguistic analysis.** We use the Logistic Regression to predict the gender for a giving quotation. If the quotation style discrepancy between males and females is not as significant as we expected. then the model we developed would be equivalent to a random assumption (we cannot infer gender from what they say), i.e. 50%. But if the model works better than 50%. it indicates that there is indeed some bias in quotes made by different genders, which is therefore identified by the model as a discriminatory feature.

## Proposed timeline

- **Xiaoyu Chen**: Study subtopics of News bias, Partisan bias, Gender bias and finish data extraction functions.
- **Siyi Liu**: Apply data processing pipeline on Quotebank datasets with different years, discover valuable and interesting patterns based on it, and conceptualize the data story.
- **Xiaotian Su**: Visualize the data including histogram, line-chart, scatterplot, etc. Design the layout and visual style of the website, then realize it.
- **Xinyu Zhou**: Polish the data story to make it more intuitive and appealing. Check codes and documentation. Prepare the final presentation.




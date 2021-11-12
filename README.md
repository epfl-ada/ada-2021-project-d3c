# Revealing implicit media biases with news quotations

## File Description

+ `data_analysis.ipynb`: Conducting some basic analyze of processed QuoteBank data.
+ `data_preprocess.ipynb`: Preprocessing the original QuoteBank data.
+ `generate_mapper.ipynb`: Generate the mapper that map Qids in QuoteBank data into real values.

## Abstract

People are used to getting information from the media including newspapers and websites. However, readers might be misguided because different outlets possess dissimilar biases. Previous research may focus on media bias itself, however, we can also utilize the quotations to reveal such bias, which probably reflects hidden inequality and trends in the world. The Quotebank dataset provides us with a good opportunity to implement this idea.

With sufficient quotation-speaker pairs, we hope to find the hidden media bias behind the sentences through the topics they refer to and the speakers’ attributes (e.g. gender, party, etc.). Furthermore, quotations make it plausible to explore different variables changing patterns over time with many available NLP techniques. Eventually, we can unite different small blocks of analysis together and give an overview of the media bias. The user will be able to use our visualization tool to do searches about media biases.

## Research Questions

We plan to continue our research in the following three directions, and we list here various questions to go on exploring under each topic.

1. News bias

    - What are the most frequent topics quoted by each outlet every year?
    - What is the frequency of different newspapers reporting different political parties? And how do the frequencies change over time?
    - What are the top 10 quoted political figures for different media? How does this change over time?
    - Do newspapers tend to use neutral words (e.g. economic migrants) or discriminative words (e.g. refugees) in their quotations?

2. Partisan bias

    - What are the keywords for the same media reporting different political parties?
    - When referring to other or opposing parties, what are the most frequent words used by a political group?
    - What is the attitude of separate political parties towards the same topic (e.g. abortion, BLM)? Do they tend to agree or disagree with each other with time going by?

3. Gender bias

    - How gender bias is reflected under different topics.
    - What is the percentage of female politicians mentioned or quoted for each outlet, and the average across outlets?
    - What kind of topics do different genders focus on?
    - The difference of the media quoting sentences from males and females, and how they change over time.
    - Is gender discrimination aggravating or mitigating over time?

## Methods

- **log-log plot.** We applied the log-log plot method to check whether our data’s distribution follows the power law.
- **TF-IDF.** If we want to extract quotations about one topic, TF-IDF can be an easy and plausible method. In the beginning, we counted tokens’ frequency in quotations to observe the topics from the word itself. However, the effect wasn’t good, hence we discarded it and chose TF-IDF.
- **Tokenize and stemming.** The common way to analyse texts is by tokenizing them to obtain every single word. As words have different senses(e.g. have -- had, having), stemming is also necessary for better analysis. Here, we used NLTK(Natural Language Toolkit) for processing.
- **Combining variables with time/date.** A proper way to explore the trend for topics in subgroups(e.g. gender, party and publisher) is by observing the data over time. We aggregated the data by “date” and took week as a unit bin inste**ad of the day, aiming to reduce the fluctuation under fine-grained.
- **Word and sentence embeddings.** Transforming a word or sentence into a vector representation is widely used. Many methods have been developed including word2vec, transformer and BERT. Here, we use the BERT-Pretrained model to get the embeddings.
- **PCA and t-SNE.** Dimensionality reduction is important for visualizing the high-dimensional vector in lower dimensions. One of the popular methods is PCA. Another one is t-SNE, which is a nonlinear dimensionality reduction technique well-suited for high-dimensional data.
- **Cosine similarity.** Original useful information might be lost if a high-dimensional vector is mapped to a low-dimensional one. Thus, we can numerically compute the Cosine similarity between two vectors in addition to dimensionality reduction, which might be more accurate.

## Proposed timeline

- Milestone 2.1(11.13-11.26): Study subtopics of News bias, Partisan bias, Gender bias and finish data extraction functions.
- Milestone 2.2(11.27-12.03): Apply data processing pipeline on Quotebank datasets with different years, discover valuable and interesting patterns based on it, and conceptualize the data story.
- Milestone 2.3(11.4-12.10): Visualize the data including histogram, line-chart, scatterplot, etc. Design the layout and visual style of the website, then realize it.
- Milestone 2.4(12.11-12.17): Polish the data story to make it more intuitive and appealing. Check codes and documentation. Prepare the final presentation.

## Organization within the team

- Milestone  2.1
    - Xiaotian: For each publisher, analyse the most quoted topics and figures from political parties. Figure out the emotional bias of the words used in the quotations and each media outlet’s preference on neutral or radical words.
    - Siyi: Analyse the keywords in quotations within different political parties, the keywords used by political parties to quote their opponents, and the differences in the attitudes of different political parties towards some topics.
    - Xinyu: Study the gender bias in various topics and the changing tendency to quote male and female politicians in different media.
    - Xiaoyu: Evaluate the differences in the topics that speakers talk about at the gender level and whether gender bias is increasing or not.
- Milestone 2.2
    - Siyi, Xinyu: Apply pipeline and explore patterns.
    - All:  Conceptualize the data story.
- Milestone 2.3
    - Xiaoyu, Xiaotian: Visualize the data, design the layout and visual style of the website.
    - Siyi, Xinyu: Write code for the data story.
- Milestone 2.4
    - All: Final check and prepare for the presentation.

## Questions for TAs (optional)

Due to the limitation of computing power, it is not realistic to analyze the five years of data at one time. If we analyze it year by year, how can we combine them together more reasonably?


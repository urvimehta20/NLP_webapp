import streamlit as st 
import os
import json


# NLP Pkgs
from textblob import TextBlob 
import spacy

import nltk; nltk.download('punkt')

from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


#pos tagging 
nltk.download('averaged_perceptron_tagger')
# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	summary_result = str(result)
	return result

# Function to Analyse Tokens and Lemma
@st.cache
def text_analyzer(my_text):
	words = nltk.word_tokenize(my_text)
	return words 

#Function for POS tagging 
#@st.cache
#def pos_tagging(my_text):
#	pos_tags = nltk.pos(words)
#	return pos_tags

# Function For Extracting Entities
#@st.cache
#def entity_analyzer(my_text):
#	nlp = spacy.load('en')
#	docx = nlp(my_text)
#	tokens = [ token.text for token in docx]
#	entities = [(entity.text,entity.label_)for entity in docx.ents]
#	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
#	return allData


def main():
	""" NLP Based App """

	# Title
	st.title("NLP made fun!!")
	st.subheader("Natural Language Processing On One Go!!!")
	st.markdown("""
    	#### Description
    	+ This is a Natural Language Processing(NLP) Based App useful for NLP tasks that can be performed on any kind of text
    	""")

	# Tokenization
	if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize Your Text")

		message = st.text_area("Enter Text","")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)

	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Analyse Your Text")

		message = st.text_area("Enter Text","")
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

	# Summarization
	if st.checkbox("Show Text Summarization"):
		st.subheader("Summarize Your Text")

		message = st.text_area("Enter Text","")
		summary_options = st.selectbox("Summarizer Used",['sumy','gensim'])
		if st.button("Summarize"):
			if summary_options == 'sumy':
				st.text("Using Sumy Summarizer ..")
				summary_result = sumy_summarizer(message)
				st.success(summary_result)
				ser = message.count(" ")+1
				st.text("Wordcount of original text : " + str(ser))
				res = summary_result.count(" ")+1
				st.text("Wordcount of summarized text : " + str(res))
				
			elif summary_options == 'gensim':
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(message)
			else:
				st.warning("Using Default Summarizer")
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(message)


	# Pos Tagging
	#if st.checkbox("Show POS tags"):
	#	st.subheader("POS tag Your Text")

	#	message = st.text_area("Enter Text","Type Here ..")
	#	if st.button("Tag"):
	#		tag_result = pos_tagging(message)
	#		st.json(tag_result)

	# Entity Extraction
	#if st.checkbox("Show Named Entities"):
	#	st.subheader("Analyze Your Text")

	#	message = st.text_area("Enter Text","Type Here ..")
	#	if st.button("Extract"):
	#		entity_result = entity_analyzer(message)
	#		st.json(entity_result)


	st.sidebar.subheader("NLP made fun!!")
	st.sidebar.text("An app that can perform all the NLP text operations.")

	st.sidebar.subheader("By")
	st.sidebar.text("Urvi Mehta B03")
	st.sidebar.text("Mansi Dhokale B16")

if __name__ == '__main__':
	main()

	

	

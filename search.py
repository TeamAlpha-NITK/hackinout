import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp
object_set = []
threshold = 0.0

def get_objs_for_query(search_query):
	# tokenize
	doc = nlp(search_query)

	filtered_tokens = []
	# remove stop words
	for token in doc:
		print(token)
		lexeme = nlp.vocab[token]
		if lexeme.is_stop == False:
			filtered_tokens.append(token)
	
	# create map of token to set of objects
	#	1. if similarity is 1 only consider that
	#	2. else consider top 3 based on which qualify threshold reverse sorted
	query_tokens_objects = {}
	found_match = true
	for token in filtered_tokens:
		for object in object_set:
			similarity = token.lemma_.similarity.(object) # check if similarity function works on lemma_ of a token
			query_tokens_objects[token].append((object, similarity)
			if similarity == 1.0:
				found_match = true
				break
		if not found_match:
			# sort based on similarity
			query_tokens_objects[token].sort(key=operator.itemgetter(1), reverse=true)
			# get top three
			query_tokens_objects[token] = query_tokens_objects[token][:3]

def rank_videos(query_tokens_objects):
	query_token_videos = {}
	for query_token, objects in query_tokens_objects:
		for object, _ in objects: 
			# [(uid, count)] = db_query(object) -> video_info reverse sorted as per count
			video_info = [(0, 1)]
			query_token_videos[query_token] += video_info

if __init__ == '__main__':

	nlp = spacy.load('en_core_web_sm')
	
	with open('classes.txt') as f:
		object_set = f.readlines()
	object_set = [x.strip() for x in object_set] 

	threshold = 0.5

	# rank_videos(get_objs_for_query("man wearing black shoe"))
	get_objs_for_query("man wearing black shoe")

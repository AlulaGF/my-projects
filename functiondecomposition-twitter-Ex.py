def is_valid_tweet_length(tweet_text):
	"""Validates the tweet length."""
	if not tweet_text:
		return False # tweet text can not be empty
	if len(tweet_text) > 280:
		return False # tweet text length is less than 280 character
	return True

def are_valid_media_files(media_files):
	"""Validate the media files (basic checks)."""
    if media_file is None:
        return True #because attaching media file is optional
    elif isinstance(media_files, list):
    	return True # A list of media files 
    else:
    	return False
import paralleldots
paralleldots.set_api_key('NUNKqcYnIy5QffKF4pO0JoATQVTjy26vJIhoHFyWtGo')
def ner(text):
    response = paralleldots.ner(text)
    return response
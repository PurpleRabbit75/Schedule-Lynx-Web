# To whom it may concern:
This is my list of known bugs that I'm working on fixing. If you find another one, please open a new issue.

# Bugs

## JSON Display Object Persistence
When the user uploads a new configuration JSON, the old one that was printed is not removed from the UI
## JSON config file cannot be replaced on web application
- When the user uploads a json config file, it does not affect the functionality of the app except to raise an error
- to fix this, use the session state technique used in `upload.py`
## UI defaults to light mode rather than dark
- fix with a config.toml file (or somesuch--see Streamlit docs)
## Uploader glitch
When a user uploads 2 person.json files with the same name, the display is not updated. Additionally, the first one is kept, not the second. 
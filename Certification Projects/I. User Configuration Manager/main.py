def add_setting(settings, option):
    key, value = option
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, option):
    key, value = option
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
    

def delete_setting(settings, option):
    key = option
    key = key.lower()

    if key in settings:
        settings.pop(key, None)
        return f"Setting '{key}' deleted successfully!"
    
    return 'Setting not found!'

def view_settings(settings):
    preview = 'Current User Settings:\n'
    if len(settings):
        for key, value in settings.items():
            key = key.lower()
            value = value.lower()
            preview += f'{key.capitalize()}: {value}\n'
        return preview
    
    return 'No settings available.'


test_settings = {
    'volume': 'dark',
    'theme': 'dark'
}
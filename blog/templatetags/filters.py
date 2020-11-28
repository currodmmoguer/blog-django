from django import template

register = template.Library()

@register.filter
def hide_img(text):
    
    while '<img' in text:
        start = text.index('<img')
        end = text.index('/>', text.index('<img')) + len('/>')
        sbtr = text[start:end]
        text = text.replace(sbtr, '')
        text = text.replace('<p></p>', '')  # Elimina el párrafo que contiene la imagen
    return text
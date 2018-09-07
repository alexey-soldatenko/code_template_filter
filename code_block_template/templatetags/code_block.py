from django import template

register = template.Library()

def code_block(code):
    numbers = len(code.split('\n'))
    text_block = '<div class="code_text">'+code+"</div>"
    num_block = ""
    for num in range(numbers):
        num_block += str(num) + '<br>'
    num_block = '<div class="code_num">'+num_block+"</div>"
    owner_block = '<div class="code_owner">'+num_block+text_block+'</div>'
    return owner_block

register.filter('code_block', code_block)

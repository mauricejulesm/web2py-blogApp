# -*- coding: utf-8 -*-
# try something like

def display_form():
    form = SQLFORM(db.blog)
    if form.process().accepted:
        session.flash = 'Form accepted'
        redirect(URL('thanks'))
    elif form.errors:
        response.flash = 'Your form has shit errors'
    else:
        response.flash = 'You are new here, please fill out the damn form'
    return locals()

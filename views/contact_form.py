def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            find_us = form.cleaned_data['find_us']
            message = form.cleaned_data['message']
            # form.save()
            comment = 'Name: ' + name + " \nFrom: " + email + "\n\n" + message + "\n\n\nDepartment: " + find_us + "\nTEL: " + phone
            try:
                send_mail(
                    name,  # subject
                    comment,  # message
                    email,  # from email
                    [settings.EMAIL_HOST_USER],  # to email
                    fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            print('success')
            messages.success(request, f"{name} your message successfully sent!")
            return redirect("contact-page")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'web/contact.html', context)
